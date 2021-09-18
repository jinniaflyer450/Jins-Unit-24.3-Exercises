from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)