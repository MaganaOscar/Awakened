from flask_app.config.mysqlconnection import connectToMySQL

class Room:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']

    @classmethod
    def get_room(cls, data):
        query = "SELECT * FROM rooms WHERE id = %(id)s;"
        result = connectToMySQL("awakened_schema").query_db(query, data)
        return cls(result[0])