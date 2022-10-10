""" imports """
from http import client
from twister import app 
import pymongo
from flask import Flask
from pymongo import MongoClient
# from twister.create_db import *

if __name__ == "__main__":
    # print('welcome to mongodb')
    # print(client)
    app.run(host='0.0.0.0', port=5000,debug=True)
   

# app = Flask(__name__)

# client = MongoClient('localhost', 27017)

# db = client.flask_db
# todos = db.todos


# how to connect multiple databases in flask ?
# SQLALCHEMY_DATABASE_URI = 'postgres://localhost/main'
# SQLALCHEMY_BINDS = {
#     'users':        'mysqldb://localhost/users',
#     'appmeta':      'sqlite:////path/to/appmeta.db'
# }









