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

@main.route('/blog/new', methods=['GET', 'POST'])
@login_required
def blogs():
    """
    View Blog function that returns the BLog page and data
    """
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        title_blog= blog_form.title_blog.data
        description = blog_form.description.data
        new_blog = Blog(title_blog=title_blog, description=description, user=current_user)
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('main.theblog'))
    title = 'My Blog'
    return render_template('blogs.html', title=title, blog_form=blog_form)

