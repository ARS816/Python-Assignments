from flask import render_template, request, redirect

from flask_app.models.dojo import Dojo

from flask_app.models.ninja import Ninja

from flask_app import app

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template("new_dojo.html", dojos= Dojo.get_all())

@app.route('/dojos/add', methods=['POST'])
def new():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show(id):
    data = {"id":id}
    return render_template("dojo_show.html", dojo = Dojo.get_ninjas(data))

