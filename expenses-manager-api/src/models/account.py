from src import db

class Account(db.Model):

    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    transactions = db.relationship('Transaction', backref='aacount', lazy=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    deactivated_at = db.Column(db.DateTime(timezone=True))
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "transactions": self.transactions,
            "client_id": self.client_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deactivated_at": self.deactivated_at,
            "is_active": self.is_active
        }