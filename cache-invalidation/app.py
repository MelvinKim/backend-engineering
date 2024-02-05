from flask import Flask
from flask_caching import Cache
import redis

# create an instance of the Flask app, assign it to the variable app
app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
  return "Homepage."

if __name__ == '__main__':
    app.run(debug=True)

# def create_app():
#   app.config['CACHE_TYPE'] = 'redis'
#   app.config['CACHE_REDIS_HOST'] = 'localhost'
#   app.config['CACHE_REDIS_PORT'] = '6379'
#   app.config['CACHE_REDIS_DB'] = 0
  
#   # intiliaze Flask-Caching
#   cache = Cache(app=app)
#   cache.init_app(app)
  
#   # initialize Redis client
#   redis_client = redis.Redis(host='localhost', port=6379, db=0)
  
#   if __name__ == "__main__":
#     app.run(debug=False, port=5000)
    
# create_app()

