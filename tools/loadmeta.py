#!/usr/bin/env python3

import psycopg2
import sqlite3
import re
import dateutil.parser
import datetime
import os
import csv
import docopt

stage_ddl = '''
create table staging.frames
(
    id text,
    cam_id text,
    filename text,
    frame int,
    time_stamp timestamp,
    event_time_stamp timestamp,
    local_filename text
);
'''

insert_sql = '''
insert into frame
(
    select
        *
    from
        frame_staging
    where id not in (select id from frame)
)
returning id
'''

dr = re.compile(r'(\d\d\d\d)(\d\d)(\d\d)(\d\d)(\d\d)(\d\d)')

def connect_db():
    return psycopg2.connect(os.environ['ECODB'])

def parse_decimal_stamp(k):
    """20191018133916"""
    """2019 10 18 13 39 16"""
    m = re.match(dr, str(k))
    if m is not None:
        ll = m.groups()
        ll = [int(x) for x in ll]
        year, month, day, hour, minute, second = ll
        dt = datetime.datetime(year, month, day, hour, minute, second)
        return dt
    else:
        raise ValueError('Cannot parse {}'.format(k))


def format_timestamp(dt):
    pass

class CSVLikeFile:
    '''
    Wrap table data [row, row, ...] as a file-like object that contains CSV.
    '''

    def __init__(self, table):
        self.array = iter(table)
        self._rest = ''
        self._buffer = self._Buffer()
        self._writer = csv.writer(self._buffer)

    def read(self, size=None):
        try:
            while not size or len(self._rest) < size:
                self._writer.writerow(next(self.array))
                self._rest += self._buffer.row
            response = self._rest[:size]
            self._rest = self._rest[size:]
            return response

        except StopIteration:
            response = self._rest
            self._rest = ''
            return response

    def readline(self, size=None):
        try:
            if not self._rest:
                self._writer.writerow(next(self.array))
                self._rest += self._buffer.row

            if '\n' in self._rest:
                newline = self._rest.index('\n')
            else:
                newline = len(self._rest)

            if not size or size < 0:
                size = len(self._rest)

            part_size = min(newline, size)
            result = self._rest[:part_size]
            self._rest = self._rest[part_size:]
            return result

        except StopIteration:
            response = self._rest
            self._rest = ''
            return response

    class _Buffer:
        row = ''

        def write(self, string):
            self.row = string

def load_frames(filename, cam_id):
    '''
    load frames out of a Motion sqlite3 database
    '''
    with sqlite3.connect(filename) as conn:
        cursor = conn.cursor()
        q = 'select filename, frame, time_stamp, event_time_stamp from security'
        columns = ['filename', 'frame', 'time_stamp', 'event_time_stamp']
        cursor.execute(q)
        result = []
        for row in cursor.fetchall():
            d = dict(zip(columns, row))
            d['local_filename'] = d['filename']
            d['filename'] = os.path.basename(d['filename'])
            d['time_stamp'] = dateutil.parser.parse(d['time_stamp'])
            d['event_time_stamp'] = parse_decimal_stamp(d['event_time_stamp'])
            d['cam_id'] = cam_id
            d['id'] = str(d['cam_id']) + '/' + d['filename']
            # TODO: is this UTC or local time zone ??
            result.append(d)
        return result


def get_rows(frames, columns):
    for event in frames:
        yield [event[col] for col in columns]

def insert_frames(cursor, frames):
    columns = [
        'id',
        'cam_id',
        'filename',
        'frame',
        'time_stamp',
        'event_time_stamp',
        'local_filename'
    ]
    f = CSVLikeFile(get_rows(frames, columns))
    # cursor.execute(stage_ddl)
    cursor.copy_expert(f'copy staging.frames from stdin with csv delimiter \',\';', f)

    # cursor.execute(insert_sql)
    # x = cursor.fetchall()
    # return x

def run(sqlite_db, cam_id):
    '''
    Usage: loadmeta <sqlite-db> <cam-id>
    '''
    # fn = '/home/stefan/Downloads/frames.db'
    frames = load_frames(sqlite_db, 'cam1')
    print(f'Found {len(frames)} frames in sqlite db')
    with connect_db() as conn:
        cursor = conn.cursor()
        ids = insert_frames(cursor, frames)
        # print(f'Inserted {len(ids)} new frames to DB')


def main():
    args = docopt.docopt(run.__doc__)
    run(args['<sqlite-db>'], args['<cam-id>'])


if __name__ == '__main__':
    main()
