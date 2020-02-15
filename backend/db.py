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
from collections import namedtuple

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


SqlExpr = namedtuple('SqlExpr', ['from_expr', 'where_clauses'])


def sql_expr(frames_query):
    if frames_query.collection_id is not None:
        from_expr = '''
        eco.frames f
        inner join eco.collection_frame cf
            on cf.frame_id = f.id
            and cf.collection_id = %(collection_id)s
        '''
    else:
        from_expr = '''
        eco.frames f
        '''

    if frames_query.tbegin is not None and frames_query.tend is not None:
        where_clauses = [
            '%(tbegin)s <= "timestamp"',
            '"timestamp" < %(tend)s'
        ]
    else:
        where_clauses = []
    return SqlExpr(from_expr, where_clauses)


def sqlify_where(where_clauses):
    if len(where_clauses) == 0:
        return ''
    else:
        s = ' and '.join(f'({wc})' for wc in where_clauses)
        return f'where {s}'


def sqlify_sql_expr(sql_expr):
    where_sql = sqlify_where(sql_expr.where_clauses)
    s = f'{sql_expr.from_expr} {where_sql}'
    return s


def frames_query_dict(frames_query):
    d = {}
    if frames_query.tbegin is not None:
        d['tbegin'] = frames_query.tbegin

    if frames_query.tend is not None:
        d['tend'] = frames_query.tend

    if frames_query.collection_id is not None:
        d['collection_id'] = frames_query.collection_id

    return d


def fetch_frame_ids(session, frames_query, pagination=None):
    q = f'''
    select
        f.id
    from
    {sqlify_sql_expr(sql_expr(frames_query))}
    order by "timestamp" asc
    '''
    print(q)
    cursor = get_cursor(session)
    cursor.execute(q, frames_query_dict(frames_query))
    rows = cursor.fetchall()
    ids_ = [r[0] for r in rows]
    return ids_


def fetch_frame_ids_subsample(session, frames_query, nframes):
    '''
    Args:
        frames_query (FramesQuery):
    '''

    q = f'''
    with

    bounds as (
        select
            min(f."timestamp"),
            max(f."timestamp")
        from
        {sqlify_sql_expr(sql_expr(frames_query))}
    ),

    ages as (
        select
            id,
            extract(epoch from age("timestamp", (select "min" from bounds limit 1))) age
        from
        {sqlify_sql_expr(sql_expr(frames_query))}
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
    d = frames_query_dict(frames_query)
    d['n'] = nframes
    cursor = get_cursor(session)
    cursor.execute(q, d)
    rows = cursor.fetchall()
    ids_ = [r[0] for r in rows]

    q2 = f'''
        select
            count(*)
        from
        {sqlify_sql_expr(sql_expr(frames_query))}
    '''
    cursor.execute(q2, frames_query_dict(frames_query))
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
        frames_query = FramesQuery(tbegin, tend, None)

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
        frames_query = FramesQuery(tbegin, tend, None)
        return frames_query
        collection_remove_frames_via_query(session, 23, frames_query)


def test3():
    with session_scope() as session:
        frames_query = FramesQuery(None, None, 27)
        return fetch_frame_ids_subsample(session, frames_query, 10)
