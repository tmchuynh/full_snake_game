from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.user_model import User


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/button', methods=['POST'])
def create_new_user():
    username = request.form.get('username')
    saveScore = request.form.get('saveScore')
    if saveScore:
        return f'The username submitted was: {username}'
    return 'Username was not valid'


if __name__ == '__main__':
    app.run(debug=True)
