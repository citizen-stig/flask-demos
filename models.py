# -*- encoding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy
# from sqlalchemy import db.Column, db.Integer, db.String, DateTime, Boolean, Float

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
