from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, current_user, login_required, UserMixin

import pymongo
import twister.env as env
mongo_client  = pymongo.MongoClient("mongodb://localhost:27017/") # create a mongo client
mongo_db = mongo_client["POSTS"] # create a database

# DATABASE CONFIGURATION
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = env.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = env.SECRET_KEY   # SECRET_KEY is a random string used to encrypt the session cookie
app.config['UPLOAD_FOLDER'] = env.UPLOAD_FOLDER
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# STATIC FOLDER
app.static_folder = 'static'
# UPLOAD FOLDER
app.config['UPLOAD_FOLDER'] = env.UPLOAD_FOLDER

# imports routes from twisker app
from twister import routes  # noqa
