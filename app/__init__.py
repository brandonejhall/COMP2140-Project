from flask import Flask
from flask.blueprints import Blueprint
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)


from .appointment.routes import appointment as appoi
app.register_blueprint(appoi)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from .appointment import routes

