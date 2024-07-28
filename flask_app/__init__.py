# __init__.py
from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template('index.html')


app.secret_key = "randomly the kids decided that chasing the snakes would be a lot of fun"
DATABASE = "snake_game"
