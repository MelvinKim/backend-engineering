from src import db

class Client(db.Model):

    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    accounts = db.relationship('Account', backref='client', lazy=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    deactivated_at = db.Column(db.DateTime(timezone=True))
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "age": self.age,
            "accounts": self.accounts,
            "created_at": self.created_at,
            "deactivated_at": self.deactivated_at,
            "is_active": self.is_active
        }