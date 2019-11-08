import socketio
import base64

def update_image(sio):
    with open('dummy/test.jpg', "rb") as image_file:
        base64_bytes = base64.b64encode(image_file.read())
    base64_string = base64_bytes.decode('utf-8')
    sio.emit('action', {"type": 'LIVEIMAGE_PUSH', "liveImage": base64_string})


if __name__ == '__main__':
    # standard Python
    sio = socketio.Client()
    sio.connect('http://localhost:5000')
    update_image(sio)
