from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    """
    RegstrationForm class that passes in the required details for validation
    """

    email = StringField('your email address', validators=[Required(), Email()])
    username = StringField('your username', validators=[Required()])
    password = PasswordField('password', validators=[Required(), EqualTo('password',message='passwords must match')])
    password_confirm = PasswordField('confirm password', validators=[Required()])
    submit = SubmitField('sign Up')





