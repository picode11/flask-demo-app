"""
User Controller
===============
Handles regular user operations (profile viewing, etc.)
"""

from flask import render_template
from flask_login import current_user


def profile():
    """
    Display user profile.
    
    Shows the logged-in user's information.
    
    Returns:
        Rendered profile template
    """
    return render_template('user/profile.html', user=current_user)
