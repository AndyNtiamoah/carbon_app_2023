from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from flask_login import LoginManager


application = Flask(__name__)

# application.config['SECRET_KEY'] = os.environ['SECRET_KEY']  

application.config['SECRET_KEY'] = os.environ['SECRET_KEY']  
DBVAR = DBVAR="postgresql://username:os.environ.get(‘DB_PASSWORD’)@host:port/database"
DBVAR = "postgresql://qpkkgqggrfdfyb:a6d286a6f688ab48e035bcdc614566ef5f9d76f4ed6c44073597a19c0be2e6d8@ec2-52-50-161-219.eu-west-1.compute.amazonaws.com:5432/d93oucbfvllhpg"
# databases for users and transport 
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
application.config['SQLALCHEMY_BINDS'] ={'transport': DBVAR}

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager= LoginManager(application)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)
