from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Order:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cookie = data['cookie']
        self.boxes = data['boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders;"
        results = connectToMySQL('cookies_schema').query_db(query)
        orders = []
        for order in results:
            orders.append( cls(order) )
        return orders
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO orders (name, cookie , boxes) VALUES (%(name)s,%(cookie)s,%(boxes)s);"
        result = connectToMySQL('cookies_schema').query_db(query,data)
        return result

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM orders WHERE id = %(id)s;"
        results = connectToMySQL('cookies_schema').query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        query = "UPDATE orders SET name = %(name)s, cookie = %(cookie)s, boxes = %(boxes)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('cookies_schema').query_db(query,data)
    
    @staticmethod
    def validate_order(order):
        is_valid = True
        if len(order['name']) < 2:
            flash("Name cannot be blank")
            is_valid = False
        if len(order['cookie']) < 2:
            flash("Please input cookie type.")
            is_valid = False
        if not order['boxes'] or int(order['boxes']) < 1: 
            flash("Please add quanity")
            is_valid = False
        return is_valid