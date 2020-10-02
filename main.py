from flask import Flask, g, render_template
from database import init_db
from api.books import (
    get_all_books,
    add_new_book,
    delete_all_books,
    get_one_book,
    add_comment,
    delete_one_book,
)

app = Flask("app", static_folder="public", template_folder="views")

with app.app_context():
    init_db()


@app.route("/")
def index():
    return render_template("index.html")


app.add_url_rule("/api/books", view_func=get_all_books, methods=["GET"])
app.add_url_rule("/api/books", view_func=add_new_book, methods=["POST"])
app.add_url_rule("/api/books", view_func=delete_all_books, methods=["DELETE"])
app.add_url_rule("/api/books/<book_id>", view_func=get_one_book, methods=["GET"])
app.add_url_rule("/api/books/<book_id>", view_func=add_comment, methods=["POST"])
app.add_url_rule("/api/books/<book_id>", view_func=delete_one_book, methods=["DELETE"])


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
