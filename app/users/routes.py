from flask import request, jsonify
from . import users_bp
from ..extensions import db, neo4j_driver
from .models.user import User

@users_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    
    with neo4j_driver.driver.session() as session:
        session.run("CREATE (n:User {name: $name, email: $email})",
                    name=data['name'], email=data['email'])
    
    return jsonify({"message": "User created successfully"}), 201

@users_bp.route('/<email>', methods=['GET'])
def get_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"name": user.name, "email": user.email})
    return jsonify({"message": "User not found"}), 404

@users_bp.route('/name/<name>', methods=['GET'])
def get_user_by_name(name):
    user = User.query.filter_by(name=name).first()
    if user:
        return jsonify({"name": user.name, "email": user.email})
    return jsonify({"message": "User not found"}), 404
