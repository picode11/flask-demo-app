"""
Admin Routes
============
URL routes for admin operations (user CRUD).
All routes require admin authentication.
"""

from functools import wraps
from flask import Blueprint, flash, redirect, url_for
from flask_login import login_required, current_user
from controllers import admin_controller

# Create blueprint
admin_bp = Blueprint('admin', __name__)


def admin_required(f):
    """
    Decorator to require admin role.
    
    Must be used AFTER @login_required decorator.
    Usage:
        @admin_bp.route('/some-route')
        @login_required
        @admin_required
        def some_view():
            ...
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin:
            flash('Access denied. Admin privileges required.', 'danger')
            return redirect(url_for('user.profile'))
        return f(*args, **kwargs)
    return decorated_function


# Dashboard route
@admin_bp.route('/')
@login_required
@admin_required
def dashboard():
    """Admin dashboard with statistics."""
    return admin_controller.dashboard()


# List all users
@admin_bp.route('/users')
@login_required
@admin_required
def users():
    """Display all users."""
    return admin_controller.list_users()


# Create new user
@admin_bp.route('/users/create', methods=['GET', 'POST'])
@login_required
@admin_required
def create_user():
    """Create a new user form and handler."""
    return admin_controller.create_user()


# Edit user
@admin_bp.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_user(user_id):
    """Edit user form and handler."""
    return admin_controller.edit_user(user_id)


# Delete user
@admin_bp.route('/users/<int:user_id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_user(user_id):
    """Delete a user."""
    return admin_controller.delete_user(user_id)
