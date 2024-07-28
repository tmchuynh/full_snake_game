from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.user_model import User


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/button', methods=['POST'])
def create_new_user():
    button_value = request.form.get('randomButton')
    if button_value:
        return f'Save score button was clicked with value: {button_value}'
    return 'Save score button was not clicked'


if __name__ == '__main__':
    app.run(debug=True)
