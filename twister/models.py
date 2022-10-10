from twister import db, bcrypt
from datetime import datetime
from flask_login import LoginManager, login_user, logout_user, current_user, login_required, UserMixin


# MODELS
class User(db.Model, UserMixin):
    def __init__(self, id, name,username, email, password, image_file, is_business):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.image_file = image_file
        self.is_business = is_business  

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    username = db.Column(db.String(200), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    image_file = db.Column(db.String(200), nullable=False, default='default.jpg')
    is_business = db.Column(db.Boolean, nullable=False)

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

class Business_Profile(db.Model):   
    def __init__(self, id,user_id, name,logo,address,url,social_url, contact_number ):
        self.id = id
        self.user_id = user_id
        self.logo = logo
        self.name = name
        self.address =address
        self.url = url
        self.social_url = social_url
        self.contact_number = contact_number
        # self.password = password

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    logo =db.Column(db.String(500), nullable=False, default='default.jpg')
    name = db.Column(db.String(200), unique=True, nullable=False)
    address = db.Column(db.String(200), unique=True, nullable=False)
    url = db.Column(db.String(200), nullable=False)
    social_url = db.Column(db.String(200), nullable=False)
    contact_number = db.Column(db.Integer(), nullable = False)
    # password = db.Column(db.String(20), nullable=False)

class Consumer(db.Model):   
    def __init__(self, id,user_id,profilepic,address,contact_number ):
        self.id = id
        self.user_id = user_id
        self.profilepic = profilepic
        self.address =address
        self.contact_number = contact_number
        # self.password = password

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    profilepic =db.Column(db.String(500), nullable=False, default='default.jpg')
    address = db.Column(db.String(200), unique=True, nullable=False)
    contact_number = db.Column(db.Integer(), nullable = False)
    # password = db.Column(db.String(20), nullable=False)
# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     bussiness_profile_id=db.Column(db.Integer, db.ForeignKey('business__profile.id'), nullable=False)
#     name=db.Column(db.String(20), nullable=False)
#     img=db.Column(db.String(20), nullable=False, default='default.jpg')
#     descriptions=db.Column(db.String(250), nullable=False)

#     # Column('person_id', Integer, ForeignKey(tbl_person.c.id), primary_key=True)
#     # # business_profile
