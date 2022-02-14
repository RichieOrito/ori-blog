from wtforms.validators import Required
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from flask_wtf import FlaskForm

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio.',validators = [Required()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    """
    Class to create a wtf form for creating a blog
    """
    title_blog = StringField('Title')
    description = TextAreaField('Write a Description', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    """
    Class to create a wtf form for creating a comment
    """
    comment = TextAreaField('Comment')
    submit = SubmitField('Submit')