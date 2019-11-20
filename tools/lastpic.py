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
    cursor = state.conn.cursor()
    while True:
        # sql = "select '/home/stefan/repos/insects/backend/dummy/simon.jpg'"
        try:
            sql = 'select filename from security order by time_stamp desc limit 1'
            cursor.execute(sql)
            f = cursor.fetchone()[0]
            if f != state.file:
                cursor.close()
                return f
            time.sleep(cfg.poll_sleep_secs)
        except Exception as e:
            print('There was an exception: {}'.format(e))


def wait_next_frame(cfg, state):
    f = poll_frame(cfg, state)
    state.file = f


def gen_callback(server_received_image):
    def f():
        with server_received_image:
            server_received_image.notify()
    return f


class State:
    def __init__(self, conn):
        self.file = None
        self.conn = conn


def main(cfg):
    sio = socketio.Client()
    sio.connect(cfg.host_url)

    conn = sqlite3.connect(cfg.dbfilename)
    state = State(conn)

    server_received_image = threading.Condition()

    while True:
        wait_next_frame(cfg, state)

        print('Found new picture!')
        base64_string = read_file(state.file)

        sio.emit('action', {"type": 'LIVEIMAGE_PUSH', "liveImage": base64_string}, callback=gen_callback(server_received_image))
        with server_received_image:
            server_received_image.wait()
        print('Image pushed to server')



usage = '''
Usage: ./lastpic URL DBFILE
'''

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(usage)
        sys.exit(1)
    cfg = Config(sys.argv[1], sys.argv[2])
    main(cfg)
