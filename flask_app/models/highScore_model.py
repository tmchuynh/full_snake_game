from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

from flask_app.models.user_model import User

class HighScore:
    def __init__(self, data):
        self.id = data['id']
        self.high_score = data['high_score']
        self.difficulty = data['difficulty']
        self.obstacles = data['obstacles']
        self.obstaclesMove = data['obstaclesMove']
        self.peacefulMode = data['peacefulMode']
        self.user_id = data['user_id']
        self.date_created = data['date_created']
        self.date_updated = data['date_updated']
        self.user = None

    @classmethod
    def get_all_highScores(cls):
        query = """SELECT high_score.*, user.* FROM high_score 
        LEFT JOIN user ON user.id = high_score.user_id
        ORDER BY user.username ASC, high_score.high_score DESC"""
        results = connectToMySQL(DATABASE).query_db(query)
        print("Query Results:", results)
        list_highScores = []
        for result in results:
            high_score = cls(result)
            high_score.user = User(result)
            list_highScores.append(high_score)
        return list_highScores

    @classmethod
    def get_highScore_by_user(cls, data):
        query = "SELECT * FROM high_score WHERE user_id = %(user_id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return None
        return cls(results[0])

    @classmethod
    def get_highScore_by_difficulty(cls, data):
        query = "SELECT * FROM high_score WHERE difficulty = '%(difficulty)s'"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return None
        list_of_users = []
        for result in results:
            list_of_users.append(cls(result))
        return list_of_users
    
    @classmethod
    def delete_highScore(cls, data):
        query = "DELETE FROM high_score WHERE user_id = %(user_id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results)
    
    @classmethod
    def get_highScore_by_user_obstacles(cls, data):
        query = "SELECT * FROM high_score WHERE user_id = %(user_id)s AND obstacles = %(obstacles)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
    @classmethod
    def get_highScore_by_user_obstacles_and_peacefulMode(cls, data):
        query = "SELECT * FROM high_score WHERE user_id = %(user_id)s AND obstacles = %(obstacles)s AND %(peacefulMode)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
    @classmethod
    def check_existing_score(cls, data):
        query = """SELECT * FROM high_score WHERE user_id = %(user_id)s
        AND difficulty = '%(difficulty)s'
        AND obstacles = %(obstacles)s
        AND high_score = %(high_score)s
        AND obstaclesMove = %(obstaclesMove)s
        AND peacefulMode = %(peacefulMode)s"""
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) == 0:
            # exact high score doesn't exist
            return False
        if (HighScore.get_highScore_by_user_obstacles(data)):
            # If the user already has a high score with this many obstacles
            HighScore.update_obstacles_highScore(data)
            return False
        return True
    
    @classmethod
    def create_new_highScore(cls, data):
        check = HighScore.check_existing_score(data)
        if check:
            return None
        query = """INSERT INTO high_score (difficulty, obstacles, obstaclesMove, peacefulMode, high_score) 
        VALUES ('%(difficulty)s', %(obstacles)s, %(obstaclesMove)s, %(peacefulMode)s, %(high_score)s) WHERE user_id = %(user_id)s"""
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
    @classmethod
    def update_highScore(cls, data):
        query = """
        UPDATE high_score SET difficulty = '%(difficulty)s', obstacles = %(obstacles)s, obstaclesMove = %(obstaclesMove)s,
        peacefulMode = %(peacefulMode)s, high_score = %(high_score)s WHERE user_id = %(user_id)s"""
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
    @classmethod
    def update_obstacles_highScore(cls, data):
        query = """
        UPDATE high_score SET difficulty = '%(difficulty)s', obstaclesMove = %(obstaclesMove)s,
        peacefulMode = %(peacefulMode)s, high_score = %(high_score)s WHERE user_id = %(user_id)s AND obstacles = %(obstacles)s"""
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results