from twister.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from flask_bcrypt import Bcrypt 
from datetime import datetime
import os
import pymongo

# Create a mongo database and a collection
client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = client["POSTS"]  # create a database
post_collection = mongo_db["posts"]  # create a collection



# delete"twitter.db" if it exists
if os.path.exists("twitter.db"):
    os.remove("twitter.db")

# create a db file
with open("twitter.db", "w") as f:
    f.write("")
    
# create tables in 'twitter.db'
engine = create_engine('sqlite:///twitter.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


# delete all tables if they exist
try:
    session.query(User).delete()
    session.query(Post).delete()
    session.query(Comment).delete()
    session.query(Follow).delete()
    session.query(Like).delete()
    session.commit()
except:
    pass
# create tables in 'twitter.db' based on models.py
db.create_all()

# create users
'''
user : id, name, username, email, password_encrypted, image_file
post : id, date_posted, content, user_id, post_image

1,Helen Brown,@helen.brown, helen.brown@gmail.com,drago,user1.jpg
1,22/01/2022,Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Voluptates et voluptatibus vel tenetur quos, id omnis sed error
                fuga necessitatibus.,1,post-img-1.jpg

2,Jane Doe,@jane.doe,jane.doe@gmail.com,drago,user2.jpg
2,22/01/2022,Lorem ipsum dolor sit amet, consectetur adipisicing elit.,2,post-img-2.jpg

3,John Thompson,@john.thompson,john.thompson@gmail.com,drago,user3.jpg
3,22/01/2022,Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Voluptates et voluptatibus vel tenetur quos, id omnis sed error
                fuga necessitatibus.,3,post-img-3.jpg

4,James Dias,@james.dias,james.dias@gmail.com,drago,user4.jpg
4,22/01/2022,Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Voluptates et voluptatibus vel tenetur quos, id omnis sed error
                fuga necessitatibus.,4,post-img-4.jpg

5,Nick Johnson,@nick.johnson,nick.johnson@gmail.vom,drago,user5.jpg
5,22/01/2022,Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Voluptates et voluptatibus vel tenetur quos, id omnis sed error
                fuga necessitatibus.,5,-

6,Ann Smith,@ann.smith,ann.smith@gmail.com,drago,user6.jpg
6,22/01/2022,Lorem ipsum dolor sit amet, consectetur adipisicing elit.
                Voluptates et voluptatibus vel tenetur quos, id omnis sed error
                fuga necessitatibus.,6,post-img-6.jpg
'''

users = """
1,Helen Brown,@helen.brown, helen.brown@gmail.com,drago,user1.jpg
2,Jane Doe,@jane.doe,jane.doe@gmail.com,drago,user2.jpg
3,John Thompson,@john.thompson,john.thompson@gmail.com,drago,user3.jpg
4,James Dias,@james.dias,james.dias@gmail.com,drago,user4.jpg
5,Nick Johnson,@nick.johnson,nick.johnson@gmail.vom,drago,user5.jpg
6,Ann Smith,@ann.smith,ann.smith@gmail.com,drago,user6.jpg
"""

posts  = """
1,22/01/2022,Lorem ipsum dolor sit amet consectetur adipisicing elit.Voluptates et voluptatibus vel tenetur quos id omnis sed errorfuga necessitatibus.,1,post-img-1.jpg
2,22/01/2022,Lorem ipsum dolor sit amet consectetur adipisicing elit.Voluptates et voluptatibus vel tenetur quos id omnis sed errorfuga necessitatibus.,2,post-img-2.jpg
3,22/01/2022,Lorem ipsum dolor sit amet consectetur adipisicing elit.Voluptates et voluptatibus vel tenetur quos id omnis sed errorfuga necessitatibus.,3,post-img-3.jpg
4,22/01/2022,Lorem ipsum dolor sit amet consectetur adipisicing elit.Voluptates et voluptatibus vel tenetur quos id omnis sed errorfuga necessitatibus.,4,post-img-4.jpg
5,22/01/2022,Lorem ipsum dolor sit amet consectetur adipisicing elit.Voluptates et voluptatibus vel tenetur quos id omnis sed errorfuga necessitatibus.,5,-
6,22/01/2022,Lorem ipsum dolor sit amet consectetur adipisicing elit.Voluptates et voluptatibus vel tenetur quos id omnis sed errorfuga necessitatibus.,6,-
"""

# user : id, name, username, email, password_encrypted, image_file
# post : id, date_posted, content, user_id, post_image
for user in users.split('\n'):
    user = user.split(',')
    if user[0] == '':
        continue
    user_id = int(user[0])
    name = user[1]
    username = user[2]
    email = user[3]
    password = user[4]
    encrypted_password = Bcrypt().generate_password_hash(password).decode('utf-8')
    image_file = user[5]
    user = User(id=user_id, name=name, username=username, email=email, password=encrypted_password, image_file=image_file)
    session.add(user)
    session.commit()

for post in posts.split('\n'):
    post = post.split(',')
    if post[0] == '':
        continue
    post_id = int(post[0])
    date_posted = post[1]
    # convert to datetime
    date_posted  = datetime.strptime(date_posted, '%d/%m/%Y')
    content = post[2]
    user_id = int(post[3])
    post_image = post[4]
    post = Post(id=post_id, date_posted=date_posted, content=content, user_id=user_id, post_image=post_image)
    session.add(post)
    session.commit()

    # committ to mongoDB
    post = {
        'id': post_id,
        'date_posted': date_posted,
        'content': content,
        'user_id': user_id,
        'post_image': post_image
    }
    mongo_db.posts.insert_one(post)   # insert_one()

