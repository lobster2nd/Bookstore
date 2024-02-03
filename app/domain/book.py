import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    publish_year = Column(Integer)
    pages_count = Column(Integer)
    created_at = Column(DateTime)
