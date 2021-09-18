from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app
from models import db, Cupcake

def refresh_database():
    db.drop_all()
    db.create_all()
    db.session.commit()

def seed_database():
    chocolate = Cupcake(flavor="chocolate", size="small", rating=4.5)
    vanilla = Cupcake(flavor="vanilla", size="large", rating=4.7)
    red_velvet = Cupcake(flavor="red velvet", size="medium", rating=4.0)
    
    db.session.add_all([chocolate, vanilla, red_velvet])
    db.session.commit()

refresh_database()
seed_database()