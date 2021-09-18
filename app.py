from flask import Flask, request, render_template, redirect, flash, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from models import db, connect_db, Cupcake
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'catdog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ob1wankenobi@localhost/cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()

@app.route('/api/cupcakes')
def show_all_cupcakes():
    cupcakes = Cupcake.query.all()
    json_ready_cupcakes = [cupcake.serialize() for cupcake in cupcakes]
    return jsonify(cupcakes=json_ready_cupcakes)

@app.route('/api/cupcakes/<int:cupcake_id>')
def show_single_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    json_ready_cupcake = cupcake.serialize()
    return jsonify(cupcake=json_ready_cupcake)

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    json = request.json
    new_cupcake = Cupcake(flavor=json["flavor"], size=json["size"], 
    rating=json["rating"], image=json.get("image"))
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake=new_cupcake.serialize()), 201)
