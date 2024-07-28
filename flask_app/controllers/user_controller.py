from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.user_model import User


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/{id}', methods=['POST'])
def create_new_user():
    button_value = request.form.get('button')
    if button_value:
        return f'Button was clicked with value: {button_value}'
    return 'Button was not clicked'
