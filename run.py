"""
Application Entry Point
=======================
This is the main file to run the Flask application.
Run with: python run.py
"""
from flask import Flask
from extensions import db, login_manager
from models.user import User
from config import config
from helper import seed_database

# Create Flask app instance
app = Flask(__name__)

# Load configuration
app.config.from_object(config['development'])

# Initialize extensions with app
db.init_app(app)
login_manager.init_app(app)

# Setup user loader for flask-login
from models.user import User

@login_manager.user_loader
def load_user(user_id):
    """Load user by ID for flask-login."""
    return User.query.get(int(user_id))

# Register Blueprints (Routes)
from routes.auth_routes import auth_bp
from routes.admin_routes import admin_bp
from routes.user_routes import user_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(user_bp, url_prefix='/user')

# Add a root route that redirects to login
@app.route('/')
def index():
    from flask import redirect, url_for
    return redirect(url_for('auth.login'))



# Seed the database with admin user
seed_database(app)

if __name__ == '__main__':
    # Run the development server
    app.run(debug=True, host='0.0.0.0', port=6060)
