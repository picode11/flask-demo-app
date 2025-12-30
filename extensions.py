"""
Flask Extensions
================
Centralized initialization of Flask extensions.
Extensions are created here and initialized in the app factory.
This pattern prevents circular imports.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Database ORM
db = SQLAlchemy()

# Login Manager for user sessions
login_manager = LoginManager()

# Configure login manager
login_manager.login_view = 'auth.login'  # Redirect to this view when login is required
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'warning'
