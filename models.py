# -*- encoding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)

    def __str__(self):
        return self.username


class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __str__(self):
        return self.name


class Magazine(db.Model):
    __tablename__ = 'magazines'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))

    author = db.relationship(User,
                             backref=db.backref('magazines',
                                                order_by=id,
                                                lazy='joined'))
    genre = db.relationship(Genre,
                            backref=db.backref('magazines',
                                               order_by=id,
                                               lazy='joined'))


class WorkType(db.Model):
    __tablename__ = 'work_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __str__(self):
        return self.name


class WorkEvent(db.Model):
    __tablename__ = 'work_events'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    work_type_id = db.Column(db.Integer, db.ForeignKey('work_types.id'))
    work_type = db.relationship(WorkType,
                                backref=db.backref('work_events'), order_by=id,
                                lazy='joined')


class AuthorRate(db.Model):
    __tablename__ = 'author_rates'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    work_type_id = db.Column(db.Integer, db.ForeignKey('work_types.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    work_type = db.relationship(WorkType,
                                backref=db.backref('author_rates'), order_by=id,
                                lazy='joined')

    author = db.relationship(User,
                             backref=db.backref('author_rates'),
                             order_by=id, lazy='joined')

    def __str__(self):
        return str(self.amount)
