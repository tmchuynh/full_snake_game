from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

from flask_app.models import highScore_model

import re


class User:
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.date_creaed = data['date_creaed']
        self.date_updated = data['date_updated']

    def create_new_user(cls, data):
        query = "INSERT INTO user (username) VALUES (%(username)s)"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    def get_all_users(cls):
        query = "SELECT * FROM user"
        results = connectToMySQL(DATABASE).query_db(query)
        list_users = []
        for result in results:
            list_users.append(cls(result))
        return list_users

    def get_highScore_by_user(cls, data):
        query = """SELECT * FROM user
            LEFT JOIN high_score ON high_score.user_id = %(user_id)s"""

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
        highScore_model.delete_highScore(data)
        return cls(results)
    
    @classmethod
    def check_database(cls, data):
        query = "SELECT * FROM user WHERE username = %(username)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) == 0:
            return False
        return True
    
    @staticmethod
    def validate_username(data):
        # Search for special characters in a string
        regex = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')

        is_valid = True

        # Ensure 'username' key is in the data dictionary and check length and special characters
        if 'username' not in data:
            return False  

        username = data['username']

        # Check for special characters
        if regex.search(username):
            is_valid = False

        # Check if the username is too short
        if len(username) < 5:
            is_valid = False

        # Check if the username already exists in the database
        this_user = {
            'username': data['username']
        }
        
        results = User.check_database(this_user)

        if results:
            is_valid = False

        return is_valid
