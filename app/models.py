from . import db
from datetime import datetime

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    books = db.relationship('Book', backref='genre', lazy='dynamic')

    def __repr__(self):
        return f'<Genre {self.name}>'

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    author = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))

    def __repr__(self):
        return f'<Book {self.title} by {self.author}>'
