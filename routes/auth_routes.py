"""
Authentication Routes
=====================
URL routes for authentication (login, logout).
"""

from flask import Blueprint
from controllers import auth_controller

# Create blueprint
auth_bp = Blueprint('auth', __name__)


# Login route
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Login page and form handler."""
    return auth_controller.login()


# Logout route
@auth_bp.route('/logout')
def logout():
    """Logout and clear session."""
    return auth_controller.logout()
