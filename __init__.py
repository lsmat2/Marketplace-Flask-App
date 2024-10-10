from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# db = SQLAlchemy()

def init_app():
    """Initialize Core Application"""
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize Plugins
    # db.init_app(app)

    # Include Routes
    return app