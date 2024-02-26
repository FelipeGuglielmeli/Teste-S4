from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'Dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from .models import User, Product
    
    from . import auth
    app.register_blueprint(auth.bp)   
    
    from . import products
    app.register_blueprint(products.bp)
    app.add_url_rule('/', endpoint='index')
    
    create_database(app)
    
    return app

def create_database(app):
    if not path.exists('myapp/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created database!')