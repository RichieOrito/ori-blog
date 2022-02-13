from flask import render_template, request, redirect, url_for, abort,jsonify, flash
from flask_login import login_required, current_user
from . forms import BlogForm, CommentForm
from .import main
from .. import db, photos
from ..models import User, Blog, Comment
from ..request import get_blogQuotes

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    blogQuote = get_blogQuotes()
    title = 'Home -welcome to My Blogs'
    
    return render_template('index.html',title = title, blogQuote=blogQuote)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
