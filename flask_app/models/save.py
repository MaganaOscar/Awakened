from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Save:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.items = data['items']
        self.current_location = data['current_location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(self, data):
        query = "INSERT INTO saves (user_id, items, current_location, created_at, updated_at " \
            "VALUES ( %(user_id)s, %(items)s, %(current_location)s, NOW(), NOW() )"
        return connectToMySQL("awakened_schema").query_db(query, data)
    
    @classmethod
    def add_visited(self, data):
        query = "INSERT INTO rooms_visited (save_id, room_id) VALUES ( %(save_id)s, %(room_id)s, NOW() )"
        return connectToMySQL("awakened_schema").query_db(query, data)
    
    @classmethod
    def get_save(self, data):
        query = "SELECT * FROM saves WHERE user_id = %(user_id)s"
        results = connectToMySQL("awakened_schema").query_db(query, data)