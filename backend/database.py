from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import Frame, Process, BoundingBox, Appearance, Tracking, SpecimenClass, Classification, ClassificationValue, Collection
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Create the fixtures
    process = Process()

    frame1 = Frame(process_id=process.id, url='test1')
    frame2 = Frame(process_id=process.id, url='test2')
    frame3 = Frame(process_id=process.id, url='test3')

    coll1 = Collection(process_id=process.id)

    coll1.frames.append(frame1)
    coll1.frames.append(frame2)

    db_session.add(process)
    db_session.add(frame1)
    db_session.add(frame2)
    db_session.add(frame3)
    db_session.add(coll1)

    db_session.commit()
