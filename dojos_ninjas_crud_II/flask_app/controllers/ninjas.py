from flask import render_template, redirect, request

from flask_app import app 

from flask_app.models.dojo import Dojo

from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def ninjas():
    return render_template("add_ninja.html", dojos= Dojo.get_all())

@app.route('/ninjas/add', methods=['POST'])
def add_ninja():
    Ninja.save(request.form)
    return redirect('/dojos')

@app.route('/delete/<int:id>')
def delete(id):
    data = {"id":id}
    Ninja.delete_ninja(data)
    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):
    data = { "id":(id)}
    return render_template("edit_ninja.html", ninja = Ninja.get_one(data))

@app.route('/update', methods=['POST'])
def update():
    Ninja.update(request.form)
    return redirect('/')