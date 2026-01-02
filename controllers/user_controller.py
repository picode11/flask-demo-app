"""
User Controller
===============
Handles regular user operations (profile viewing, etc.)
"""

import os
import secrets
from flask import render_template, current_app, flash, redirect, url_for, request
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from forms.user_forms import ProfileUploadForm
from extensions import db
from helper import save_picture


def profile():
    """
    Display user profile and handle image upload.
    
    GET: Show profile and upload form
    POST: Handle image upload
    
    Returns:
        Rendered profile template
    """
    form = ProfileUploadForm()
    
    if form.validate_on_submit():
        if form.photo.data:
            picture_file = save_picture(form.photo.data)
            current_user.profile_image = picture_file
            db.session.commit()
            flash('Your profile picture has been updated!', 'success')
            return redirect(url_for('user.profile'))
            
    image_file = url_for('static', filename='uploads/' + (current_user.profile_image or 'default.jpg'))
    return render_template('user/profile.html', user=current_user, image_file=image_file, form=form)
