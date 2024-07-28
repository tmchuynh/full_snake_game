# __init__.py
from flask import Flask
app = Flask(__name__)
app.secret_key = "randomly the kids decided that chasing the snakes would be a lot of fun"
DATABASE = "snake_game"