from mysqlconnection import connectToMySQL

from flask import flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM orders WHERE id = %(id)s;"
        results = connectToMySQL('users_schema').query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
        result = connectToMySQL('users_schema').query_db(query,data)
        return result
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectoMySQL(cls.db).query_db(query, data)
        if len(results)<1:
            return False
        return cls(results[0])
    
    @staticmethod
    def validate_user(user):
        is_valid = True 
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db) .query_db(query, user)
        if len(results) >= 1:
            flash("Email already in use." , "register")
            is_valid=False
        if len(user['first_name']) < 1:
            flash("First name cannot be blank.","register")
            is_valid = False
        if len(user['last_name']) < 1:
            flash("Last name cannot be blank.","register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address.","register")
            is_valid = False
        if len(user['password']) <8:
            flash("Password must be at least 8 characters","register")
            is_valid = False
        if user['password']!= user['confirm']:
            flash("Passwords do not match","register")
        return is_valid
    