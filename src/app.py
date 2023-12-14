"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# Get a list of all the blog post users

@app.route('/user', methods=['GET'])
def get_user():
    all_users=User.query.all()
    results= list( map( lambda user:user.serialize(), all_users ))
    #user_list= list(results)
  
    return jsonify( results), 200
# 

# Get a list of all the people in the database

@app.route('/people', methods=['GET'])
def get_people():
    all_people=People.query.all()
    results= list( map( lambda People:People.serialize(), all_people ))
    
    return jsonify( results), 200

# Get a one single people information

@app.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    person = People.query.get(people_id)
 # If the planet doesn't exist, return a 404 error
    if person is None:
        return jsonify({'error': 'Planet not found'}), 404

    # Serialize the retrieved planet to JSON
    serialized_person = person.serialize()
    
    return jsonify(serialized_person), 200


# Get a list of all the planets in the database 

@app.route('/planets', methods=['GET'])
def get_planets():
    all_planets=Planets.query.all()
    results= list( map( lambda Planets:Planets.serialize(), all_planets ))
    
    return jsonify( results), 200

# Get one single planet information

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planets.query.get(planet_id)

    # If the planet doesn't exist, return a 404 error
    if planet is None:
        return jsonify({'error': 'Planet not found'}), 404

    # Serialize the retrieved planet to JSON
    serialized_planet = planet.serialize()

    # Return the JSON-serialized planet object
    return jsonify(serialized_planet), 200




# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
