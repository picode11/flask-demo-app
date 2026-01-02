"""
User Routes
===========
URL routes for regular user operations.
All routes require authentication.
"""

from flask import Blueprint
from flask_login import login_required
from controllers import user_controller

# Create blueprint
user_bp = Blueprint('user', __name__)


# Profile route
@user_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """Display user's profile."""
    return user_controller.profile()
