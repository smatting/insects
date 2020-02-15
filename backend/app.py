from flask import Flask
from flask_socketio import SocketIO, send, emit
import datetime
import json
import numpy as np
from . import db
from . import models

from .utils import snakeize_dict_keys, camelize_dict_keys, to_dict

from sqlalchemy import inspect
from sqlalchemy.ext.declarative import DeclarativeMeta


def id_to_str(obj):
    return {**obj, 'id': str(obj['id'])}


# credit: https://stackoverflow.com/questions/44146087/pass-user-built-json-encoder-into-flasks-jsonify
class Better_JSON_ENCODER(json.JSONEncoder):
    '''
    Used to help jsonify numpy arrays or lists that contain numpy data types.
    '''
    def default(self, obj):
        print(obj)
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, (datetime.datetime, datetime.date)):
            print('datetime', obj)
            return obj.isoformat()
        else:
            return super(Better_JSON_ENCODER, self).default(obj)


# credit: https://github.com/miguelgrinberg/Flask-SocketIO/issues/274
class BetterJsonWrapper(object):
    @staticmethod
    def dumps(*args, **kwargs):
        if 'cls' not in kwargs:
            kwargs['cls'] = Better_JSON_ENCODER
        return json.dumps(*args, **kwargs)

    @staticmethod
    def loads(*args, **kwargs):
        return json.loads(*args, **kwargs)


app = Flask(__name__)
socketio = SocketIO(json=BetterJsonWrapper)
socketio.init_app(app, cors_allowed_origins="*")



def test():
    with db.session_scope() as session:
        tbegin = datetime.datetime(2019, 11, 1)
        tend = datetime.datetime(2019, 11, 15)

        # EXAMPLE: get subsample
        # return db.get_frames_subsample(session, tbegin, tend, 10)

        # EXAMPLE: get single frame
        # f = session.query(models.Frame).get(16597);

        # EXAMPLE: add collection
        # coll = models.Collection(name='test')
        # session.add(coll)

        # EXAMPLE: add subsample to collection
        # coll = models.Collection(name='test')
        # session.add(coll)
        # session.flush()
        # db.collection_add_frames_subsample(session, coll.id, tbegin, tend, 10)

        # EXAMPLE: get collection with frames
        # coll =  session.query(models.Collection).get(7);
        # frames = coll.frames
        # return [to_dict(f) for f in frames]

        # EXAMPLE: remove frame from collection
        # coll = session.query(models.Collection).get(7);
        # return to_dict(coll, rels=['frames'])

        # EXAMPLE: add an appearance
        # frame = session.query(models.Frame).first()
        # app = models.Appearance(frame=frame)
        # session.add(app)

        # EXAMPLE: update bbox
        # app = session.query(models.Appearance).first()
        # app.bbox_xmin = 42

        # EXAMPLE: get all labels
        # labels = session.query(models.Label).all()
        # return [to_dict(label) for label in labels]


def _get_all(model):
    with db.session_scope() as session:
        objs = session.query(model).all()
        objs = [id_to_str(to_dict(o)) for o in objs]
    return objs


def load_collection(collection_id):
    with db.session_scope() as session:
        coll = session.query(models.Collection).get(collection_id)
        frames = coll.frames
        coll = {'id': coll.id, 'frames': [id_to_str(to_dict(f)) for f in frames]}
    emit('action', {"type": 'COLLECTION_LOADED', 'collection': coll})


def delete_appearance():
    #TODO
    pass
    # emit('action', {"type": 'APPEARANCE_DELETED', 'collection': coll})


def add_appearance(frameId, appearance):
    with db.session_scope() as session:
        frame = session.query(models.Frame).get(frameId)
        print(appearance)
        app = models.Appearance(frame=frame, **snakeize_dict_keys(appearance))
        session.add(app)
        session.commit()
        app_dict = camelize_dict_keys(id_to_str(to_dict(app)))
    emit('action', {
        "type": 'APPEARANCE_ADDED',
        'appearance': app_dict,
        'frameId': frameId
    })


@socketio.on('connect')
def handle_connection():
    pass
    # species = _get_all(models.Label)
    # collections = _get_all(models.Collection)
    # emit('action', {"type": 'SERVER_INIT', 'species': species, 'collections': collections})

    # load_collection(7)


def update_search(action):
    search = action['search']
    with db.session_scope() as session:
        ntotal, frames = db.get_frames_subsample(session, tbegin=search['startDate'], tend=search['endDate'], nframes=10)
        search_results = {'ntotal': ntotal, 'frames': [to_dict(frame) for frame in frames]}

        # print(f'ntotal: {ntotal}')
        print(f'ntotal: {ntotal}')
        print(f'len(frames): {len(search_results["frames"])}')

        # print(search_results)
        emit('action', {"type": 'SEARCH_UPDATED', 'searchResults': search_results})


@socketio.on('action')
def handle_actions(action):
    print(action)
    if action['type'] == "SEARCH_UPDATE":
        update_search(action)
    if action['type'] == "APPEARANCE_ADD":
        print('APPEARANCE_ADD', action)
        add_appearance(action['frameId'], action['appearance'])
    if action['type'] == "APPEARANCE_DELETE":
        print('APPEARANCE_ADD', action)
    if action['type'] == "COLLECTIONFRAME_SELECT":
        print('COLLECTIONFRAME_SELECT', action)



def debug():
    socketio.run(app, host='0.0.0.0', debug=True, port=5000)
