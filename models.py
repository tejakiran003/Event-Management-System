from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    price_per_hour = db.Column(db.Float, nullable=False)
    status = db.Column(db.Boolean, default=True)
    mail = db.Column(db.String(100), db.ForeignKey('user.mail'), nullable=True)  # ForeignKey to User's mail
    book_events = db.relationship('BookEvent', backref='event', cascade='all, delete-orphan')

    def __str__(self):
        return self.event_name




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    mail = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(20), default='USER')
    
    book_events = db.relationship('BookEvent', backref='user', cascade='all, delete-orphan', foreign_keys='BookEvent.username')
    
    def __str__(self):
        return self.username




class BookEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), db.ForeignKey('user.username', ondelete='CASCADE'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id', ondelete='CASCADE'), nullable=False)
    mail = db.Column(db.String(100), nullable=False)  # Store mail directly here for clarity

    def __str__(self):
        return f"{self.username} Holds {self.event_id}"


    
class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    recipient = db.Column(db.String(50)) 
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
