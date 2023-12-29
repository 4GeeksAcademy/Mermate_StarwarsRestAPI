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
from models import db, User, People, Planet, Favourite_people,Favourite_planet
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


# [GET]Listar todos los usuarios del blog

@app.route('/user', methods=['GET'])
def get_user():
    all_users=User.query.all()
    results= list( map( lambda user:user.serialize(), all_users ))
 
  
    return jsonify( results), 200
   

#  ['GET'] Listar todos los favoritos que pertenecen al usuario actual.


#  ['GET']Listar todos los registros de people en la base de datos

@app.route('/people', methods=['GET'])
def get_people():
    all_people=People.query.all()
    results= list( map( lambda People:People.serialize(), all_people ))
    
    return jsonify( results), 200

#  ['GET']Listar la información de una sola people

@app.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    person = People.query.get(people_id)
 
    if person is None:
        return jsonify({'error': 'Planet not found'}), 404
    
    return jsonify(person.serialize()), 200


#  ['GET']Listar los registros de planets en la base de datos

@app.route('/planets', methods=['GET'])
def get_planets():
    all_planets=Planet.query.all()
    results= list( map( lambda Planets:Planets.serialize(), all_planets ))
    
    return jsonify( results), 200

#  ['GET'] Listar la información de un solo planet

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planet.query.get(planet_id)

    if planet is None:
        return jsonify({'error': 'Planet not found'}), 404

    return jsonify(planet.serialize()), 200


#^[POST] añade un nuevo planeta 

    
@app.route('/planet', methods=['POST'])
def add_new_planet():

    body = request.get_json()
    
    if (
        "name" not in body
        or "population" not in body
        or "terrain" not in body
        or "climate" not in body
        or "diameter" not in body
    ):
        return jsonify({"error": "incomplete data"}), 400
    
    #me = User('admin', 'admin@example.com')
    #db.session.add(me)
    #db.session.commit()
   
    new_planet = Planet(
        name=body["name"],
        population=body["population"],
        terrain=body["terrain"],
        climate=body["climate"],
        diameter=body["diameter"]
    )
    
    db.session.add(new_planet)
    db.session.commit()

    response_body = {
        "msg": "New planet added successfully"
    }

    return jsonify(response_body), 200



# [POST] Añade un nuevo planet favorito al usuario actual con el planet id = planet_id.



# [POST] Añade una nueva people favorita al usuario actual con el people.id = people_id.



# [DELETE] Elimina un planet favorito con el id = planet_id`.


# [DELETE] Elimina una people favorita con el id = people_id.



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
