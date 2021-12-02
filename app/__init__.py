from flask import Flask
from flask.blueprints import Blueprint
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_login import LoginManager


app = Flask(__name__)



app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)
login = LoginManager(app)
login.login_view = 'administration.login'

from .appointment.routes import appointment as appoi
app.register_blueprint(appoi, url_prefix = '')

from .administrative.routes import admin
app.register_blueprint(admin)


from .appointment import routes
from .administrative import routes