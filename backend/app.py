from flask import Flask, send_from_directory
from flask_socketio import SocketIO, send, emit
import base64


app = Flask(__name__, static_url_path='')
# app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO()
socketio.init_app(app, cors_allowed_origins="*")


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


@socketio.on('connect')
def handle_connection():
    print('Connected Client')

@socketio.on('action')
def handle_action_mouse(action):
    print(action)
    if action['type'] == 'LIVEIMAGE_PUSH':
        emit('action', {"type": 'LIVEIMAGE_NEW', "liveImage": action['liveImage']}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
