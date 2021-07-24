from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import date, datetime

class Save:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.items = data['items']
        self.current_location = data['current_location']
        self.play_time = data['play_time']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        data['created_at'] = datetime.now()
        data['updated_at'] = datetime.now()
        query = "INSERT INTO saves (user_id, name, items, play_time, current_location, created_at, updated_at) " \
            "VALUES ( %(user_id)s, %(name)s, %(items)s, %(play_time)s, %(current_location)s, %(created_at)s, %(updated_at)s );"
        return connectToMySQL("awakened_schema").query_db(query, data)
    
    @classmethod
    def add_visited(cls, data):
        query = "INSERT INTO rooms_visited (save_id, room_id) VALUES ( %(save_id)s, %(room_id)s );"
        return connectToMySQL("awakened_schema").query_db(query, data)
    
    @classmethod
    def get_saves(cls, data):
        query = "SELECT * FROM saves WHERE user_id = %(user_id)s"
        results = connectToMySQL("awakened_schema").query_db(query, data)
        saves = []
        if len(results) > 0:
            for result in results:
                saves.append(cls(result))
        return saves
    
    @classmethod
    def get_save(cls, data):
        query = "SELECT * FROM saves WHERE id = %(id)s;"
        result = connectToMySQL("awakened_schema").query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_save_location(cls, data):
        query = "SELECT current_location FROM saves WHERE id = %(id)s;"
        result = connectToMySQL("awakened_schema").query_db(query, data)
        return result[0]['current_location']

    @classmethod
    def update_play_time(cls, data):
        data['updated_at'] = datetime.now()
        query = "UPDATE saves SET play_time = ADDTIME(play_time, '00:00:01'), updated_at = %(updated_at)s WHERE id = %(id)s;"
        connectToMySQL("awakened_schema").query_db(query, data)

    @classmethod
    def delete_save(cls, data):
        query = "DELETE FROM saves WHERE id = %(id)s;"
        connectToMySQL("awakened_schema").query_db(query, data)