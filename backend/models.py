from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, String, Integer, DateTime, Sequence)
from sqlalchemy.orm import relationship


Base = declarative_base()

Base.metadata.schema = 'eco'


class Frame(Base):
    __tablename__ = 'frames'
    id = Column(Integer, Sequence('frame_id_seq'), primary_key=True)
    timestamp = Column(DateTime)
    url = Column(String)


class Collection(Base):
    __tablename__ = 'collections'
    id = Column(Integer, Sequence('collection_id_seq'), primary_key=True)
    name = Column(String)
    date_created = Column(DateTime)
