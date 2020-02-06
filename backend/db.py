import datetime
import re
import os
import datetime
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from .models import Base


ECODB = os.environ['ECODB']
engine = create_engine(ECODB, echo=True)
# session class
Session = sessionmaker(bind=engine)


THUMB_HEIGHT = 200
THUMB_WIDTH = int(1.3 * THUMB_HEIGHT)
THUMB_PREFIX = f'http://195.201.97.57:5556/unsafe/{THUMB_WIDTH}x{THUMB_HEIGHT}/'


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def get_cursor(session):
    return session.connection().connection.cursor()


def create_schema():
    Base.metadata.create_all(engine)


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
    # thumbnail = get_thumbnail(url)
    # frame = models.Frame(id=id_, url=url, timestamp=timestamp, thumbnail=thumbnail)
    thumbnail = get_thumbnail(url)
    frame = {'id': id_, 'timestamp': timestamp, 'url': url, 'thumbnail': thumbnail}
    return frame


# def get_frames_continuous(tbegin, tend, after, nframes=10):
#     frame = get_frame(after)
#     cursor = connection.cursor()
#     q = '''
#     select
#         id,
#         timestamp,
#         url
#     from
#         insects_frame
#     where
#         %s < timestamp
#         and timestamp < %s
#     order by timestamp asc, url asc
#     limit %s
#     '''
#     cursor.execute(q, (frame.timestamp, tend, nframes))
#     frames = []
#     for (id_, timestamp, url) in cursor.fetchall():
#         frame = make_frame(id_, timestamp, url)
#         frames.append(frame)
#     return len(frames), frames


def frames_fetch_sub(session, tbegin, tend, sub_fun):
    cursor = get_cursor(session)

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
    if n <= 0:
        return (0, [])

    idxs = tuple(sub_fun(n))
    if len(idxs) == 0:
        return []
    cursor.execute(q2, (tbegin, tend, idxs))
    rows = cursor.fetchall()

    frames = []
    for (id_, timestamp, url) in rows:
        frame = make_frame(id_, timestamp, url)
        frames.append(frame)

    return n, frames


def get_frames_subsample(session, tbegin, tend, nframes=10):
    return frames_fetch_sub(session, tbegin, tend, lambda n: equidx(n, nframes))


