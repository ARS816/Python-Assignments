from flask import render_template, request, redirect

from flask_app.models.user import User

from flask_app import apps

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("allusers.html", users= User.get_all())

@app.route('/new')
def create():
    return render_template("create.html")

@app.route('/add', methods=['POST'])
def new():
    User.save(request.form)
    return redirect('/users')

@app.route('/edit/<int:id>')
def get_one(id):
    data = { "id":(id)}
    return render_template("edit_user.html", user= User.get_one(data))

@app.route('/delete/<int:id>')
def delete(id):
    data = {"id":id}
    User.delete_user(data)
    return redirect('/users')

@app.route('/show/<int:id>')
def show(id):
    data = { "id":(id)}
    return render_template("show_user.html", user= User.get_one(data))

@app.route('/update', methods=['POST'])
def updat():
    User.update(request.form)
    return redirect('users')