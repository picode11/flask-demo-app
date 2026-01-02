"""
Admin Controller
================
Handles admin-only operations like user CRUD.
"""

from flask import render_template, redirect, url_for, flash
from forms.user_forms import UserCreateForm, UserEditForm
from models.user import User
from extensions import db
from helper import save_picture


def dashboard():
    """
    Admin dashboard.
    
    Shows overview statistics and quick links.
    
    Returns:
        Rendered dashboard template
    """
    # Get counts for dashboard stats
    total_users = User.query.count()
    admin_count = User.query.filter_by(role='admin').count()
    user_count = User.query.filter_by(role='user').count()
    
    return render_template(
        'admin/dashboard.html',
        total_users=total_users,
        admin_count=admin_count,
        user_count=user_count
    )


def list_users():
    """
    List all users.
    
    Returns:
        Rendered user list template
    """
    users = User.query.order_by(User.created_at.desc()).all()
    return render_template('admin/users.html', users=users)


def create_user():
    """
    Create a new user.
    
    GET: Display user creation form
    POST: Validate and create user
    
    Returns:
        Rendered template or redirect
    """
    form = UserCreateForm()
    
    if form.validate_on_submit():
        # Create new user
        user = User(
            username=form.username.data,
            email=form.email.data,
            role=form.role.data
        )
        user.set_password(form.password.data)
        
        # Save to database
        db.session.add(user)
        db.session.commit()
        
        flash(f'User "{user.username}" created successfully!', 'success')
        return redirect(url_for('admin.users'))
    
    return render_template('admin/user_form.html', form=form, title='Create User')


def edit_user(user_id):
    """
    Edit an existing user.
    
    GET: Display edit form with current data
    POST: Validate and update user
    
    Args:
        user_id: ID of user to edit
    
    Returns:
        Rendered template or redirect
    """
    user = User.query.get_or_404(user_id)
    
    # Create form with original values for validation
    form = UserEditForm(
        original_username=user.username,
        original_email=user.email
    )
    
    if form.validate_on_submit():
        # Update user data
        user.username = form.username.data
        user.email = form.email.data
        user.role = form.role.data
        
        # Only update password if provided
        if form.password.data:
            user.set_password(form.password.data)
            
        # Update profile picture if provided
        if form.photo.data:
            picture_file = save_picture(form.photo.data)
            user.profile_image = picture_file
        
        # Save changes
        db.session.commit()
        
        flash(f'User "{user.username}" updated successfully!', 'success')
        return redirect(url_for('admin.users'))
    
    # Pre-populate form with current data (GET request)
    if not form.is_submitted():
        form.username.data = user.username
        form.email.data = user.email
        form.role.data = user.role
    
    return render_template('admin/user_form.html', form=form, title='Edit User', user=user)


def delete_user(user_id):
    """
    Delete a user.
    
    Args:
        user_id: ID of user to delete
    
    Returns:
        Redirect to user list
    """
    user = User.query.get_or_404(user_id)
    
    # Store username for flash message
    username = user.username
    
    # Delete user
    db.session.delete(user)
    db.session.commit()
    
    flash(f'User "{username}" deleted successfully!', 'success')
    return redirect(url_for('admin.users'))
