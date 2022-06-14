from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    pseudo = db
    nom = db.Column(db.String(30))
    email = db.Column(db.String(50), unique=True)
    adresse = db.Column(db.String(80))
    password = db.Column(db.String(150))
    question_secrete = db.Column(db.String(150))
    reponse_secrete = db.Column(db.String(150))
    notes = db.relationship('Note')


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(300))
    corps = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
