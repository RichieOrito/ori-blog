from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime
from sqlalchemy.sql import func
from . import db 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index =True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    comments = db.relationship("Comments", backref="user", lazy = "dynamic")
    date_joined = db.Column(db.DateTime,default=datetime.utcnow)
    blogs = db.relationship('Blog', backref ='user', passive_deletes=True,lazy = "dynamic")
    