from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

from flask_app.models import highScore_model


class User:
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.date_creaed = data['date_creaed']
        self.date_updated = data['date_updated']

    def get_all_users(cls):
        query = "SELECT * FROM user"
        results = connectToMySQL(DATABASE).query_db(query)
        list_users = []
        for result in results:
            list_users.append(cls(result))
        return list_users

    def get_user_by_id(cls, data):
        query = "SELECT * FROM user WHERE id = %(user_id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return None
        return cls(results[0])

    def get_highScore_by_user(cls, data):
        query = """SELECT * FROM user
            LEFT JOIN high_score ON high_score.user_id = user.id"""

        results = connectToMySQL(DATABASE).query_db(query, data)

        if results:
            user = cls(results[0])
            user.highScore = []

            for result in results:
                highScore = {
                    'id': result['id'],
                    'difficulty': result['difficulty'],
                    'obstacles': result['obstacles'],
                    'obstaclesMove': result['obstaclesMove'],
                    'peacefulMode': result['peacefulMode'],
                    'date_created': result['date_created'],
                    'date_updated': result['date_updated']
                }
                user.highScore.append(highScore_model.HighScore(highScore))
            return user
        return []

    def delete_user(cls, data):
        query = "DELETE FROM user WHERE id = %(user_id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results)
