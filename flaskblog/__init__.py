import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

# Set the secret key for the application
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', '5791628bb0b13ce0c676dfde280ba245')

# Set the SQLAlchemy database URI, with a fallback to SQLite for development
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', f'sqlite:///{os.path.join(basedir, "site.db")}')


# Initialize the SQLAlchemy, Bcrypt, LoginManager instances
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Import routes
from flaskblog import routes
