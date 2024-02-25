from flask import request, Response, json, Blueprint

# user controller blueprint to be registered with api blueprint
users = Blueprint("users", __name__)

# login route
@users.route('/signin', methods = ["GET", "POST"])
def handle_login():
    return Response(
        response=json.dumps({'status': "signin success"}),
        status=200,
        mimetype='application/json'
    )

# signup route
@users.route('/signup', methods = ["GET", "POST"])
def handle_signup():
    return Response(
        response=json.dumps({'status': "signup success"}),
        status=200,
        mimetype='application/json'
    )