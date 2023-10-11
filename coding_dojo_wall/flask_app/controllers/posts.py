from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.post import Post
from flask_app.models.user import User

@app.route('/new_post', methods=["POST"])
def new_post():
    if not Post.validate_post(request.form):
        return redirect ('/wall')
    Post.save(request.form)
    return redirect('/wall')

@app.route("/delete/<id>")
def delete_post(id):
    Post.delete(id)
    return redirect("/wall")