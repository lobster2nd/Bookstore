from flask import Blueprint, jsonify, request
from database import db, Books

bp = Blueprint("book", __name__)


@bp.route("/")
def get_books():
    books = Books.query.all()
    return jsonify([book.serialize() for book in books])


@bp.route("/", methods=["POST"])
def add_book():
    data = request.get_json()
    book = Books(id=data["id"], book=data["book"])
    db.session.add(book)
    db.session.commit()
    return jsonify(data)


@bp.route("/<id>", methods=["DELETE"])
def delete_book(id):
    book = Books.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
    return jsonify({})
