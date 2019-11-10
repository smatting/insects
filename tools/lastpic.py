import sys
import base64
import sqlite3
import socketio
import time


class Config:
    def __init__(self, host_url, dbfilename):
        self.host_url = host_url
        self.dbfilename = dbfilename


def read_file(filename):
    with open(filename, "rb") as image_file:
        base64_bytes = base64.b64encode(image_file.read())
    return base64_bytes.decode('utf-8')


def update_image(sio, filename):
    print('emitting new image')
    base64_string = read_file(filename)
    sio.emit('action', {"type": 'LIVEIMAGE_PUSH', "liveImage": base64_string})


def get_last(dbfilename):
    '''
    load frames out of a Motion sqlite3 database
    '''
    with sqlite3.connect(dbfilename) as conn:
        sql = 'select filename from security order by time_stamp desc limit 1'
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchone()[0]


def main(cfg):
    sio = socketio.Client()
    sio.connect(cfg.host_url)

    filename = None
    while True:
        filename_poll = get_last(cfg.dbfilename)
        if filename_poll != filename:
            filename = filename_poll
        if filename is not None:
            update_image(sio, filename)
        time.sleep(0.1)


usage = '''
Usage: ./lastpic URL DBFILE
'''

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(usage)
        sys.exit(1)
    cfg = Config(sys.argv[1], sys.argv[2])
    main(cfg)
