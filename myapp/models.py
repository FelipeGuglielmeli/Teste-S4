from sqlalchemy.sql import func
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    
    
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000))
    create = db.Column(db.DateTime(timezone=True), default=func.now())
    price = db.Column(db.Numeric(10,2), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __init__(self, name, description, price, user_id):
        self.name = name
        self.description = description
        self.price = price
        self.user_id = user_id