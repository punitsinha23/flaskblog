import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate  # Import Flask-Migrate

app = Flask(__name__)

# Set the secret key for the application
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# Set the SQLAlchemy database URI to PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://flaskblogdatabase_user:vKgP5yguErifewSk1rscLRXXVOhrOXcE@dpg-criglcm8ii6s73f3cfl0-a/flaskblogdatabase')

# Initialize the SQLAlchemy, Bcrypt, LoginManager, and Migrate instances
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
migrate = Migrate(app, db)  # Initialize Flask-Migrate

# Import routes
from flaskblog import routes
