"""
User Forms
==========
Forms for user CRUD operations with validations.
"""

from flask_wtf import FlaskForm
import flask_wtf.file
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional, ValidationError
from models.user import User


class UserCreateForm(FlaskForm):
    """
    User Creation Form
    
    Used by admin to create new users.
    All fields are required for new user creation.
    """
    
    username = StringField(
        'Username',
        validators=[
            DataRequired(message='Username is required'),
            Length(min=3, max=80, message='Username must be between 3 and 80 characters')
        ],
        render_kw={'placeholder': 'Enter username', 'class': 'form-control'}
    )
    
    email = StringField(
        'Email',
        validators=[
            DataRequired(message='Email is required'),
            Email(message='Please enter a valid email address'),
            Length(max=120, message='Email must be less than 120 characters')
        ],
        render_kw={'placeholder': 'Enter email address', 'class': 'form-control'}
    )
    
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(message='Password is required'),
            Length(min=6, max=128, message='Password must be between 6 and 128 characters')
        ],
        render_kw={'placeholder': 'Enter password (min 6 characters)', 'class': 'form-control'}
    )
    
    role = SelectField(
        'Role',
        choices=[('user', 'User'), ('admin', 'Admin')],
        validators=[DataRequired(message='Role is required')],
        render_kw={'class': 'form-control'}
    )
    
    submit = SubmitField('Create User', render_kw={'class': 'btn btn-primary'})
    
    def validate_username(self, field):
        """Check if username already exists."""
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different one.')
    
    def validate_email(self, field):
        """Check if email already exists."""
        user = User.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError('Email already registered. Please use a different email.')


class UserEditForm(FlaskForm):
    """
    User Edit Form
    
    Used by admin to edit existing users.
    Password is optional - only updated if provided.
    """
    
    username = StringField(
        'Username',
        validators=[
            DataRequired(message='Username is required'),
            Length(min=3, max=80, message='Username must be between 3 and 80 characters')
        ],
        render_kw={'placeholder': 'Enter username', 'class': 'form-control'}
    )
    
    email = StringField(
        'Email',
        validators=[
            DataRequired(message='Email is required'),
            Email(message='Please enter a valid email address'),
            Length(max=120, message='Email must be less than 120 characters')
        ],
        render_kw={'placeholder': 'Enter email address', 'class': 'form-control'}
    )
    
    password = PasswordField(
        'New Password (leave blank to keep current)',
        validators=[
            Optional(),
            Length(min=6, max=128, message='Password must be between 6 and 128 characters')
        ],
        render_kw={'placeholder': 'Enter new password (optional)', 'class': 'form-control'}
    )
    
    role = SelectField(
        'Role',
        choices=[('user', 'User'), ('admin', 'Admin')],
        validators=[DataRequired(message='Role is required')],
        render_kw={'class': 'form-control'}
    )
    
    photo = flask_wtf.file.FileField('Profile Picture', validators=[
        flask_wtf.file.FileAllowed(['jpg', 'png', 'jpeg', 'gif'], 'Images only!')
    ])
    
    submit = SubmitField('Update User', render_kw={'class': 'btn btn-primary'})
    
    def __init__(self, original_username=None, original_email=None, *args, **kwargs):
        """
        Initialize form with original values for validation.
        
        Args:
            original_username: Current username (to allow keeping same username)
            original_email: Current email (to allow keeping same email)
        """
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
        self.original_email = original_email
    
    def validate_username(self, field):
        """Check if username already exists (excluding current user)."""
        if field.data != self.original_username:
            user = User.query.filter_by(username=field.data).first()
            if user:
                raise ValidationError('Username already exists. Please choose a different one.')
    
    def validate_email(self, field):
        """Check if email already exists (excluding current user)."""
        if field.data != self.original_email:
            user = User.query.filter_by(email=field.data).first()
            if user:
                raise ValidationError('Email already registered. Please use a different email.')


class ProfileUploadForm(FlaskForm):
    """
    Form for uploading profile picture.
    """
    photo = flask_wtf.file.FileField('Profile Picture', validators=[
        flask_wtf.file.FileRequired(),
        flask_wtf.file.FileAllowed(['jpg', 'png', 'jpeg', 'gif'], 'Images only!')
    ])
    submit = SubmitField('Upload', render_kw={'class': 'btn btn-primary'})
