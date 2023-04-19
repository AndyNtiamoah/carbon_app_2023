from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from flask_login import LoginManager


application = Flask(__name__)

# application.config['SECRET_KEY'] = os.environ['SECRET_KEY']  

application.config['SECRET_KEY'] = '23b3436c2bd9f7ee888955a2611f160471f78097432f6d3d'
DBVAR = 'postgresql://postgres:123Japanognorge@awseb-e-ak2cfptjvy-stack-awsebrdsdatabase-kjgmzyyuqnqj.cclddedhaznl.eu-north-1.rds.amazonaws.com:5432/ebdb'
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
