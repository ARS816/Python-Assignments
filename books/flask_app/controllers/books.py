from flask import render_template, request, redirect

from flask_app.models.book import Book

from flask_app import app

@app.route('/books')
def all_books():
    return render_template("books.html", books= Book.get_all())

@app.route('/books/add', methods=['POST'])
def add_book():
    Book.save(request.form)
    return redirect('/books')