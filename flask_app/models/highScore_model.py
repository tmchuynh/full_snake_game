from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash


class HighScore:
    def __init__(self, data):
        self.id = data['id']
        self.difficulty = data['difficulty']
        self.obstacles = data['obstacles']
        self.obstaclesMove = data['obstaclesMove']
        self.peacefulMode = data['peacefulMode']
        self.user_id = data['user_id']
        self.date_created = data['date_created']
        self.date_updated = data['date_updated']

    def get_all_highScores(cls):
        query = "SELECT * FROM high_score"
        results = connectToMySQL(DATABASE).query_db(query)
        list_highScores = []
        for result in results:
            list_highScores.append(cls(result))
        return list_highScores

    def get_highScore_by_user(cls, data):
        query = "SELECT * FROM high_score WHERE user_id = %(user_id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return None
        return cls(results[0])

    def get_highScore_by_difficulty(cls, data):
        query = "SELECT * FROM high_score WHERE difficulty = %(difficulty)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return None
        list_of_users = []
        for result in results:
            list_of_users.append(cls(result))
        return list_of_users
