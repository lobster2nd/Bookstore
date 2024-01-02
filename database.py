from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "book": self.book
        }

