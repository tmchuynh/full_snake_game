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