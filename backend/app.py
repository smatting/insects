from flask import Flask
from flask_socketio import SocketIO, send, emit
import datetime
from . import db
from . import models

from sqlalchemy import inspect



# NOTE: relationship fields will be missing
def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


app = Flask(__name__)
socketio = SocketIO()
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
        # return [object_as_dict(f) for f in frames]

        # EXAMPLE: remove frame from collection
        coll = session.query(models.Collection).get(7);


@socketio.on('connect')
def handle_connection():
    emit('action', {"type": 'SERVER_INIT'})


def update_search(action):
    search = action['search']
    ntotal, frames = db.get_frames(tbegin=search['startDate'], tend=search['endDate'], nframes=10, after=None)
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
