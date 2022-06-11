from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    account_type = db.Column(db.String(20))
    nom = db.Column(db.String(30))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(150))
    question_secrete = db.Column(db.String(150))
    reponse_secrete = db.Column(db.String(150))
    notes = db.relationship('Note')
    animaux = db.relationship('Animal')


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(300))
    corps = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom_animal = db.Column(db.String(30))
    espece = db.Column(db.String(30))
    race = db.Column(db.String(30))
    date_naissance = db.Column(db.DateTime)
    icad = db.Column(db.Integer)
    numero_pass = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
