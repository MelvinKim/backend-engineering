from flask import request, Response, jsonify, json, Blueprint, make_response, jsonify
from src.models.account import Account
from src import db, cache

accounts = Blueprint("accounts", __name__)

@accounts.route("/", methods=["GET"])
def get_accounts():
    """
    Get accounts
    """
    try:
        current_accounts = Account.query.all()
        return make_response(jsonify([account.serialize() for account in current_accounts]))
    except Exception as e:
        message = f"error getting accounts: {str(e)}"
        return make_response(
            jsonify({"error": message}),
            500
        )

@accounts.route("/", methods=["POST"])
def create_account():
    """
    Create Account
    """
    try:
        new_account = Account(
            client_id = request.json["client_id"]
        )
        db.session.add(new_account)
        db.session.commit()
        message = "new account created successfully"
        return make_response(
            jsonify({"message": message}),
            201
        )
    except Exception as e:
        message =  f"error creating new account: {str(e)}"
        return make_response(
            jsonify({'error': message}),
            500
        )

@accounts.route("/deactivate/<account_id>", methods=["PUT"])
def deactivate(account_id):
    """
    Deactivate Account
    """
    account = Account.query.get(account_id)
    account.is_active = False
    db.session.commit()

    cache.set(account_id, json.dumps(account.serialize()))

    return ('Account with Id {} deactivated successfully!').format(account_id)

@accounts.route("/activate/<account_id>", methods=["PUT"])
def activate(account_id):
    """
    Activate Account
    """
    account = Account.query.get(account_id)
    account.is_active = True
    db.session.commit()

    cache.set(account_id, json.dumps(account.serialize()))

    return ('Account with Id {} activated successfully!').format(account_id)