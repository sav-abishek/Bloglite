import datetime
import time
import os

#       IMPORT FOR FLASK
from flask import Flask, jsonify, request, make_response, flash, current_app, send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_caching import Cache

#       IMPORT FOR JWT
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from functools import wraps
import jwt

#       IMPORT FOR CELERY
from celery_worker import make_celery
from celery.result import AsyncResult
from celery import Celery
from celery.schedules import crontab
import csv
from json import dumps
from httplib2 import Http

#       IMPORT FOR MAILHOG
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from jinja2 import Template


app = Flask(__name__)
CORS(app)

###########         CONFIG      ##############
app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogs.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CACHE_TYPE'] = "RedisCache"
app.config['CACHE_REDIS_HOST'] = "localhost"
app.config['CACHE_REDIS_PORT'] = 6379

SMPTP_SERVER_HOST = "localhost"
SMPTP_SERVER_PORT = 1025
SENDER_ADDRESS="email@thejeshgn.com"
SENDER_PASSWORD = "" 


base = 'http://127.0.0.1:5000/'

db = SQLAlchemy(app)
ma = Marshmallow(app)

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)
cache = Cache(app)


@cache.cached(timeout=10,key_prefix = "get posts")
def get_posts():
    blogs = Blogs.query.all()
    return blogs


##########      GENERATE & EXPORT CSV
@celery.task
def generate_csv(username):
    my_blogs = Blogs.query.filter_by(user=username).all()

    with open('data.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['User', 'Blog Title', 'Blog Description'])
        for blog in my_blogs:
            csvwriter.writerow([blog.user, blog.title, blog.description])
    return "job started...."


@app.route('/export_csv')
def generateCSV():
    token = request.headers.get('token')
    data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    user_name = data['user']

    a = generate_csv.delay(user_name)
    return {
        "TASK_ID": a.id,
        "TASK_STATE": a.state,
        "TASK_RESULT": a.result
    }

@app.route('/download_file')
def downloadFile():
    return send_file("./data.csv")

#######################################

##########      SEND A WEBHOOK MESSAGE
@celery.task
def webhook_message():
    """Hangouts Chat incoming webhook quickstart."""
    
    url = 'https://chat.googleapis.com/v1/spaces/AAAAW26HYZw/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=kWcfX2MrZuuHFsSVPD0OKXPhsyHodEnwS7110C4lJR0%3D'
    bot_message = {
        'text': "Hey, checkout what's trending with other users on bloglite"}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    print(response)

###########     SEND A MAILHOG MAIL
@celery.task
def send_email(to_address, subject, message, content="text"):
    msg = MIMEMultipart()
    msg["From"] = SENDER_ADDRESS
    msg["To"] = to_address
    msg["Subiect"] = subject

    if content == "html":
        msg.attach(MIMEText(message, "html"))
    else:
        msg.attach(MIMEText(message, "plain"))

    s = smtplib.SMTP(host=SMPTP_SERVER_HOST, port=SMPTP_SERVER_PORT)
    s.login(SENDER_ADDRESS, SENDER_PASSWORD)
    s.send_message(msg)
    s.quit()
    return True


@app.route('/monthly_report')
def monthlyReport():
    # send_email(to_address = "dsfds@asdfs.sdf", subject = "Monthly report", message = "message")
    users = User.query.all()
    for user in users:
        user_posts = Blogs.query.filter_by(user = user.username)
        with open("monthly_report.html") as file_:
            template = Template(file_.read())
            message = template.render(data = user, dict=user_posts)
        send_email(to_address = user.email, subject = "Monthly report", message = message, content="html")

    return "Email sent"

#############################################

# @app.route('/status/<taskid>')
# def check_status(taskid):
#     a = AsyncResult(taskid, app = celery)
#     return {
#         "TASK_ID": a.id,
#         "TASK_STATE": a.state,
#         "TASK_RESULT": a.result
#     }

###########     CELERY SCHEDULE JOBS       ################
@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute=0, hour='6'), webhook_message.s(), name='Remainder everyday 6am')
    sender.add_periodic_task(crontab(0, 0, day_of_month='2'), monthlyReport.s(), name='Remainder every second day of the month')


###################################     END OF CELERY       #################################

############        MODELS      ###################
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(60), nullable = False)
    username = db.Column(db.String(30), unique=True, nullable = False)
    password = db.Column(db.String(300), nullable=False)
    followers = db.Column(db.Integer, default=0)
    posts = db.Column(db.Integer, default=0)
    

class Blogs(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String, db.ForeignKey('user.username'), nullable=False)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(100), nullable = False)
    # image = db.Column(db.String(100))
    # image_name = db.Column(db.String(100))
    # image_data = db.Column(db.LargeBinary)
    likes = db.Column(db.Integer) #Change

class Followers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    followed_by = db.Column(db.Integer, db.ForeignKey('user.username'), nullable=False) ##Change to db.String
    following = db.Column(db.Integer, db.ForeignKey('user.username'), nullable=False)   ##Change to db.String

class Likes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    liked_by = db.Column(db.Integer,db.ForeignKey('user.username'),nullable = False) ## CHAnge to db.String
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'),nullable = False)


##########      SCHEMA CONTROL FOR API RESPONSE         ################
class ProfileSchema (ma.Schema):
    class Meta:
        fields = ('id', 'email', 'username', 'followers', 'posts')
        
class BlogSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user', 'title', 'description', 'likes')

class is_FollowingSchema(ma.Schema):
    class Meta:
        fields = ('id', 'following')

profile_schema = ProfileSchema()
profiles_schema = ProfileSchema(many=True)

blogs_schema = BlogSchema(many=True)

is_following_schema = is_FollowingSchema(many=True)


##########      TOKEN VERIFICATION      ##############
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('token')
        # token = request.args.get('t')
        if token:
            try:
                jwt.decode(request.headers.get('token'), key = current_app.config['SECRET_KEY'])
            except:
                return jsonify({'message': 'Invalid token'}), 401
        else:
            return jsonify({'message': 'Missing token'}), 401
    return decorated


##########      API ROUTES      ##############

#########       LOGIN       ###############
@app.route('/login', methods = ["GET", "POST"])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()

    if user:
        if check_password_hash(user.password, password):
            token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=5)},  current_app.config['SECRET_KEY'])
            return jsonify({'token': token}), 200
        else:
            return jsonify({'error': 'invalid credentials'}, 401)
    else:
        # return make_response('sername does not exist.', 401)
            # flash('Username does not exist.', category='error')
            return jsonify({'error': 'invalid credentials'}), 401


###############     REGISTER        ###############
@app.route('/register', methods = ["GET", "POST"])
def register():
    if request.method == 'POST':
        data = request.json
        username = data['username']
        email = data['email']
        password = data['password']

        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return make_response({'message': 'Account with same email or username already exists'}, 401)
        
        new_user = User(username=username, email=email, password=generate_password_hash(password, method='sha256'))
        try:
            db.session.add(new_user)
            db.session.commit()
            return make_response({'message': 'Account created Succesfully'}, 200)
        except:
            return make_response({'message': 'Account Not Created'}, 401)
    return make_response({'message': 'JWT works'}, 401)

###########     MY PROFILE      ###########
@token_required
@app.route('/myprofile', methods = ["GET"])
def profile():
    token = request.headers.get('token')
    data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    username = data['user']
    prof = User.query.filter_by(username=username).first()
    followers = int(Followers.query.filter_by(following = username).count())
    following = int(Followers.query.filter_by(followed_by = username).count())
    # return jsonify(profile_schema.dump(prof))
    return jsonify({"username": prof.username, "posts": prof.posts,  "email": prof.email, "followers": followers, "following": following})


# @app.route('/upload', methods=['POST'])
# def upload():
#     file = request.files['file']
#     image = Image(name=file.filename, data=file.read())
#     db.session.add(image)
#     db.session.commit()
#     return jsonify({'message': 'Image uploaded successfully!'})

##########      ADD A NEW POST      ##########
@token_required
@app.route('/addpost', methods=["POST"])
def addPost():
    token = request.headers.get('token')
    data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    username = data['user']

    title = request.json['title']
    description = request.json['description']

    new_post = Blogs(user=username, title=title, description=description, likes=0)
    user_prof = User.query.filter_by(username=username).first()
    try:
        user_prof.posts = int(user_prof.posts) + 1
        db.session.add(new_post)
        db.session.commit()
        return make_response({'message': 'Post created successfully'}, 200)
    except:
        return make_response({'message': 'Post could not be created!X!X!X'}, 200)


##########      EDIT A NEW POST      ##########
@token_required
@app.route('/edit/<int:id>', methods = ["POST"])
def editPost(id):
    blog = Blogs.query.filter_by(id=id).first()
    blog.title = request.json['title']
    blog.description = request.json['description']
    try:
        db.session.commit()
        return make_response({'message': 'Post edited successfully'}, 200)
    except:
        return make_response({'error': 'Post could not be edited!X!X!X'}, 200)


##########      DELETE A NEW POST      ##########
@token_required
@app.route('/delete/<int:id>')
def deletePost(id):
    token = request.headers.get('token')
    data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    username = data['user']

    blog = Blogs.query.filter_by(id=id).first()
    user_prof = User.query.filter_by(username=username).first()
    try:
        user_prof.posts = int(user_prof.posts) - 1
        db.session.delete(blog)
        db.session.commit()
        return make_response({'message': 'Post delete successfully'}, 200)
    except:
        return make_response({'error': 'Post could not be deleted!X!X!X'}, 200)


###########         SEARCH POST         ############
@token_required
@app.route('/search', methods=["POST"])
def search():
    token = request.headers.get('token')
    data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    username = data['user']

    search_query = request.json['query']
    users = User.query.filter(User.username.like(f"%{search_query}%")).all()
    return jsonify(profiles_schema.dump(users))

###########     ISLIKED         ##################
@token_required
@app.route('/is_liked/<int:id>', methods = ["POST", "GET"])
def is_liked(id):
    token = request.headers.get('token')
    data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    username = data['user']
    like = Likes.query.filter_by(liked_by = username, blog_id = id).first()
    if like:
        return make_response({'message': True}, 200)
    else:
        return make_response({'message': False}, 400)


###########     LIKE A POST         ##################
@token_required
@app.route('/like/<int:id>', methods = ["POST", "GET"])
def likes(id):
    token = request.headers.get('token')
    data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    username = data['user']
    like = Likes(liked_by = username, blog_id = id)
    try:
        db.session.add(like)
        db.session.commit()
        return make_response({'message': 'Like created succesfully'}, 200)
    except:
        return make_response({'message': 'Error with liking the posts'}, 400)
    

###########     UNLIKE A POST         ##################
@token_required
@app.route('/unlike/<int:id>', methods = ["POST", "GET"])
def unlike(id):
    token = request.headers.get('token')
    data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    username = data['user']
    like = Likes.query.filter_by(liked_by = username, blog_id = id).first()

    if like:
        db.session.delete(like)
        db.session.commit()
        return make_response({'message': 'Unliked succesfully'}, 200)
    else:
        return make_response({'message': 'Error with unliking the posts'}, 400)
    
#########       IS_FOLLOWING       ############
@token_required
@app.route('/is_following', methods = ["POST", "GET"])
def is_following():
    token = request.headers.get('token')
    data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    followed_by = data['user']
    # following = user
    follow = Followers.query.filter_by(followed_by = followed_by).all()
    return is_following_schema.dump(follow)

    
#########       FOLLOWING SOMEONE       ############
@token_required
@app.route('/follow/<string:user>', methods = ["POST", "GET"])
def follow_Someone(user):
    token = request.headers.get('token')
    data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    followed_by = data['user']
    following = user
    follow = Followers(followed_by = followed_by, following = following)
    following_user = User.query.filter_by(username=following).first()
    try:
        following_user.followers = int(following_user.followers) + 1
        db.session.add(follow)
        db.session.commit()
        return make_response({'message': 'Followed perfectly'}, 200)
    except:
        return make_response({'message': 'Error with following another user'}, 400)
    
#########       UNFOLLOW SOMEONE       ############
@token_required
@app.route('/unfollow/<string:user>', methods = ["POST", "GET"])
def unfollow_Someone(user):
    token = request.headers.get('token')
    data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    followed_by = data['user']
    following = user
    follow = Followers.query.filter_by(followed_by = followed_by, following = following).first()
    following_user = User.query.filter_by(username=following).first()
    if follow:
        following_user.followers = int(following_user.followers) - 1
        db.session.delete(follow)
        db.session.commit()
        return make_response({'message': 'Un-followed perfectly'}, 200)
    else:
        return make_response({'message': 'youre not following'}, 400)    



############        MY USER POSTS       ##########
@token_required
@app.route('/myposts', methods=["GET"])
def myPosts():
    token = request.headers.get('token')
    data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    username = data['user']
    blogs = Blogs.query.filter_by(user = username).all()
    return jsonify( blogs_schema.dump(blogs) )


############        MY USER POSTS       ##########
@token_required
@app.route('/dashboard_posts', methods=["GET"])
def dashoardPosts():
    token = request.headers.get('token')
    data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    username = data['user']
    users_im_following = Followers.query.filter_by(followed_by=username).all()
    # blogs = Blogs.query.filter(or_(User == v.following for v in users_im_following))
    # blogs = Blogs.query.all()
    blogs = get_posts()
    # blogs = Blogs.query.all()
    return jsonify( blogs_schema.dump(blogs) )



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)