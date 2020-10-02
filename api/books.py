from flask import request
from database import get_db
import nanoid


def get_all_books():
    pass


def add_new_book():
    title = request.form.get("title")
    if not title:
        return "No title given"
    book_id = nanoid.generate()

    try:
        db = get_db()
        c = db.cursor()
        c.execute("INSERT INTO book(title, _id) VALUES(?, ?)", (title, book_id))
        db.commit()

        return {"title": title, "_id": book_id}

    except:
        return "Database error"


def delete_all_books():
    pass


def get_one_book(book_id):
    pass


def add_comment(book_id):
    pass


def delete_one_book(book_id):
    pass
