from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Table, ForeignKey, Column, String, Integer, DateTime, Sequence)
from sqlalchemy.orm import relationship
import datetime


Base = declarative_base()

Base.metadata.schema = 'eco'


class Frame(Base):
    __tablename__ = 'frames'
    id = Column(Integer, Sequence('frame_id_seq'), primary_key=True)
    timestamp = Column(DateTime)
    url = Column(String)


collection_frame = \
    Table('collection_frame',
          Base.metadata,
          Column('collection_id', ForeignKey('collections.id'), primary_key=True),
          Column('frame_id', ForeignKey('frames.id'), primary_key=True))


class Collection(Base):
    __tablename__ = 'collections'
    id = Column(Integer, Sequence('collection_id_seq'), primary_key=True)
    name = Column(String)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)

    # frames = relationship('Frame', order_by=Frame.timestamp)
    frames = relationship('Frame', secondary=collection_frame)

