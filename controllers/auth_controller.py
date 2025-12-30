"""
Authentication Controller
=========================
Handles user authentication logic (login, logout).
"""

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from forms.auth_forms import LoginForm
from models.user import User


def login():
    """
    Handle user login.
    
    GET: Display login form
    POST: Validate credentials and create session
    
    Returns:
        Rendered template or redirect
    """
    # If user is already logged in, redirect to appropriate dashboard
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('admin.dashboard'))
        return redirect(url_for('user.profile'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        # Find user by username
        user = User.query.filter_by(username=form.username.data).first()
        
        # Verify user exists and password is correct
        if user and user.check_password(form.password.data):
            # Login the user (creates session)
            login_user(user)
            flash(f'Welcome back, {user.username}!', 'success')
            
            # Redirect to the page user was trying to access, or default dashboard
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            
            # Redirect based on role
            if user.is_admin:
                return redirect(url_for('admin.dashboard'))
            return redirect(url_for('user.profile'))
        
        # Invalid credentials
        flash('Invalid username or password. Please try again.', 'danger')
    
    return render_template('auth/login.html', form=form)


def logout():
    """
    Handle user logout.
    
    Clears the user session and redirects to login.
    
    Returns:
        Redirect to login page
    """
    logout_user()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('auth.login'))
