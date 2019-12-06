from database import Base
from sqlalchemy import Table, Column, DateTime, Float, ForeignKey, Integer, String, Boolean, Enum
from sqlalchemy.orm import backref, relationship


class Process(Base):
    __tablename__ = 'process'
    id = Column(Integer, primary_key=True)
#     properties = Column(Json)


frame_collection = Table('frame_collection', Base.metadata,
    Column('frame_id', Integer, ForeignKey('frame.id')),
    Column('collection_id', Integer, ForeignKey('collection.id'))
)

class Frame(Base):
    __tablename__ = 'frame'
    id = Column(Integer, primary_key=True)
    process_id = Column(Integer, ForeignKey('process.id'))
    timestamp = Column(DateTime)
    url = Column(String)
    # properties = Column(Json)
    process = relationship(
        Process,
        backref=backref('frames',
                        uselist=True,
                        cascade='delete,all'))
    collections = relationship(
        'collection',
        secondary=frame_collection,
        backref=backref('frames',
                        uselist=True,
                        cascade='delete,all'))


class BoundingBox(Base):
    __tablename__ = 'boundingbox'
    id = Column(Integer, primary_key=True)
    process_id = Column(Integer, ForeignKey('process.id'))
    x = Column(Integer)
    y = Column(Integer)
    width = Column(Integer)
    heigth = Column(Integer)
#     properties = Column(Json)
    process = relationship(
        Process,
        backref=backref('boundingboxes',
                        uselist=True,
                        cascade='delete,all'))


class Appearance(Base):
    __tablename__ = 'appearance'
    id = Column(Integer, primary_key=True)
    process_id = Column(Integer, ForeignKey('process.id'))
    frame_id = Column(Integer, ForeignKey('frame.id'))
    boundingbox_id = Column(Integer, ForeignKey('boundingbox.id'))
    tracking_id = Column(Integer, ForeignKey('tracking.id'))
#     properties = Column(Json)
    process = relationship(
        'process',
        backref=backref('appearances',
                        uselist=True,
                        cascade='delete,all'))
    frame = relationship(
        'frame',
        backref=backref('appearances',
                        uselist=True,
                        cascade='delete,all'))
    boundingbox = relationship(
        'boundingbox',
        backref=backref('appearances',
                        uselist=True,
                        cascade='delete,all'))
    tracking = relationship(
        'tracking',
        backref=backref('appearances',
                        uselist=True,
                        cascade='delete,all'))


class Tracking(Base):
    __tablename__ = 'tracking'
    id = Column(Integer, primary_key=True)
    process_id = Column(Integer, ForeignKey('process.id'))
#     properties = Column(Json)
    process = relationship(
        Process,
        backref=backref('trackings',
                        uselist=True,
                        cascade='delete,all'))


class SpecimenClass(Base):
    __tablename__ = 'specimen_class'
    id = Column(Integer, primary_key=True)
    process_id = Column(Integer, ForeignKey('process.id'))
#     properties = Column(Json)
    process = relationship(
        Process,
        backref=backref('classes',
                        uselist=True,
                        cascade='delete,all'))


class Classification(Base):
    __tablename__ = 'classification'
    id = Column(Integer, primary_key=True)
    process_id = Column(Integer, ForeignKey('process.id'))
    appearance_id = Column(Integer, ForeignKey('appearance.id'))
    tracking_id = Column(Integer, ForeignKey('tracking.id'))
    ctype = Column(Enum('APEARANCE', 'TRACKING'))
#     properties = Column(Json)
    process = relationship(
        Process,
        backref=backref('classifications',
                        uselist=True,
                        cascade='delete,all'))
    appearance = relationship(
        Process,
        backref=backref('classifications',
                        uselist=True,
                        cascade='delete,all'))


class ClassificationValue(Base):
    __tablename__ = 'classification_value'
    id = Column(Integer, primary_key=True)
    classification_id = Column(Integer, ForeignKey('classification.id'))
    class_id = Column(Integer, ForeignKey('class.id'))
    value = Column(Float)
    is_maximum = Column(Boolean)
    classification = relationship(
        Classification,
        backref=backref('classification_values',
                        uselist=True,
                        cascade='delete,all'))
    specimen_class = relationship(
        SpecimenClass,
        backref=backref('classification_values',
                        uselist=True,
                        cascade='delete,all'))




class Collection(Base):
    __tablename__ = 'collection'
    id = Column(Integer, primary_key=True)
    process_id = Column(Integer, ForeignKey('process.id'))
    process = relationship(
        Process,
        backref=backref('relations',
                        uselist=True,
                        cascade='delete,all'))
    frames = relationship(
        Frame,
        secondary=frame_collection,
        backref=backref('relations',
                        uselist=True,
                        cascade='delete,all'))


