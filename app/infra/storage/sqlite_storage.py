from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from domain.book import Base, Book


class SQLiteStorage:
    def __init__(self):
        engine = create_engine('sqlite:///database.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add(self, book):
        self.session.add(book)
        self.session.commit()
        return book.id

    def delete(self, id):
        book = self.session.query(Book).get(id)
        self.session.delete(book)
        self.session.commit()

    def get(self):
        return self.session.query(Book).all()
