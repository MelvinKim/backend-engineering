from flask import request, Response, jsonify, json, Blueprint, make_response, jsonify
from src.models.client import Client
from src import db

clients = Blueprint("clients", __name__)

# get client
@clients.route("/", methods=["GET"])
def get_clients():
    try:
        current_clients = Client.query.all()
        return make_response(jsonify([client.serialize() for client in current_clients]), 200)
    except Exception as e:
        message = f"error getting client: {str(e)}"
        return make_response(
            jsonify({'error': message}),
            500
        )
        
# create client
@clients.route("/", methods=["POST"])
def create_client():
    try:
        new_client = Client(
            firstname = request.json['firstname'],
            lastname = request.json['lastname'],
            email = request.json['email'],
            age = request.json['age']
        )
        db.session.add(new_client)
        db.session.commit()
        message = "new client created successfully"
        return make_response(
            jsonify({"message": message}),
            201
        )
    except Exception as e:
        message = f"error creating new client: {str(e)}"
        return make_response(
            jsonify({'error': message}),
            500
        )
        
# get client by id
@clients.route("/<client_id>", methods=["GET"])
def get_client_by_id(client_id):
    response = Client.query.get(client_id).serialize()
    return jsonify(response)
        
# update client details
@clients.route("/<client_id>", methods=["PUT"])
def update_client(client_id):
    client = Client.query.get(client_id)
    client.firstname = request.json["firstname"]
    client.lastname = request.json["lastname"]
    client.email = request.json["email"]
    db.session.commit()
    
    response = Client.query.get(client_id).serialize()
    return jsonify(response)

# safe delete client details
@clients.route("/<client_id>", methods=["DELETE"])
def delete_client(client_id):
    client = Client.query.get(client_id)
    client.is_active = False
    db.session.commit()
    
    return ('Client with Id "{}" deleted successfully!').format(client_id)