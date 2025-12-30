"""
Authentication Forms
====================
Forms for user authentication (login, etc.)
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    """
    Login Form
    
    Fields:
        username: User's username (required)
        password: User's password (required)
    """
    
    username = StringField(
        'Username',
        validators=[
            DataRequired(message='Username is required'),
            Length(min=3, max=80, message='Username must be between 3 and 80 characters')
        ],
        render_kw={'placeholder': 'Enter your username', 'class': 'form-control'}
    )
    
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(message='Password is required')
        ],
        render_kw={'placeholder': 'Enter your password', 'class': 'form-control'}
    )
    
    submit = SubmitField('Login', render_kw={'class': 'btn btn-primary'})
