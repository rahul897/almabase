import datetime
from logging.handlers import RotatingFileHandler

from flask import Flask
# from flask_socketio import SocketIO

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import atexit

from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'wtf'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
scheduler = BackgroundScheduler()
# socketio = SocketIO(app)

from app import routes, models
atexit.register(lambda: scheduler.shutdown())