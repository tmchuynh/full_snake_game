from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

class User:
    def __init__(self, data):
          self.id = data['id']
          self.username = data['username']
          self.date_creaed = data['date_creaed']
          self.date_updated = data['date_updated']