from flask import render_template, request, redirect

from flask_app.models.author import Author

from flask_app import app

@app.route('/')
def authors():
    return redirect('/authors')

@app.route('/authors')
def all_authors():
    return render_template("authors.html", authors= Author.get_all())

@app.route('/authors/add', methods=['POST'])
def add_author():
    Author.save(request.form)
    return redirect('/authors')