from flask import Flask
from flask.blueprints import Blueprint
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail


app = Flask(__name__)



app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

from .appointment.routes import appointment as appoi
app.register_blueprint(appoi)


from .appointment import routes

