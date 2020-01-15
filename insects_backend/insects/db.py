import datetime
import re
from .data import initialize
from . import models

from django.db import connection

THUMB_HEIGHT = 280
THUMB_WIDTH = int(1.3 * THUMB_HEIGHT)
THUMB_PREFIX = f'http://195.201.97.57:5556/unsafe/{THUMB_WIDTH}x{THUMB_HEIGHT}/'


def foo():
    # cursor = connection.cursor()
    # cursor.execute('select count(*) from insects_frame')
    # return cursor.fetchall()
    tbegin = datetime.datetime(2019, 11, 1)
    tend = datetime.datetime(2019, 11, 15)
    return get_subsample(tbegin, tend)


def equidx(n, k):
    '''
    Return a equispaced subsample from [1...n] of size k
    '''
    if k <= 0:
        return []
    delta = n / k
    if delta <= 1.0:
        return range(1, n)
    return [int(delta * i) for i in range(1, k + 1)]


def concat_paths(p1, p2):
    if p1.endswith('/'):
        p1 = p1[:-1]
    if p2.startswith('/'):
        p2 = p1[1:]
    return f'{p1}/{p2}'


def get_thumbnail(url):
    m = re.match('http(s)://(.+)', url)
    if m is None:
        return None
    _, x = m.groups()
    thumbnail = concat_paths(THUMB_PREFIX, x)
    return thumbnail


def make_frame(id_, timestamp, url):
    thumbnail = get_thumbnail(url)
    frame = models.Frame(id=id_, url=url, timestamp=timestamp, thumbnail=thumbnail)
    return frame


def get_frame(frame_id):
    cursor = connection.cursor()
    q = '''
        select
            id,
            timestamp,
            url
        from
            insects_frame
        where id = %s
    '''
    cursor.execute(q, (frame_id, ))
    (id_, timestamp, url) = cursor.fetchone()
    return make_frame(id_, timestamp, url)


def get_frames_continuous(tbegin, tend, after, nframes=10):
    frame = get_frame(after)
    cursor = connection.cursor()
    q = '''
    select
        id,
        timestamp,
        url
    from
        insects_frame
    where
        %s < timestamp
        and timestamp < %s
    order by timestamp asc, url asc
    limit %s
    '''
    cursor.execute(q, (frame.timestamp, tend, nframes))
    frames = []
    for (id_, timestamp, url) in cursor.fetchall():
        frame = make_frame(id_, timestamp, url)
        frames.append(frame)
    return frames


def get_frames_subsample(tbegin, tend, nframes=10):
    cursor = connection.cursor()

    q = '''
    select
        count(*)
    from
        insects_frame
    where
        %s <= timestamp
        and timestamp < %s
    '''
    cursor.execute(q, (tbegin, tend))
    (n, ) = cursor.fetchone()

    q2 = '''
    select
        x.id,
        x.timestamp,
        x.url
    from (
        select
            *,
            row_number() over (order by timestamp asc, url asc) as idx
        from
            insects_frame
        where
            %s <= timestamp
            and timestamp < %s
    ) x
        where x.idx in %s
    '''
    idxs = tuple(equidx(n, nframes))
    cursor.execute(q2, (tbegin, tend, idxs))
    rows = cursor.fetchall()

    frames = []
    for (id_, timestamp, url) in rows:
        frame = make_frame(id_, timestamp, url)
        frames.append(frame)

    return frames


def get_frames(tbegin, tend, nframes, after=None):
    '''
    If `after` is provided return the next nframes after it
    else return a equidistant sample in [tbegin, tend].

    Args:
        after (int): A frame_id
    '''
    if after is not None:
        return get_frames_continuous(tbegin=tbegin,
                                     tend=tend,
                                     nframes=nframes,
                                     after=after)
    else:
        return get_frames_subsample(tbegin=tbegin,
                                    tend=tend,
                                    nframes=nframes)