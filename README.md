# Python personal library microservice

[![Run on Repl.it](https://repl.it/badge/github/tywmick/library-python)](https://repl.it/github/tywmick/library-python)

This is a Python port of my [Node.js personal library microservice](https://ty-library.glitch.me/), built with [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [SQLite](https://sqlite.org/index.html). The front end API tests on the home page also use [Bootstrap](https://getbootstrap.com/), [jQuery](https://jquery.com/), and [highlight.js](https://highlightjs.org/). The API fulfills the following user stories:

1. I can **post** a `title` to `/api/books` to add a book and returned will be the object with the `title` and a unique `_id`.
2. I can **get** `/api/books` to retrieve an aray of all books containing `title`, `_id`, & `commentcount`.
3. I can **get** `/api/books/{_id}` to retrieve a single object of a book containing `title`, `_id`, & an array of `comments` (empty array if no comments present).
4. I can **post** a `comment` to `/api/books/{_id}` to add a comment to a book and returned will be the books object similar to **get** `/api/books/{_id}`.
5. I can **delete** `/api/books/{_id}` to delete a book from the collection. Returned will be `"delete successful"` if successful.
6. If I try to request a book that doesn't exist I will get a `"no book exists"` message.
7. I can send a **delete** request to `/api/books` to delete all books in the database. Returned will be `"complete delete successful"` if successful.
