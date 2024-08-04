from flask import Flask, flash, render_template, request, redirect, session
from flask_app import app
from flask_app.models.user_model import User


@app.route('/')
def index():
    return render_template('opening.html')

@app.route('/snake_game')
def new_game():
    return render_template('index.html')


@app.route('/new_user', methods=['POST'])
def create_new_user():
    username = request.form.get('username')
    noButton = request.form.get('noButton')
    new_user = {
        'username': request.form['username'].capitalize()
    }
    if noButton:
        return f'no thanks button clicked'
    if not User.validate_username(new_user):
        flash("Usernames cannot contain special characters and cannot be less than 5 characters in length", "registration_failure")
        return redirect('/')
    if not User.check_database(new_user):
        flash("The username " + username + " already exists.", "registration_failure")
        return redirect('/')
    
    User.create_new_user(new_user)
    return redirect('/snake_game')


if __name__ == '__main__':
    app.run(debug=True)
