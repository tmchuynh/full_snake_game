from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.user_model import User


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/new_user', methods=['POST'])
def create_new_user():
    username = request.form.get('username')
    if not User.validate_username(request.form):
        return redirect('/')
    
    new_user = {
        'username': request.form['username'].capitalize()
    }

    User.create_new_user(new_user)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
