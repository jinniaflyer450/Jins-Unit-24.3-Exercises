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

#JSON routes:

@app.route('/api/cupcakes')
def get_all_cupcakes():
    cupcakes = Cupcake.query.all()
    json_ready_cupcakes = [cupcake.serialize() for cupcake in cupcakes]
    return jsonify(cupcakes=json_ready_cupcakes)

@app.route('/api/cupcakes/<int:cupcake_id>')
def get_single_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    json_ready_cupcake = cupcake.serialize()
    return jsonify(cupcake=json_ready_cupcake)

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    json = request.json
    if json["image"] == "":
        json["image"] = None
    new_cupcake = Cupcake(flavor=json["flavor"], size=json["size"], 
    rating=json["rating"], image=json.get("image"))
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake=new_cupcake.serialize()), 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor=request.json.get("flavor", cupcake.flavor)
    cupcake.size=request.json.get("size", cupcake.size)
    cupcake.rating=request.json.get("rating", cupcake.rating)
    cupcake.image=request.json.get("image", cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):
    cupcake=Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")

#HTML routes:

@app.route('/')
def show_all_cupcakes():
    return render_template('index.html')