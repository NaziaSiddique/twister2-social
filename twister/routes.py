import os
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import flask
from werkzeug.utils import secure_filename
import sys
from twister import app, db, mongo_db,login_manager,bcrypt
from twister.models import *

# USER LOADER
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ROUTES
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('subpages/about.html', title='About')

@app.route('/help')
def help():
    return render_template('subpages/help.html', title='Help')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        print(username, email, password, confirm_password,file=sys.stdout)
        if not username or not email or not password or not confirm_password:
            flash('Please fill in all fields', 'danger')
        elif password != confirm_password:
            flash('Passwords do not match', 'danger')
        else:
            print("hello world",file=sys.stdout)
            user = User.query.filter_by(email=email).first()
            if user:
                flash('Email already exists', 'danger')
            else:
                id = User.query.count() + 1
                image_file = 'default.jpg'
                password_encrypted = bcrypt.generate_password_hash(password).decode('utf-8')
                user = User(id, name,username, email, password_encrypted, image_file)
                db.session.add(user)
                db.session.commit()
                flash('You are now registered and can log in', 'success')
                return redirect(url_for('login'))
    return render_template('register.html', title='Register')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('posts'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        print(user,file=sys.stdout)
        if user and bcrypt.check_password_hash(user.password, password):
            ## goto posts page of user
            login_user(user)
            return redirect(url_for('posts'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

## Url for posts
@app.route('/posts', methods=['GET', 'POST'])
@login_required
def posts():
    if request.method == 'GET':
        # posts = Post.query.all()
        ## use mongodb to get all posts
        posts = mongo_db.posts.find()

        # jsonify
        posts_json = []
        for post in posts:
            id= post['id']
            content = post['content']
            date_posted = post['date_posted']
            user_id = post['user_id']
            user = User.query.filter_by(id=user_id).first()
            username = user.username
            name = user.name
            image_file = user.image_file
            post_image = post['post_image']
            # check the number of likes for this post
            likes = Like.query.filter_by(post_id=id).count()
            # all comments for this post
            comments = Comment.query.filter_by(post_id=id).all()        # jsonify
            comments_json = []
            for comment in comments:
                # id, date_posted, content, user_id, post_id
                id_comment = comment.id
                content_comment = comment.content
                date_posted_comment = comment.date_posted
                user_id_comment = comment.user_id
                post_id_comment = comment.post_id
                user_comment = User.query.filter_by(id=user_id_comment).first()
                username_comment = user_comment.username
                name_comment = user_comment.name
                image_file_comment = user_comment.image_file
                comment_json = {
                    "id": id_comment,
                    "content": content_comment,
                    "date_posted": date_posted_comment,
                    "user_id": user_id_comment,
                    "post_id": post_id_comment,
                    "username": username_comment,
                    "name": name_comment,
                    "image_file": image_file_comment
                }
                comments_json.append(comment_json)
                # sort comments by date_posted
                comment_json = sorted(comments_json, key=lambda k: k['date_posted'],reverse=True)


            to_post = {
                'id': id,
                'content': content,
                'date_posted': date_posted,
                'username': username,
                'name' : name,
                'likes': likes,
                'comments': comments_json,
                'post_image' : "./static/images/post_images/" + post_image,
                'image_file': "./static/images/user_images/" + image_file

            }
            posts_json.append(to_post)

        # sort descending by date_posted
        posts_json = sorted(posts_json, key=lambda k: k['date_posted'], reverse=True)

        ## following and followers
        following = []
        followers = []
        for follow in Follow.query.all():
            if follow.user_id == current_user.id:
                following.append(follow.follower_id)
            if follow.follower_id == current_user.id:
                followers.append(follow.user_id)
        return render_template('posts.html', title='Posts', followers=followers,following=following,\
            posts=posts_json,name=current_user.name,username = current_user.username,user_image = "./static/images/user_images/" + current_user.image_file)

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')

@app.route('/post_new', methods=['GET', 'POST'])
@login_required
def post_new():
    if request.method == 'POST':
        content = request.form['content']
        if content=="":
            flash('Please fill in all fields', 'danger')
            return redirect(url_for('posts'))
        try:
            post_image = request.files['post_image']
        except:
            post_image = None


        if post_image:
            filename = secure_filename(post_image.filename)
            post_image.save(os.path.join(app.config['UPLOAD_FOLDER'], 'post_images',filename))
            post_image = filename
        else:
            post_image = '-'
        # id, date_posted, content, user_id, post_image
        id = Post.query.count() + 1
        date_posted = datetime.now()
        user_id = current_user.id
        # post = Post(id, date_posted, content, user_id, post_image)
        ## use mongodb to insert new post
        # db.session.add(post)
        # db.session.commit()
        post = {
            'id': id,
            'date_posted': date_posted,
            'content': content,
            'user_id': user_id,
            'post_image': post_image
        }
        mongo_db.posts.insert_one(post)
        flash('Your post has been created!', 'success')
        return redirect(url_for('posts'))
    return render_template('posts.html', title='New Post')



@app.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user != current_user:
        flash('You cannot update this post', 'danger')
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_image = request.form.get('post_image')
        if not title or not content:
            flash('Please fill in all fields', 'danger')
        else:
            post.title = title
            post.content = content
            post.post_image = post_image
            # db.session.commit()
            # use monogodb to update post
            mongo_db.posts.update_one({"id": post_id}, {"$set": {"content": content, "title": title, "post_image": post_image}})

            flash('Your post has been updated', 'success')
            return redirect(url_for('post', post_id=post.id))
    return render_template('update_post.html', title='Update Post', post=post)

@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.user != current_user:
        flash('You cannot delete this post', 'danger')
    # db.session.delete(post)
    # db.session.commit()
    # use monogodb to delete post
    mongo_db.posts.delete_one({"id": post_id})
    flash('Your post has been deleted', 'success')
    return redirect(url_for('home'))

@app.route('/user/<string:username>')
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(user_id=user.id).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)

## LIKE,COMMENT,RETWEET
@app.route('/post/<int:post_id>/like', methods=['GET','POST'])
@login_required
def like_post(post_id):
    if request.method == 'GET':
        post = Post.query.get_or_404(post_id)
        if post.user_id != current_user.id:
            # check if already liked
            like = Like.query.filter_by(user_id=current_user.id, post_id=post_id).first()
            print(like,file=sys.stdout)
            if not like:
                id = Like.query.count() + 1
                like = Like(id, current_user.id, post_id)
                db.session.add(like)
                db.session.commit()
                flash('You liked this post', 'success')
                return redirect(url_for('posts'))
            else:
                flash('You already liked this post', 'danger')
                print('You already liked this post',file =sys.stdout)
                return redirect(url_for('posts'))
        else:
            flash('You cannot like your own post', 'danger')
            print('You cannot like your own post',file =sys.stdout)
            return redirect(url_for('posts'))
    return redirect(url_for('posts'))

@app.route('/post/<int:post_id>/comment', methods=['GET','POST'])
@login_required
def comment_post(post_id):
    if request.method == 'POST':
        comment = request.form.get('comment')
        if not comment:
            flash('Please enter a comment', 'danger')
        else:
            # id, date_posted, content, user_id, post_id
            id = Comment.query.count() + 1
            date_posted = datetime.now()
            user_id = current_user.id
            comment = Comment(id, date_posted, comment, user_id, post_id)
            db.session.add(comment)
            db.session.commit()
            flash('Your comment has been posted', 'success')
            return redirect(url_for('posts'))
    return redirect(url_for('posts'))



# FOLLOW/UNFOLLOW
@app.route('/user/<string:to_follow_username>/follow', methods=['GET','POST'])
@login_required
def follow_user(to_follow_username):
    if flask.request.method == 'GET':
        print(to_follow_username,file=sys.stdout)
        user = User.query.filter_by(username=to_follow_username).first()
        if user is None:
            flash('User {} not found'.format(to_follow_username), 'danger')
            return redirect(url_for('posts'))
        if user == current_user:
            flash('You cannot follow yourself!', 'danger')
            return redirect(url_for('posts'))

        ## increase the id
        id = Follow.query.count() + 1
        ## id of the user to be followed
        user_id = user.id
        # if if already following
        if Follow.query.filter_by(user_id=user_id, follower_id=current_user.id).first():
            flash('You are already following {}'.format(to_follow_username), 'danger')
            print('You are already following {}'.format(to_follow_username), file=sys.stdout)
            return redirect(url_for('posts'))
        new_follow = Follow(id=id, user_id=user_id, follower_id=current_user.id)
        db.session.add(new_follow)
        db.session.commit()
        flash('You are following {}!'.format(to_follow_username), 'success')
        print('You are following {}!'.format(to_follow_username),file=sys.stdout)
        return redirect(url_for('posts'))
    else:
        return redirect(url_for('posts'))



@app.route('/user/<string:to_unfollow_username>/unfollow', methods=['GET','POST'])
@login_required
def unfollow_user(to_unfollow_username):
    if flask.request.method == 'GET':
        user = User.query.filter_by(username=to_unfollow_username).first()
        if user is None:
            flash('User {} not found'.format(to_unfollow_username), 'danger')
            return redirect(url_for('posts'))
        if user == current_user:
            flash('You cannot unfollow yourself!', 'danger')
            return redirect(url_for('posts'))
        follow = Follow.query.filter_by(user_id=user.id, follower_id=current_user.id).first()
        if follow is None:
            flash('You are not following {}'.format(to_unfollow_username), 'danger')
            return redirect(url_for('posts'))
        db.session.delete(follow)
        db.session.commit()
        flash('You are not following {}'.format(to_unfollow_username), 'success')
        return redirect(url_for('posts'))
    else:
        return redirect(url_for('posts'))
