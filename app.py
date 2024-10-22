import os
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth
from models import db
from routes import init_routes
from flask_migrate import Migrate
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__, static_url_path='/pogo/static')

# Add secret key for session protection (important for OAuth)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback-secret-key')  # Replace with a secure key in production

# Configure PostgreSQL database (handling deprecated 'postgres://' URLs)
uri = os.getenv("DATABASE_URL")
if not uri:
    raise ValueError("DATABASE_URL is not set in environment variables")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Set up database migrations
migrate = Migrate(app, db)

# OAuth configuration
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    access_token_url='https://oauth2.googleapis.com/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    redirect_uri='https://theespeys.com/pogo/oauth2callback',
    client_kwargs={'scope': 'openid profile email'}
)

# Ensure that OAuth environment variables are set
if not os.getenv('GOOGLE_CLIENT_ID') or not os.getenv('GOOGLE_CLIENT_SECRET'):
    raise ValueError("Google OAuth credentials are not set in environment variables")

# Initialize application routes
init_routes(app, google)

# Run the Flask application
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(os.getenv("PORT", 5002)),  # Use PORT from environment for Heroku, default to 5002 locally
        debug=os.getenv('DEBUG', 'True').lower() == 'true'  # Toggle debug mode based on environment variable
    )