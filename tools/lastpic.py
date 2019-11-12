import sys
import base64
import sqlite3
import socketio
import time
import threading


class Config:
    def __init__(self, host_url, dbfilename):
        self.host_url = host_url
        self.dbfilename = dbfilename
        self.poll_sleep_secs = 0.1


def read_file(filename):
    with open(filename, "rb") as image_file:
        base64_bytes = base64.b64encode(image_file.read())
    return base64_bytes.decode('utf-8')


def poll_frame(cfg, state):
    with sqlite3.connect(cfg.dbfilename) as conn:
        cursor = conn.cursor()
        while True:
            # sql = "select '/home/stefan/repos/insects/backend/dummy/simon.jpg'"
            sql = 'select filename from security order by time_stamp desc limit 1'
            cursor.execute(sql)
            f = cursor.fetchone()[0]
            if f != state.file:
                return f
            else:
                print('meh')
            time.sleep(0.1)


def wait_next_frame(cfg, state, next_frame_available):
    f = poll_frame(cfg, state)
    state.file = f
    with next_frame_available:
        next_frame_available.notify()


def gen_callback(cfg, state, next_frame_available):
    def f():
        # threading.Thread(target=wait_next_frame, args=(cfg, state, next_frame_available)).start()
        return wait_next_frame(cfg, state, next_frame_available)
    return f


class State:
    def __init__(self):
        self.file = None


def main(cfg):
    sio = socketio.Client()
    sio.connect(cfg.host_url)

    state = State()
    next_frame_available = threading.Condition()
    wait_next_frame(cfg, state, next_frame_available)

    while True:
        if state.file is not None:
            base64_string = read_file(state.file)

            # TODO: Do i need to "clear" next_frame_available here?
            sio.emit('action', {"type": 'LIVEIMAGE_PUSH', "liveImage": base64_string}, callback=gen_callback(cfg, state, next_frame_available))

            print('Waiting for new image...')
            with next_frame_available:
                next_frame_available.wait()

            print('Confirmed!')


usage = '''
Usage: ./lastpic URL DBFILE
'''

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(usage)
        sys.exit(1)
    cfg = Config(sys.argv[1], sys.argv[2])
    main(cfg)
