from flask import Flask, request, jsonify, make_response
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
import redis
import os

# create an instance of the Flask app, assign it to the variable app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://test:test@localhost:5432/postgres"
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_KEY_PREFIX'] = 'myapp:'
app.config['CACHE_REDIS_HOST'] = 'localhost'
app.config['CACHE_REDIS_PORT'] = 6379
app.config['CACHE_REDIS_DB'] = 0
db = SQLAlchemy(app)
cache = Cache(app)
cache.init_app(app)

class User(db.Model):
  __tablename__ = 'users'
  
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  
  def json(self):
    return {'id': self.id,'username': self.username, 'email': self.email}
 
# creates tables that do not exist
with app.app_context():
  db.create_all()

# create user
@app.route('/users', methods=['POST'])
def create_user():
  try:
    data = request.get_json()
    
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
      return make_response(jsonify({'message': 'User with this username already exists'}), 400)
    
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return make_response(jsonify({'message': 'user created'}), 201)
  except Exception as e:
    error_message = f"error creating user: {str(e)}"
    return make_response(jsonify({'message': error_message}), 500)
  
# get all users
@app.route('/users', methods=['GET'])
def get_users():
  try:
    users = User.query.all()
    # TODO: Implement pagination
    return make_response(jsonify([user.json() for user in users]), 200)
  except Exception as e:
    error_message = f"error getting users: {str(e)}"
    return make_response(jsonify({'message': error_message}), 500)
  
# get users by id
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
  # get user from cache
  user_data = cache.get(id)
  if user_data:
    return make_response(jsonify(user_data), 200)
  
  try:
    user = User.query.filter_by(id=id).first()
    if user:
      # add to cache
      cache.set(id, {'id': user.id, 'username': user.username, 'email': user.email})
      return make_response(jsonify({'user': user.json()}), 200)
    return make_response(jsonify({'message': 'user not found'}), 404)
  except e:
    return make_response(jsonify({'message': 'error getting user'}), 500)
  

if __name__ == '__main__':
    app.run(debug=True)

