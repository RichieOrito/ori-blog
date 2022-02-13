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

    @property
    def password(self):
        raise AttributeError('You can not read the password Attribute')


    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    title_blog = db.Column(db.String(255), index=True)
    description = db.Column(db.String(255), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='CASCADE'), nullable=False)

    def save_blog(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_blogs(cls, id):
        blogs = Blog.query.filter_by(id=id).all()
        return blogs
    @classmethod
    def get_all_blogs(cls):
        blogs = Blog.query.order_by('-id').all()
        return blogs
    def __repr__(self):
        return f'Blogs {self.blog_title}'


    