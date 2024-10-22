import os
import re
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth
from models import db
from routes import init_routes
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

# Initialize Flask app
app = Flask(__name__, static_url_path='/pogo/static')

# Configure PostgreSQL database
uri = os.getenv("DATABASE_URL")  # Get the database URL from the environment
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri

# Initialize the database
db.init_app(app)

# Migrate the database
migrate = Migrate(app, db)

# Load API credentials for OAuth
with open('/Users/bradyespey/Projects/GitHub/PoGO/static/api_credentials.json') as f:
    credentials = json.load(f)

# OAuth configuration
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=credentials['client_id'],
    client_secret=credentials['client_secret'],
    access_token_url='https://oauth2.googleapis.com/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    redirect_uri='https://theespeys.com/pogo/oauth2callback',
    client_kwargs={'scope': 'openid profile email'}
)

# Initialize routes
init_routes(app, google)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5002,
        debug=True
    )