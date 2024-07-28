from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.highScore_model import HighScore