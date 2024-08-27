from flask import render_template, request, redirect, session, flash

from flask_app.models.user import User

from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/login', methods=['GET'])
def login():
    user = User.get_by_email(request.form)
    if not user: 
        flash('Invalid Email', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid Password', 'login')
        return redirect('/')
    session['user_id']= user.id
    return redirect('/profile')

@app.route('/register', methods=['POST'])
def new():
    if not User.validate_user(request.form):
        return redirect('/')
    data ={
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user.id']= id
    return redirect('/profile')

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {'id': session['user_id']}
    return render_template('profile.html', user = User.get_one(data))

@app.route('logout')
def logout():
    session.clear()
    return redirect('/')