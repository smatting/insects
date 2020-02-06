from flask import Flask
from flask_socketio import SocketIO, send, emit
import datetime
from . import db


app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO()
socketio.init_app(app, cors_allowed_origins="*")


def test():
    with db.session_scope() as session:
        tbegin = datetime.datetime(2019, 11, 1)
        tend = datetime.datetime(2019, 11, 15)
        return db.get_frames_subsample(session, tbegin, tend, 10)


@socketio.on('connect')
def handle_connection():
    emit('action', {"type": 'SERVER_INIT'})


def update_search(action):
    search = action['search']
    ntotal, frames = db.get_frames(tbegin=search['startDate'], tend=search['endDate'], nframes=10, after=None)
    search_results = {'ntotal': ntotal, 'frames': frames}
    emit('action', {"type": 'SEARCH_UPDATED', 'searchResults': search_results})


@socketio.on('action')
def handle_actions(action):
    print(action)
    if action['type'] == "SEARCH_UPDATE":
        update_search(action)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True, port=5000)
