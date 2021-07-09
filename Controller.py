from app import app, db
import Model
from flask import render_template, request, redirect, url_for, jsonify, make_response

@app.route('/get', methods=['GET'])
def getList():
    return make_response(Model.User.query.all(), 200)


@app.route('/add-user', methods=['POST'])
def create_user():
    req = request.get_json()
    if db.session.query(db.exists().where(Model.User.username == req['username'])).scalar():
        res = make_response(jsonify({"error": "User already exists"}))
        return res

    user = Model.User(
        name=req['name'],
        last_name=req['last_name'],
        address=req['address'],
        username=req['username'],
        phone=req['phone'],
        avatar=req['avatar'],
        email=req['email'],
        password=req['password']
    )

    db.session.add(user)
    db.session.commit()

    return make_response(jsonify({"message": "User created"}), 201)
