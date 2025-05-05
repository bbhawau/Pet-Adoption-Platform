from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True,nullable=False)
    password = db.Column(db.String(150), nullable=False)
   
class AnimalGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    animals = db.relationship('Animal', backref='group', lazy=True)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    breed = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(100), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('animal_group.id'), nullable=False)