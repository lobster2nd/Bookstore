import dataclasses
import datetime
import json

from flask import Blueprint, current_app, request, jsonify

from context import get_context
from domain.book import Book

bp = Blueprint("book", __name__)


@bp.route("/")
def get_books():
    ctx = get_context(current_app)
    books = ctx.book_service.get()
    serialized_books = [book_to_dict(book) for book in books]
    return jsonify(serialized_books)


def book_to_dict(book):
    return {
        'id': book.id,
        'title': book.title,
        'description': book.description,
        'publish_year': book.publish_year,
        'pages_count': book.pages_count,
        'created_at': book.created_at.strftime('%Y-%m-%d')
    }


@bp.route("/", methods=["POST"])
def add_book():
    ctx = get_context(current_app)

    created_at = datetime.datetime.strptime(request.json['created_at'],
                                            '%Y-%m-%d')
    book = Book(title=request.json['title'],
                description=request.json['description'],
                publish_year=request.json['publish_year'],
                pages_count=request.json['pages_count'],
                created_at=created_at)

    book_id = ctx.book_service.add(book)
    return jsonify({"id": book_id, "book": book.title})


@bp.route("/<id>", methods=["DELETE"])
def delete_book(id):
    ctx = get_context(current_app)

    ctx.book_service.delete(id)

    return jsonify({"message": "Книга успешно удалена"})
