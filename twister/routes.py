import os
from xmlrpc.client import DateTime
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import flask
from werkzeug.utils import secure_filename
import sys
from twister import app, db, mongo_db, login_manager, bcrypt
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


@app.route('/message')
def message():
    return render_template('subpages/message.html', title='Message')


@app.route('/alerts')
def alerts():
    return render_template('subpages/alerts.html', title='Message')


@app.route('/analytics')
def analytics():
    return render_template('subpages/analytics.html', title='Message')


@app.route('/offer')
def offer():
    return render_template('subpages/offer.html', title='Message')


@app.route('/help')
def help():
    return render_template('subpages/help.html', title='Help')


@app.route('/contact')
def contact():
    return render_template('subpages/contact.html', title='Contact')


@app.route('/privacy_policy')
def privacy_policy():
    return render_template('subpages/privacy policy.html', title='Privacy Policy')


@app.route('/brand')
def brand():
    return render_template('subpages/brand.html', title='Brand')


@app.route('/developers')
def developers():
    return render_template('subpages/developers.html', title='Developers')


# for registration endpoint
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
        is_business = request.form.get('is_business')
        if "is_consumer" in is_business:
            is_business = False
        else:
            is_business = True

        if not username or not email or not password or not confirm_password:
            flash('Please fill in all fields', 'danger')
        elif password != confirm_password:
            flash('Passwords do not match', 'danger')
        else:
            user = User.query.filter((User.email==email) | (User.username==username)).first()
            if user:
                flash('Email or Username already exists', 'danger')
            else:
                id = User.query.count() + 1
                image_file = 'default.jpg'
                password_encrypted = bcrypt.generate_password_hash(password).decode('utf-8')
                user = User(id, name, username, email, password_encrypted, image_file, is_business)
                db.session.add(user)
                db.session.commit()
                flash('You are now registered and can log in', 'success')
                login_user(user)
                if is_business == True:
                    return redirect(url_for('business_profile'))
                else:
                    return redirect(url_for('consumer'))
    return render_template('register.html', title='Register')


# for login endpoint
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('posts'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        print(user, file=sys.stdout)
        if user and bcrypt.check_password_hash(user.password, password):
            ## goto posts page of user
            login_user(user)
            return redirect(url_for('posts'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login')


# for logout endpoint
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


## Url for posts
@app.route('/posts', methods=['GET', 'POST'])
@login_required
def posts():
    if request.method == 'GET':
        if current_user.is_business == True:
            current_userdata = Business_Profile.query.filter_by(user_id = current_user.id).first()
            # posts = Post.query.all()
            ## use mongodb to get all posts
            posts = mongo_db.db.posts.find()
            user = User.query.filter_by(email=current_user.email).first()
            users = User.query.filter(User.id != current_user.id).all()[:3]
            for userdata in users:
                if userdata.is_business == True:
                    datauser = Business_Profile.query.filter_by(user_id = userdata.id).first()
                    userdata.image_file = datauser.logo
                else:
                    datauser = Consumer.query.filter_by(user_id = userdata.id).first()
                    userdata.image_file = datauser.profilepic
            posts_json = []

            for post in posts:
                # if post is None:
                #     mongo_db.db.posts.insert_one(
                #         {'id': 1, 'user_id': 1, 'date_posted': datetime.now(), 'content': 'hello',
                #          'post_image': 'static/images/product_image/Screenshot_from_2022-09-12_10-10-55.png'})
                id = post['id']
                content = post['content']
                date_posted = post['date_posted']
                likes = mongo_db.db.like.find({'post_id':id})
                like = len(list(likes))
                time = datetime.now() - date_posted
                if time.days == 0:
                    post_times = time.total_seconds()
                    if post_times >= 60:
                        post_timem = post_times / 60
                        if post_timem >= 60:
                            post_timeh = post_timem / 60
                            post_time = f'{int(post_timeh)}h'
                        else:
                            post_time = f'{int(post_timem)}m'
                    else:
                        post_time = f'{int(post_times)}s'
                else:
                    post_time = f'{time.days}d'
                user_id = post['user_id']
                user = User.query.filter_by(id=user_id).first()
                userdata = Business_Profile.query.filter_by(user_id = user.id).first()
                username = user.username
                name = user.name
                image_file = userdata.logo
                post_image = post['post_image']
                likes = Like.query.filter_by(post_id=id).count()
                comments = mongo_db.db.comment.find({'post_id': id})  # jsonify
                comments_json = []
                for comment in comments:
                    # id, date_posted, content, user_id, post_id
                    id_comment = comment['id']
                    content_comment = comment['content']
                    date_posted_comment = comment['date_posted']
                    time = datetime.now() - date_posted_comment
                    if time.days == 0:
                        comment_times = time.total_seconds()
                        if comment_times >= 60:
                            comment_timem = comment_times / 60
                            if comment_timem >= 60:
                                comment_timeh = comment_timem / 60
                                comment_time = f'{int(comment_timeh)}h'
                            else:
                                comment_time = f'{int(comment_timem)}m'
                        else:
                            comment_time = f'{int(comment_times)}s'
                    else:
                        comment_time = f'{time.days}d'
                    user_id_comment = comment['user_id']
                    post_id_comment = comment['post_id']
                    comment_json = {
                        "id": id_comment,
                        "content": content_comment,
                        "date_posted": comment_time,
                        "user_id": user_id_comment,
                        "post_id": post_id_comment,
                    }
                    comments_json.append(comment_json)
                    # sort comments by date_posted
                    comment_json = sorted(comments_json, key=lambda k: k['date_posted'], reverse=True)

                to_post = {
                    'id': id,
                    'content': content,
                    'date_posted': post_time,
                    'username': username,
                    'name': name,
                    'likes': like,
                    'comments': comments_json,
                    'post_image': "./static/images/post_images/" + post_image,
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
        else:
            return redirect(url_for('postconsumer'))
        return render_template('posts.html', title='Posts', followers=followers, following=following, \
                               posts=posts_json, users=users, name=current_user.name, username=current_user.username,
                               user_image="./static/images/user_images/" + current_userdata.logo,like = like)


# for consumer registartion endpoint
@app.route('/postconsumer', methods=['GET', 'POST'])
@login_required
def postconsumer():
    if request.method == 'GET':
        current_userdata = Consumer.query.filter_by(user_id = current_user.id).first()
        # posts = Post.query.all()
        ## use mongodb to get all posts
        posts = mongo_db.db.posts.find()
        user = User.query.filter_by(email=current_user.email).first()
        users = User.query.filter(User.id != current_user.id).all()[:3]
        for userdata in users:
            if userdata.is_business == True:
                datauser = Business_Profile.query.filter_by(user_id = userdata.id).first()
                userdata.image_file = datauser.logo
            else:
                datauser = Consumer.query.filter_by(user_id = userdata.id).first()
                userdata.image_file = datauser.profilepic
        # jsonify
        if user.is_business == False:
            posts_json = []
            for post in posts:
                id = post['id']
                content = post['content']
                date_posted = post['date_posted']
                user_id = post['user_id']
                likes = mongo_db.db.like.find({'post_id':id})
                like = len(list(likes))
                # user_id = 3
                time = datetime.now() - date_posted
                if time.days == 0:
                    post_times = time.total_seconds()
                    if post_times >= 60:
                        post_timem = post_times / 60
                        if post_timem >= 60:
                            post_timeh = post_timem / 60
                            post_time = f'{int(post_timeh)}h'
                        else:
                            post_time = f'{int(post_timeh)}m'
                    else:
                        post_time = f'{int(post_times)}s'
                else:
                    post_time = f'{time.days}d'

                user = User.query.filter_by(id=user_id).first()
                username = user.username
                name = user.name
                image_file = user.image_file
                post_image = post['post_image']
                # check the number of likes for this post
                likes = Like.query.filter_by(post_id=id).count()
                # all comments for this post
                comments = mongo_db.db.comment.find({'post_id': id})  # jsonify
                comments_json = []
                for comment in comments:
                    # id, date_posted, content, user_id, post_id
                    id_comment = comment['id']
                    content_comment = comment['content']
                    date_posted_comment = comment['date_posted']
                    time = datetime.now() - date_posted_comment
                    if time.days == 0:
                        comment_times = time.total_seconds()
                        if comment_times >= 60:
                            comment_timem = comment_times / 60
                            if comment_timem >= 60:
                                comment_timeh = comment_timem / 60
                                comment_time = f'{int(comment_timeh)}h'
                            else:
                                comment_time = f'{int(comment_timem)}m'
                        else:
                            comment_time = f'{int(comment_times)}s'
                    else:
                        comment_time = f'{time.days}d'
                    user_id_comment = comment['user_id']
                    post_id_comment = comment['post_id']
                    comment_json = {
                        "id": id_comment,
                        "content": content_comment,
                        "date_posted": comment_time,
                        "user_id": user_id_comment,
                        "post_id": post_id_comment,
                    }
                    comments_json.append(comment_json)
                    # sort comments by date_posted
                    comment_json = sorted(comments_json, key=lambda k: k['date_posted'], reverse=True)

                to_post = {
                    'id': id,
                    'content': content,
                    'date_posted': post_time,
                    'username': username,
                    'name': name,
                    'likes': like   ,
                    'comments': comments_json,
                    'post_image': "./static/images/post_images/" + post_image,
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
        return render_template('postcons.html', title='Posts', followers=followers, following=following, \
                               posts=posts_json, name=current_user.name, username=current_user.username, users=users,
                               user_image="./static/images/user_images/" + current_userdata.profilepic)
    # return render_template('postcons.html', title='Posts')


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')


# for changepassword for consumer & business profile
@app.route('/changepassword', methods=['GET', 'POST'])
@login_required
def changepassword():
    if current_user.is_authenticated:
        if request.method == 'POST':
            password = request.form['oldpassword']
            newpass = request.form['newpassword']
            confirmpass = request.form.get('confirmpassword')
            if password and newpass and confirmpass:
                user = User.query.filter_by(email=current_user.email).first()
                if user and bcrypt.check_password_hash(user.password, password):
                    if newpass == confirmpass:
                        password_encrypted = bcrypt.generate_password_hash(newpass).decode('utf-8')
                        user.password = password_encrypted
                        db.session.add(user)
                        db.session.commit()
                        return redirect(url_for('logout'))
                    else:
                        flash("new password & confirm password mismacth")
                else:
                    flash("old password incorrect")
            else:
                flash('all Field required')
    else:
        return redirect(url_for('login'))
    return render_template('changepassword.html', title='Change Password')


# for delete endpoint for consumer & business profile
@app.route('/deleteaccount', methods=['GET', 'POST'])
@login_required
def deleteaccount():
    if current_user.is_authenticated:
        if request.method == 'POST':
            password = request.form['password']
            if password:
                user = User.query.filter_by(email=current_user.email).first()
                if password == password:
                    business = Business_Profile.query.filter(Business_Profile.user_id==user.id).first()
                    if business:
                        db.session.delete(business)
                    customer = Consumer.query.filter(Consumer.user_id==user.id).first()
                    if customer:
                        db.session.delete(customer)
                    data = {'user_id': user.id}
                    posts = mongo_db.db.posts.delete_many(data)
                    products = mongo_db.db.product.delete_many(data)
                    comments = mongo_db.db.comment.delete_many(data)
                    mongo_db.db.like.delete_many(data)
                    db.session.delete(user)
                    db.session.commit()
                    return redirect(url_for('logout'))
                else:
                    flash("password mismacth")
            else:
                flash("password incorrect")
        else:
            flash('all Field required')
    else:
        return redirect(url_for('login'))
    return render_template('deleteaccount.html', title='Delete Account')


@app.route('/post_new', methods=['GET', 'POST'])
@login_required
def post_new():
    if current_user.is_business == False:
        return redirect(url_for('postconsumer'))
    if request.method == 'POST':
        content = request.form['content']
        if content == "":
            flash('Please fill in all fields', 'danger')
            return redirect(url_for('posts'))
        try:
            post_image = request.files['post_image']
            print(post_image)
        except:
            post_image = None

        if post_image:
            filename = secure_filename(post_image.filename)
            post_image.save(os.path.join(app.config['UPLOAD_FOLDER'], 'post_images', filename))
            post_image = filename
        else:
            post_image = '-'
        # id, date_posted, content, user_id, post_image

        date_posted = datetime.now()
        user_id = current_user.id
        # post = Post(id, date_posted, content, user_id, post_image)
        ## use mongodb to insert new post
        # db.session.add(post)
        # db.session.commit()
        post = mongo_db.db.posts.find_one()
        if post is None:
            data = {
                'id': 1,
                'date_posted': date_posted,
                'content': content,
                'user_id': user_id,
                'post_image': post_image
            }
            mongo_db.db.posts.insert_one(data)
        else:
            posts = mongo_db.db.posts.find()
            id = 0
            for products in posts:
                if id < products['id']:
                    id = products['id']
            post = {
                'id': id + 1,
                'date_posted': date_posted,
                'content': content,
                'user_id': user_id,
                'post_image': post_image
            }
            mongo_db.db.posts.insert_one(post)
        flash('Your post has been created!', 'success')
        return redirect(url_for('posts'))
    return render_template('posts.html', title='New Post')


@app.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = mongo_db.db.posts.find_one({"id": post_id})
    if post['user_id'] == current_user.id:

        if request.method == 'POST':
            content = request.form.get('content')
            post_image = request.files['post_image']
            if not content:
                flash('Please fill in all fields', 'danger')
            else:
                filename = secure_filename(post_image.filename)
                post_image.save(os.path.join(app.config['UPLOAD_FOLDER'], 'post_images', filename))
                post_image = filename
                # db.session.commit()
                # use monogodb to update post
                mongo_db.db.posts.update_one({"id": post_id}, {"$set": {"content": content, "post_image": post_image}})

                flash('Your post has been updated', 'success')
                return redirect(url_for('mypost'))
    return redirect(url_for('mypost'))


@app.route('/post/<int:post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = mongo_db.db.posts.find_one({"id": post_id})
    if post['user_id'] == current_user.id:
        mongo_db.db.posts.delete_one({"id": post_id})
        mongo_db.db.comment.delete_one({"post_id": post_id})
        flash('Your post has been deleted', 'success')
    return redirect(url_for('mypost'))


@app.route('/user/<string:username>')
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(user_id=user.id).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)


## LIKE,COMMENT,RETWEET
@app.route('/post/<int:post_id>/like', methods=['GET', 'POST'])
@login_required
def like_post(post_id):
    if request.method == "GET":
        postdata = mongo_db.db.post.find_one({'id' : post_id})
        searchdata = {'post_id':post_id,'user_id':current_user.id}
        likedata = mongo_db.db.like.find_one(searchdata)
        if postdata is None:
            flash('post does not exits')
        if likedata is not None:
            print(likedata)
            mongo_db.db.like.delete_one(searchdata)
        else:
            mongo_db.db.like.insert_one(searchdata)
        if current_user.is_business == True:
            return redirect(url_for('posts'))
        else:
            return redirect(url_for('postconsumer'))


@app.route('/post/<int:post_id>/comment', methods=['GET', 'POST'])
@login_required
def comment_post(post_id):
    if request.method == 'POST':
        content = request.form.get('comment')
        if not content:
            flash('Please enter a comment', 'danger')
        else:
            # id, date_posted, content, user_id, post_id
            date_posted = datetime.now()
            user_id = current_user.id
            comment = mongo_db.db.comment.find_one()
            if comment is None:
                data = {
                    'id': 1,
                    'post_id': post_id,
                    'user_id': user_id,
                    'content': content,
                    'date_posted': date_posted
                }
                mongo_db.db.comment.insert_one(data)
            else:
                id = 0
                comments = mongo_db.db.comment.find()
                for comment in comments:
                    if id < comment['id']:
                        id = comment['id']
                data = {
                    'id': id + 1,
                    'post_id': post_id,
                    'user_id': user_id,
                    'content': content,
                    'date_posted': date_posted
                }
                mongo_db.db.comment.insert_one(data)
            flash('Your comment has been posted', 'success')
            if current_user.is_business == True:
                return redirect(url_for('posts'))
            else:
                return redirect(url_for('postconsumer'))
    return redirect(url_for('posts'))


# FOLLOW/UNFOLLOW
@app.route('/user/<string:to_follow_username>/follow', methods=['GET', 'POST'])
@login_required
def follow_user(to_follow_username):
    if flask.request.method == 'GET':
        print(to_follow_username, file=sys.stdout)
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
        print('You are following {}!'.format(to_follow_username), file=sys.stdout)
        return redirect(url_for('posts'))
    else:
        return redirect(url_for('posts'))


@app.route('/user/<string:to_unfollow_username>/unfollow', methods=['GET', 'POST'])
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


# for business profile endpoint
@app.route('/business_profile', methods=['GET', 'POST'])
@login_required
def business_profile():
    if current_user.is_authenticated:
        if request.method == 'POST':
            name = request.form['name']
            url = request.form['url']
            address = request.form['address']
            social_url = request.form['social_url']
            logo = request.files['logo']
            contact_number = request.form['contact_number']
            if logo:
                filename = secure_filename(logo.filename)
                logo.save(os.path.join(app.config['UPLOAD_FOLDER'], 'user_images', filename))
                logo = filename
            else:
                logo = 'default.jpg'
            id = Business_Profile.query.count() + 1
            # logo = 'default.jpg'
            # print(current_user.user_id)
            user = Business_Profile(id=id, user_id=current_user.id, name=name,logo=logo,
                                    address=address, url=url, social_url=social_url,
                                    contact_number=contact_number)
            db.session.add(user)
            db.session.commit()
            flash('You are now business-profile registered and can log in', 'success')
            # login_user(user)
            return redirect(url_for('posts'))
    return render_template('business.html', title='Business')


# for consumer endpoint
@app.route('/consumer', methods=['GET', 'POST'])
@login_required
def consumer():
    if current_user.is_authenticated:

        if request.method == 'POST':
            # user_id = request.form['user_id']
            address = request.form['address']
            contact_number = request.form['contact_number']
            logo = request.files['profilepic']
            if logo:
                filename = secure_filename(logo.filename)
                logo.save(os.path.join(app.config['UPLOAD_FOLDER'], 'user_images', filename))
                logo = filename
            else:
                logo = 'default.jpg'
            id = Consumer.query.count() + 1
            user = Consumer(id=id, user_id=current_user.id,profilepic=logo, address=address, contact_number=contact_number)
            db.session.add(user)
            db.session.commit()
            flash('You are now consumer registered and can log in', 'success')
            return redirect(url_for('postconsumer'))
    return render_template('consumer.html', title='Consumer')


# for add product
@app.route('/add_product', methods=['GET', 'POST'])
@login_required
def add_product():
    if current_user.is_authenticated:
        if current_user.is_business == True:
            if request.method == 'POST':
                product_name = request.form['product_name']
                product_desc = request.form['product_desc']
                product_image = request.files['product_image']
                if product_image:
                    filename = secure_filename(product_image.filename)
                    product_image.save(os.path.join(app.config['UPLOAD_FOLDER'], 'product_image', filename))
                    product_image = './static/images/product_image/' +filename
                else:
                    flash('please enter product_image')
                product = mongo_db.db.product.find_one()
                if product is None:
                    data = {
                        'id': 1,
                        'name': product_name,
                        'desc': product_desc,
                        'image': product_image,
                        'user_id': current_user.id
                    }
                    productdata = mongo_db.db.product.insert_one(data).inserted_id
                else:
                    all_products = mongo_db.db.product.find()
                    id = 0
                    for products in all_products:
                        if id < products['id']:
                            id = products['id']
                    data = {
                        'id': id + 1,
                        'name': product_name,
                        'desc': product_desc,
                        'image': product_image,
                        'user_id': current_user.id
                    }
                    productdata = mongo_db.db.product.insert_one(data).inserted_id
                return redirect(url_for('products'))
            return render_template('posts.html', title='New Product')
        return redirect(url_for('post'))
    return redirect(url_for('login'))


# for see products
@app.route('/products', methods=['GET', 'POST'])
@login_required
def products():
    if current_user.is_authenticated:
        if current_user.is_business == True:
            current_userdata = Business_Profile.query.filter_by(user_id = current_user.id).first()
            if request.method == 'GET':
                all_products = mongo_db.db.product.find({'user_id': current_user.id})
                return render_template('products.html', title='New Product', products=all_products,
                                       name=current_user.name, username=current_user.username,
                                       user_image="./static/images/user_images/" + current_userdata.logo)
        return redirect(url_for('postconsumer'))
    return redirect(url_for('login'))


# for edit products
@app.route('/edit/product/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_product(id):
    data = {
        "id": id
    }
    product = mongo_db.db.product.find_one(data)
    if current_user.is_authenticated:
        if current_user.is_business == True and current_user.id == product['user_id']:
            data = {
                    'id': id
                }
            if request.method == 'POST':
                product_name = request.form['product_name']
                product_desc = request.form['product_desc']
                product_image = request.files['product_image']
                if product_image:
                    updatedata = {
                    '$set': {
                        'image': product_image
                        }
                    }
                    filename = secure_filename(product_image.filename)
                    product_image.save(os.path.join(app.config['UPLOAD_FOLDER'], 'product_image', filename))
                    product_image = './static/images/product_image/' + filename
                    mongo_db.db.product.update_one(data, updatedata)
                elif product_name:
                    updatedata = {
                    '$set': {
                        'name': product_name,
                        }
                    }
                    mongo_db.db.product.update_one(data, updatedata)
                elif product_desc:
                    updatedata = {
                    '$set': {
                        'desc': product_desc,
                        }
                    }
                    mongo_db.db.product.update_one(data, updatedata)
                else:
                    flash('please enter one filed')
                return redirect(url_for('products'))
            return render_template('posts.html', product=product)
        return redirect(url_for('post'))
    return redirect(url_for('login'))


# for view product by ID

# for delet product by ID
@app.route('/delete/product/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_product(id):
    product = mongo_db.db.product.find_one({'id': id})
    if current_user.is_authenticated:
        if current_user.is_business == True and current_user.id == product['user_id']:
            data = {
                'id': id
            }
            deletedata = mongo_db.db.product.delete_one(data)
            flash('product deleted successfully')
            return redirect(url_for('products'))
        return redirect(url_for('post'))
    return redirect(url_for('login'))


@app.route('/mypost', methods=['GET', 'POST'])
@login_required
def mypost():
    if current_user.is_authenticated:
        if current_user.is_business == True:
            current_userdata = Business_Profile.query.filter_by(user_id = current_user.id).first()
            if request.method == 'GET':
                all_posts = mongo_db.db.posts.find({'user_id': current_user.id})
                myposts = []
                for posts in all_posts:
                    time = datetime.now() - posts['date_posted']
                    if time.days == 0:
                        post_times = time.total_seconds()
                        if post_times >= 60:
                            post_timem = post_times / 60
                            post_timem = "{:2f}".format(post_timem)
                            if int(float(post_timem)) >= 60:
                                post_timeh = int(float(post_timem)) / 60
                                post_time = f'{int(post_timeh)}h'
                            else:
                                post_time = f'{int(post_timeh)}m'
                        else:
                            post_time = f'{int(post_times)}s'
                    else:
                        post_time = f'{time.days}d'
                    posts['date_posted'] = post_time
                    myposts.append(posts)

            return render_template('myposts.html', title='New Product', products=myposts, name=current_user.name,
                                   username=current_user.username,
                                   user_image="./static/images/user_images/" + current_userdata.logo)
        return redirect(url_for('postconsumer'))
    return redirect(url_for('login'))


@app.route('/myprofile', methods=['GET', 'POST'])
@login_required
def myprofile():
    if request.method == 'GET':
        if current_user.is_business == True:
            current_userdata = Business_Profile.query.filter_by(user_id = current_user.id).first()
            business = Business_Profile.query.filter_by(user_id=current_user.id).first()
            return render_template('Bprofile.html', profile=business, name=current_user.name,
                                   username=current_user.username,email = current_user.email,
                                   user_image="./static/images/user_images/" + current_userdata.logo)
        else:
            current_userdata = Consumer.query.filter_by(user_id = current_user.id).first()
            consumer = Consumer.query.filter_by(user_id=current_user.id).first()
            return render_template('Cprofile.html', profile=consumer, name=current_user.name,
                                   username=current_user.username,email = current_user.email,
                                   user_image="./static/images/user_images/" + current_userdata.profilepic)

@app.route('/<int:user_id>/profile', methods=['GET', 'POST'])
@login_required
def profile(user_id):
    if request.method == 'GET':
        user = User.query.filter_by(id = user_id).first()
        if current_user.is_business == True:
            current_userdata = Business_Profile.query.filter_by(user_id = current_user.id).first()
            if user.is_business == True:
                data = Business_Profile.query.filter_by(user_id=user.id).first()
                return render_template('bprofilev.html',userv = user,profile=data,current_user=current_user,
                name=current_user.name,
                username=current_user.username,email = current_user.email,
                user_image="/static/images/user_images/" + current_userdata.logo)
            else:
                data = Consumer.query.filter_by(user_id=user.id).first()
                return render_template('bprofilev.html',userv = user,profile=data,current_user=current_user,
                name=current_user.name,
                username=current_user.username,email = current_user.email,
                user_image="/static/images/user_images/" + current_userdata.logo)
        else:
            current_userdata = Consumer.query.filter_by(user_id = current_user.id).first()
            if user.is_business == True:
                data = Business_Profile.query.filter_by(user_id=user.id).first()
                return render_template('cprofilev.html',userv = user,profile=data,current_user=current_user,
                name=current_user.name,
                username=current_user.username,email = current_user.email,
                user_image="/static/images/user_images/" + current_userdata.profilepic)
            else:
                data = Consumer.query.filter_by(user_id=user.id).first()
                return render_template('cprofilev.html',userv = user,profile=data,current_user=current_user,
                name=current_user.name,
                username=current_user.username,email = current_user.email,
                user_image="/static/images/user_images/" + current_userdata.profilepic)
        # current_userdata = Consumer.query.filter_by(user_id = current_user.id).first()
        # if current_userdata:
        #     if user.is_business == True:
        #         data = Business_Profile.query.filter_by(user_id=user.id).first()
        #         return render_template('profilev.html',userdata = user, profile=data, name=current_user.name,
        #                             username=current_user.username,email = current_user.email,
        #                             user_image="./static/images/user_images/" + current_userdata.profilepic)
        #     else:
        #         data = Consumer.query.filter_by(user_id=user.id).first()
        #         return render_template('profilev.html',userdata=user, profile=data, name=current_user.name,
        #                             username=current_user.username,email = current_user.email,
        #                             user_image="./static/images/user_images/" + current_userdata.profilepic)
        # else:
        #     current_userdata = Business_Profile.query.filter_by(user_id = current_user.id).first()
        #     if user.is_business == True:
        #         data = Business_Profile.query.filter_by(user_id=user.id).first()
        #         return render_template('profilev.html',userdata = user, profile=data, name=current_user.name,
        #                             username=current_user.username,email = current_user.email,
        #                             user_image="./static/images/user_images/" + current_userdata.logo)
        #     else:
        #         data = Consumer.query.filter_by(user_id=user.id).first()
        #         return render_template('profilev.html',userdata=user, profile=data, name=current_user.name,
        #                             username=current_user.username,email = current_user.email,
        #                             user_image="./static/images/user_images/" + current_userdata.logo)
