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
from models import db, User, Character, Planet,Fav_Characters,  Fav_Planets
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

@app.route('/fav_characters', methods=['GET'])
def get_fav_characters():
    fav_characters = Fav_Characters.query.all()
    results = list(map(lambda Character: Character.serialize(), fav_characters))

    return jsonify(results), 200



#  ['GET']Listar todos los registros de Character en la base de datos

@app.route('/Character', methods=['GET'])
def get_Character():
    all_Character=Character.query.all()
    results= list( map( lambda Character:Character.serialize(), all_Character ))
    
    return jsonify( results), 200

#  ['GET']Listar la información de una sola Character

@app.route('/Character/<int:Character_id>', methods=['GET'])
def get_person(Character_id):
    person = Character.query.get(Character_id)
 
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

    
@app.route('/planets', methods=['POST'])
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

@app.route('/fav_planets', methods=['POST'])
def add_new_fav_planet():
    request_body_fav_planet = request.get_json()

    new_fav_planet = Fav_Planets(
    planet=request_body_fav_planet["planet"], 
    user=request_body_fav_planet["user"])

    db.session.add(new_fav_planet)
    db.session.commit()

    return jsonify(request_body_fav_planet), 200


   
# [POST] Añade una nuevo Character favorito.
@app.route('/fav_characters', methods=['POST'])
def add_new_fav_character():
    request_body_fav_character = request.get_json()

    new_fav_character = Fav_Characters(
    character=request_body_fav_character["character"], user=request_body_fav_character["user"])
    db.session.add(new_fav_character)
    db.session.commit()

    return jsonify(request_body_fav_character), 200


# [DELETE] Elimina un planet favorito.
@app.route('/fav_planets/<int:fav_planets_id>', methods=['DELETE'])
def delete_fav_planet(fav_planets_id):
    fav_planet = Fav_Planets.query.get(fav_planets_id)

    if not fav_planet:
        return jsonify({'message': 'Fav planet not found'}), 404

    db.session.delete(fav_planet)
    db.session.commit()

    return jsonify({'message': f'Fav planet with ID {fav_planets_id} deleted successfully'}), 200



# [DELETE] Elimina una Character favorito.
@app.route('/fav_characters/<int:fav_characters_id>', methods=['DELETE'])
def delete_fav_character(fav_characters_id):
    fav_character = Fav_Characters.query.get(fav_characters_id)

    if not fav_character:
        return jsonify({'message': 'Fav Character not found'}), 404

    db.session.delete(fav_character)
    db.session.commit()

    return jsonify({'message': f'Fav character with ID {fav_characters_id} deleted successfully'}), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
