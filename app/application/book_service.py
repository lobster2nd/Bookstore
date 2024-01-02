from flask import Flask
from app.views.book import bp as book_bp
from database import db, Books


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../instance/project.db"
    db.init_app(app)
    app.register_blueprint(book_bp)
    return app


app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    rings = Books(book="Властелин колец", id=1)
    db.session.add(rings)
    great = Books(book="От хорошего к великому", id=2)
    db.session.add(great)
    db.session.commit()

if __name__ == "__main__":
    app.run()
