"""
Helper Functions
================
Contains helper functions like database seeding.
"""

from extensions import db
from models.user import User
import os
import secrets
from flask import current_app


def save_picture(form_picture):
    """
    Save profile picture to filesystem.
    
    Args:
        form_picture: FileStorage object from form
        
    Returns:
        filename: Name of saved file
    """
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.config['UPLOAD_FOLDER'], picture_fn)
    
    # Ensure upload directory exists
    os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    form_picture.save(picture_path)
    return picture_fn


def seed_database(app):
    """
    Seed the database with initial admin user.
    This runs only if no users exist in the database.
    
    Args:
        app: Flask application instance
    """
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        
        # Check if admin user already exists
        admin = User.query.filter_by(username='admin').first()
        
        if not admin:
            # Create default admin user
            admin = User(
                username='admin',
                email='admin@example.com',
                role='admin'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            
            # Create a sample regular user
            user = User(
                username='user',
                email='user@example.com',
                role='user'
            )
            user.set_password('user123')
            db.session.add(user)
            
            db.session.commit()
            print('Database seeded with default users:')
            print('  Admin: username=admin, password=admin123')
            print('  User:  username=user, password=user123')
