from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,25}$")

class User:
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    #add user to database
    def create(cls, data):
        query = "INSERT INTO users (username, email, password, created_at, updated_at)" \
            "VALUES (%(username)s, %(email)s, %(password)s, NOW(), NOW() );"
        return connectToMySQL("awakened_schema").query_db(query, data)

    @classmethod
    def get_username(cls, data):
        query = "SELECT username FROM users WHERE id = %(id)s;"
        result = connectToMySQL("awakened_schema").query_db(query, data)
        if len(result) < 1:
            return False
        return result[0]
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("awakened_schema").query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def check_duplicate(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('awakened_schema').query_db(query, data)

        return True if len(result) > 0 else False
    
    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data['username']) < 2:
            flash("Username must be at least 2 characters long", "username")
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters long", "password")
            is_valid = False
        elif not PASS_REGEX.match(data['password']):
            flash("Password must have at least 1 uppercase letter, 1 lowercase letter, 1 number, and at least 1 special character", "password")
            is_valid = False
        if data['password'] != data['confirm_pass']:
            flash("Passwords must match", "confirm_pass")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Email is not valid!", "email")
            is_valid = False
        elif User.check_duplicate({'email': data['email']}):
            flash("A user with this email already exists. Please use another email.", "email")
            is_valid = False
        return is_valid