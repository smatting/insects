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
    scientificName = Column(String)
    systematicLevel = Column(String)


class AppearanceLabel(Base):
    __tablename__ = 'appearance_label'
    id = Column(Integer, Sequence('appearance_label_id_seq'), primary_key=True)
    creator_id = Column(Integer, ForeignKey('creators.id'))
    label_id = Column(Integer, ForeignKey('labels.id'))
    date_created = Column(DateTime, default=datetime.datetime.utcnow)


appearance_label_link = \
    Table('appearance_label_link',
          Base.metadata,
          Column('appearance_id', ForeignKey('appearances.id'), primary_key=True),
          Column('appearance_label_id', ForeignKey('appearance_label.id'), primary_key=True))


class Appearance(Base):
    __tablename__ = 'appearances'
    id = Column(Integer, Sequence('appearance_id_seq'), primary_key=True)
    frame_id = Column(Integer, ForeignKey('frames.id'), nullable=False)
    frame = relationship('Frame')
    appearance_labels = relationship('AppearanceLabel', secondary=appearance_label_link)
    bbox_xmin = Column(Float)
    bbox_xmax = Column(Float)
    bbox_ymin = Column(Float)
    bbox_ymax = Column(Float)
    creator_id = Column(Integer, ForeignKey('creators.id'))

################################################################################
