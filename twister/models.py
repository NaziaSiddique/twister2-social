from twister import db, bcrypt
from datetime import datetime
from flask_login import LoginManager, login_user, logout_user, current_user, login_required, UserMixin


# MODELS
class User(db.Model, UserMixin):
    def __init__(self, id, name,username, email, password, image_file):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.image_file = image_file

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    def __init__(self, id, date_posted, content, user_id, post_image):
        self.id = id
        self.date_posted = date_posted
        self.content = content
        self.user_id = user_id
        self.post_image = post_image

    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)
    post_image = db.Column(db.String(20), nullable=False, default='default.jpg')
    def __repr__(self):
        return f"Post('{self.date_posted}', '{self.content}', '{self.user_id}', '{self.post_image}')"

class Comment(db.Model):
    def __init__(self, id, date_posted, content, user_id, post_id):
        self.id = id
        self.date_posted = date_posted
        self.content = content
        self.user_id = user_id
        self.post_id = post_id
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    def __repr__(self):
        return f"Comment('{self.date_posted}', '{self.content}')"

class Follow(db.Model):
    def __init__(self, id, user_id, follower_id):
        self.id = id
        self.user_id = user_id
        self.follower_id = follower_id
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Follow('{self.user_id}', '{self.follower_id}')"

class Like(db.Model):
    def __init__(self, id, user_id, post_id):
        self.id = id
        self.user_id = user_id
        self.post_id = post_id
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    def __repr__(self):
        return f"Like('{self.user_id}', '{self.post_id}')"

class Dislike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    def __repr__(self):
        return f"Dislike('{self.user_id}', '{self.post_id}')"

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    def __repr__(self):
        return f"Report('{self.user_id}', '{self.post_id}')"

class Retweet(db.Model):
    def __init__(self, id, user_id, post_id):
        self.id = id
        self.user_id = user_id
        self.post_id = post_id
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    original_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    def __repr__(self):
        return f"Retweet('{self.user_id}', '{self.post_id}')"
