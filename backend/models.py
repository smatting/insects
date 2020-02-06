from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Table, ForeignKey, Column, String, Integer, Float, DateTime, Sequence)
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


class Creator(Base):
    '''
    Thing that created things: Algorithm or a user
    '''
    __tablename__ = 'creators'
    id = Column(Integer, Sequence('creator_id_seq'), primary_key=True)
    name = Column(String)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)


class Label(Base):
    __tablename__ = 'labels'
    id = Column(Integer, Sequence('label_id_seq'), primary_key=True)
    name = Column(String)


class Appearance(Base):
    __tablename__ = 'appearances'
    id = Column(Integer, Sequence('appearance_id_seq'), primary_key=True)
    frame_id = Column(Integer, ForeignKey('frames.id'), nullable=False)
    frame = relationship('Frame')
    bbox_xmin = Column(Float)
    bbox_xmax = Column(Float)
    bbox_ymin = Column(Float)
    bbox_ymax = Column(Float)
    label_id = Column(Integer, ForeignKey('labels.id'))
    creator_id = Column(Integer, ForeignKey('creators.id'))

################################################################################
