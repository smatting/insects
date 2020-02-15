import datetime
import re
import math
import os
import json
import datetime
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from psycopg2.extras import execute_values
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
import logging

from . import models
from . models import Base, FramesQuery
from . utils import to_dict

ECODB = os.environ['ECODB']
# engine = create_engine(ECODB, echo=True)
engine = create_engine(ECODB, echo=False)
# session class
Session = sessionmaker(bind=engine)


def load_json(file):
    with open(file, 'r') as f:
        return json.load(f)


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


def pop_labels():
    labels = load_json('backend/data/labels.json')
    with session_scope() as session:
        session.query(models.Label).delete()
        for l in labels:
            label = models.Label(**l)
            session.add(label)


def manage_create_all():
    Base.metadata.create_all(engine)


def manage_migrate_labels():
    # models.AppearanceLabel.__table__.drop(engine)
    # models.Label.__table__.drop(engine)
    # models.Appearance.__table__.drop(engine)
    # Base.metadata.create_all(engine)
    pop_labels()


def fetch_frame_ids(session, frames_query, pagination=None):
    q_unpaged = '''
    select
        id
    from
    eco.frames
    where
        %(tbegin)s <= "timestamp"
        and "timestamp" < %(tend)s
    order by "timestamp" asc
    '''
    cursor = get_cursor(session)
    cursor.execute(q_unpaged, {'tbegin': frames_query.tbegin, 'tend': frames_query.tend})
    rows = cursor.fetchall()
    ids_ = [r[0] for r in rows]
    return ids_


def fetch_frame_ids_subsample(session, frames_query, nframes):
    '''
    Args:
        frames_query (FramesQuery):
    '''

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
    cursor.execute(q, {'tbegin': frames_query.tbegin, 'tend': frames_query.tend, 'n': nframes})
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
    cursor.execute(q2, {'tbegin': frames_query.tbegin, 'tend': frames_query.tend})
    count = cursor.fetchall()[0][0]

    return count, ids_


def get_frames_subsample(session, frames_query, nframes=10):
    count, ids = fetch_frame_ids_subsample(session, frames_query=frames_query, nframes=nframes)
    frames = session.query(models.Frame).filter(models.Frame.id.in_(ids)).all()
    return count, frames


def collection_add_frames_via_query(session, collection_id, frames_query, nframes=None):
    if nframes is None:
        ids_ = fetch_frame_ids(session, frames_query)
    else:
        _, ids_ = fetch_frame_ids_subsample(session, frames_query, nframes)

    data = [(collection_id, id_) for id_ in ids_]
    q = 'insert into eco.collection_frame (collection_id, frame_id) values %s on conflict do nothing'
    cursor = get_cursor(session)
    execute_values(cursor, q, data, page_size=1000)


def collection_remove_frames_via_query(session, collection_id, frames_query):
    ids_ = fetch_frame_ids(session, frames_query)
    q = 'delete from eco.collection_frame where collection_id = %s and frame_id in %s'
    cursor = get_cursor(session)
    cursor.execute(q, (collection_id, tuple(ids_)))


def test():
    with session_scope() as session:
        tbegin = datetime.datetime(2019, 11, 1)
        tend = datetime.datetime(2019, 11, 16)
        frames_query = FramesQuery(tbegin, tend)

        coll = models.Collection(name='foo')
        session.add(coll)
        session.flush()

        # collection_add_frames_via_query(session, coll.id, frames_query, nframes=100)
        collection_add_frames_via_query(session, coll.id, frames_query)
        print(f'collection id: {coll.id}')


def test2():
    with session_scope() as session:
        tbegin = datetime.datetime(2019, 11, 1)
        tend = datetime.datetime(2019, 11, 16)
        frames_query = FramesQuery(tbegin, tend)
        collection_remove_frames_via_query(session, 23, frames_query)
