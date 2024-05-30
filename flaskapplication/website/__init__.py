import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Simple Secret Key"
    database_path = os.path.join(app.root_path, DB_NAME)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
    db.init_app(app)

    from .routes import routes
    app.register_blueprint(routes, url_prefix="/")

    create_database(app)
    app.config['DEBUG'] = True

    return app

def create_database(app):
    database_path = os.path.join(app.root_path, DB_NAME)
    if not os.path.exists(database_path):
        with app.app_context():
            db.create_all()
            print("Database Created")
