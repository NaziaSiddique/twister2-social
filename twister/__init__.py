from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, current_user, login_required, UserMixin
from flask_pymongo import PyMongo
import pymongo
import twister.env as env
import os

try:
    mongo_db = pymongo.MongoClient("mongodb://root:root123@ac-9gdfpwp-shard-00-00.jnkaoxm.mongodb.net:27017,ac-9gdfpwp-shard-00-01.jnkaoxm.mongodb.net:27017,ac-9gdfpwp-shard-00-02.jnkaoxm.mongodb.net:27017/?ssl=true&replicaSet=atlas-31uc1c-shard-0&authSource=admin&retryWrites=true&w=majority")  # create a database
    posts = mongo_db.db.posts
    product = mongo_db.db.product
    comment = mongo_db.db.comment
    like = mongo_db.db.like
    # product.delete_many({'name':'hello'})
except Exception as e:
    print(e)# 


# DATABASE CONFIGURATION
app = Flask(__name__)
# app.config['MONGO_URI'] = "mongodb://" + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27018/' + os.environ['MONGODB_DATABASE']
# mongo = PyMongo(app)
# print(mongo)
# mongo.db.product.insert_one({'name':'hello'})
# mongo.db.posts.insert_one({'name':'hello'})
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
 # noqa
from twister import routes