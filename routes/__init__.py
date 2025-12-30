"""
Routes Package
==============
This package contains all route blueprints.
Routes define URL endpoints and connect them to controllers.
"""

from .auth_routes import auth_bp
from .admin_routes import admin_bp
from .user_routes import user_bp

__all__ = ['auth_bp', 'admin_bp', 'user_bp']
