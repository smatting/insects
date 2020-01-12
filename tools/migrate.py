#!/usr/bin/env python3

import psycopg2
import os
import re
import csv


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


def connect_db():
    return psycopg2.connect(os.environ['ECODB'])


def all_frames(cursor):
    q = '''
    select
        id,
        cam_id,
        filename,
        frame,
        time_stamp,
        event_time_stamp,
        local_filename
    from
        frame
    order by time_stamp asc
    '''
    cursor.execute(q)
    return cursor.fetchall()


'''
create table frame_newname
(
    id text,
    cam_id text,
    filename text,
    frame int,
    time_stamp timestamp,
    event_time_stamp timestamp,
    local_filename text,
    id_new text,
    batch int
);
'''

regex = re.compile(r'cam1/(\d+)-(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})-(\d+)\.jpg')


def rename(old_id):
    (v, y, m, d, H, M, S, n) = re.match(regex, old_id).groups()
    new_name = f'cam1/{y}-{m}-{d}/{H}/{v}-{y}{m}{d}{H}{M}{S}-{n}.jpg'
    return new_name


def debug():
    with connect_db() as conn:
        cursor = conn.cursor()
        frames = all_frames(cursor)
        return frames


def debug2():
    return rename('cam1/01-20191018122858-03.jpg')


def convert(rows):
    rows_new = []
    for i, row in enumerate(rows):
        try:
            r = list(row)[:]
            r.append(rename(row[0]))
            batch = i // 250 + 1
            r.append(batch)
            rows_new.append(r)
        except Exception:
            print(f'{i} failed')
    return rows_new


def upload_new(rows):
    with connect_db() as conn:
        cursor = conn.cursor()

        f = CSVLikeFile(rows)
        cursor.execute('truncate frame_newname')
        cursor.copy_expert(f'copy frame_newname from stdin with csv delimiter \',\';', f)
        conn.commit()


def get_batch(cursor, batch):
    q = 'select * from frame_newname where batch = %s'
    cursor.execute(q, (batch,))
    return cursor.fetchall()


def foo():
    with connect_db() as conn:
        cursor = conn.cursor()
        return get_batch(cursor, 1)


def create_script(rows, batch):
    cmds = []
    cmds.append(f'echo "Processing batch {batch}"')
    cmds.append('rm -rf /tmp/stage/*')
    for row in rows:
        dst = f'/tmp/stage/{row[-2]}'
        dst_dir = os.path.dirname(dst)
        cmds.append(f'mkdir -p {dst_dir}')
        cmds.append(f'rsync -qv /media/usb/cam1/frames/{row[2]} {dst}')
    cmds.append('gsutil cp -r /tmp/stage/cam1/ gs://eco1/frames/')
    return '\n'.join(cmds)


def main():
    scripts = []
    with connect_db() as conn:
        cursor = conn.cursor()
        for batch in range(1, 360):
            print(batch)
            rows = get_batch(cursor, batch)
            scripts.append(create_script(rows, batch))

    with open('sync.sh', 'w') as f:
        f.write('\n\n'.join(scripts))
