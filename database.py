from flask import g
import sqlite3

DATABASE = "library.db"


def dict_factory(cursor, row):
    """
    Turns rows into dictionaries for easier JSON conversion. Plugs into
    Connection.row_factory.
    """
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = dict_factory
    db.execute("PRAGMA foreign_keys = ON")
    db.commit()
    return db


def init_db():
    db = get_db()
    c = db.cursor()
    c.executescript(
        """
        CREATE TABLE IF NOT EXISTS book(
            _id TEXT PRIMARY KEY, title TEXT NOT NULL
        ) WITHOUT ROWID;
        CREATE INDEX IF NOT EXISTS alphabetical ON book(title);

        CREATE TABLE IF NOT EXISTS comment(
            book_id TEXT REFERENCES book(_id) ON DELETE CASCADE, text TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS book_id ON comment(book_id)
        """
    )
    db.commit()
