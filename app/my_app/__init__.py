from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from my_app.config import DevConfig

app = Flask(__name__)

app.config.from_object(DevConfig)
db=SQLAlchemy(app)
migrate = Migrate(app,db)
from my_app.tasks.controllers import taskRoute
app.register_blueprint(taskRoute)
""" with app.app_context():
    db.create_all() """