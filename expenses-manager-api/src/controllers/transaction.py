from flask import request, Response, jsonify, json, Blueprint, make_response, jsonify
from src.models.transaction import Transaction
from src import db

transactions = Blueprint("transactions", __name__)

@transactions.route("/", methods=["GET"])
def get_transactions():
    """
    Get transactions
    """
    try:
        current_transactions = Transaction.query.all()
        return make_response(jsonify([transaction.serialize() for transaction in current_transactions]), 200)
    except Exception as e:
        message = f"error  getting transactions: {str(e)}"
        return make_response(jsonify({"error": message}), 500)

@transactions.route("/", methods=["POST"])
def create_transaction():
    """
    Create transaction
    """
    new_transaction = Transaction(
        account_id = request.json["account_id"]
    )
    db.session.add(new_transaction)
    db.session.commit()
    message = "new transaction created successfully"
    return make_response(jsonify({"message": message}), 201)

@transactions.route("/<account_id>", methods=["GET"])
def get_account_transactions(account_id):
    """
    Get transactions belonging to a specific account
    """
    transactions = Transaction.query.filter_by(account_id = account_id)
    print("account transactons: ", transactions)
    return make_response(jsonify([transaction.serialize() for transaction in transactions]), 200)