from flask import Flask
from flask_socketio import SocketIO, send, emit
import datetime
import json
import numpy as np
from . import db
from . import models

from sqlalchemy import inspect
from sqlalchemy.ext.declarative import DeclarativeMeta


def to_dict(obj, rels=[], backref=None):
    '''
    Turn models to dicts. Nested relationships listed in `rels` are turned to dicts too,
    otherwise they are missing. Hacky, barely tested.

    From https://mmas.github.io/sqlalchemy-serialize-json
    '''
    res = {column.key: getattr(obj, attr)
           for attr, column in obj.__mapper__.c.items()}
    if len(rels) > 0:
        for attr, relation in obj.__mapper__.relationships.items():
            if attr not in rels:
                continue

            if hasattr(relation, 'table'):
                if backref == relation.table:
                    continue

            value = getattr(obj, attr)
            if value is None:
                res[relation.key] = None
            elif isinstance(value.__class__, DeclarativeMeta):
                res[relation.key] = to_dict(value, backref=obj.__table__, rels=rels)
            else:
                res[relation.key] = [to_dict(i, backref=obj.__table__, rels=rels)
                                     for i in value]
    return res



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



@socketio.on('connect')
def handle_connection():
    emit('action', {"type": 'SERVER_INIT'})


def update_search(action):
    search = action['search']
    with db.session_scope() as session:
        ntotal, frames = db.get_frames_subsample(session, tbegin=search['startDate'], tend=search['endDate'], nframes=10)
    search_results = {'ntotal': ntotal, 'frames': frames}
    print(search_results)
    emit('action', {"type": 'SEARCH_UPDATED', 'searchResults': search_results})


@socketio.on('action')
def handle_actions(action):
    print(action)
    if action['type'] == "SEARCH_UPDATE":
        update_search(action)


def debug():
    socketio.run(app, host='0.0.0.0', debug=True, port=5000)
