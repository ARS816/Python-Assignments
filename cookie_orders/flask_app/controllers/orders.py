from flask import render_template, request, redirect

from flask_app.models.order import Order

from flask_app import app

@app.route('/')
def index():
    return redirect('/orders')

@app.route('/orders')
def users():
    return render_template("all_orders.html", orders = Order.get_all())

@app.route('/orders/new')
def create():
    return render_template("new_orders.html")

@app.route('/orders/add', methods=['POST'])
def new():
    if not Order.validate_order(request.form):
        return redirect('/orders/new')
    Order.save(request.form)
    return redirect('/orders')

@app.route('/orders/edit/<int:id>')
def get_one(id):
    data = { "id":(id)}
    return render_template("update_order.html", order = Order.get_one(data))

@app.route('/orders/update', methods=['POST'])
def update_order():
    print(request.form['id'])
    if not Order.validate_order(request.form):
        return redirect('/orders/edit/'+ request.form['id'])
    Order.update(request.form)
    return redirect('/')

