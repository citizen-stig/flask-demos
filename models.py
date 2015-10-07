# -*- encoding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)

    def __str__(self):
        return self.username


class UserNote(db.Model):
    __tablename__ = 'user_notes'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship(User,
                           foreign_keys='UserNote.user_id',
                           backref=db.backref('user_notes', order_by=id))
    author = db.relationship(User,
                             foreign_keys='UserNote.author_id',
                             backref=db.backref('author_user_notes',
                                                order_by=id))
