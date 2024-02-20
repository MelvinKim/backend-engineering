from init import db

class Account(db.Model):
    
    __tablename__ = 'accounts'
    
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    client = db.relationship('Client',
        primaryjoin=('Account.client_id == Client.id'),
        remote_side="Client.id")
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    deactivated_at = db.Column(db.DateTime(timezone=True))
    is_active = db.Column(db.Boolean, default=False, nullable=False)