from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users'
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def save(cls, data):
            query = "INSERT INTO users (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
            result = connectToMySQL('books_schema').query_db(query,data)
            return result