import datetime
import re
import math
import os
import datetime
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from psycopg2.extras import execute_values
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

from . models import Base
from . import models
from . utils import to_dict

ECODB = os.environ['ECODB']
engine = create_engine(ECODB, echo=True)
# session class
Session = sessionmaker(bind=engine)



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


def manage_labels():
    wanted_labels = [
        'Heimchen (acheta domesticus)',
        'Wanderheuschrecke (locusta migratoria)',
        'Wüstenheuschrecke (schistocerca gregaria)',
    ]
    with session_scope() as session:
        session.query(models.Label).delete()
        for name in wanted_labels:
            label = models.Label(name=name)
            session.add(label)


def manage_create_all():
    Base.metadata.create_all(engine)


def manage_migrate():
    models.Appearance.__table__.drop(engine)
    Base.metadata.create_all(engine)


# def get_frames_continuous(tbegin, tend, after, nframes=10):
#     frame = get_frame(after)
#     cursor = connection.cursor()
#     q = '''
#     select
#         id,
#         timestamp,
#         url
#     from
#         eco.frames
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


def fetch_frames_subsample(session, tbegin, tend, n):
    q = '''
    with

    bounds as (
        select
            min(timestamp),
            max(timestamp)
        from
        eco.frames
        where
            %(tbegin)s <= "timestamp"
            and "timestamp" < %(tend)s
    ),

    ages as (
        select
            id,
            extract(epoch from age("timestamp", (select "min" from bounds limit 1))) age
        from
        eco.frames
        where
            %(tbegin)s <= "timestamp"
            and "timestamp" < %(tend)s
        order by "timestamp" asc
    ),

    cmps as (
        select
            id,
            floor(%(n)s * age / (select max(age) from ages))::int as n,
            lag(floor(%(n)s * age / (select max(age) from ages))::int) over () as n_lag
        from
            ages
    )

    select
        *
    from cmps
    where n != n_lag
        or n_lag is null
    '''
    cursor = get_cursor(session)
    cursor.execute(q, {'tbegin': tbegin, 'tend': tend, 'n': n})
    rows = cursor.fetchall()
    ids_ = [r[0] for r in rows]

    q2 = '''
        select
            count(*)
        from
        eco.frames
        where
            %(tbegin)s <= "timestamp"
            and "timestamp" < %(tend)s
    '''
    cursor.execute(q2, {'tbegin': tbegin, 'tend': tend})
    count = cursor.fetchall()[0][0]

    return count, ids_


def get_frames_subsample(session, tbegin, tend, nframes=10):
    count, ids = fetch_frames_subsample(session, tbegin, tend, n=nframes)
    frames = session.query(models.Frame).filter(models.Frame.id.in_(ids)).all()
    return count, frames


def test():
    with session_scope() as session:
        tbegin = datetime.datetime(2019, 11, 1)
        tend = datetime.datetime(2019, 11, 15)
        cnt, frames = get_frames_subsample(session, tbegin, tend, nframes=10)
        for frame in frames:
            return to_dict(frame)
