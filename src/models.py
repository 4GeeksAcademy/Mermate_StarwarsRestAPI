from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username":self.username,
            "email": self.email,
            " is_active":self.is_active,
             
            # do not serialize the password, its a security breach
        }
    
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name=db.Column(db.String(120), unique=True, nullable=False)
    gender  = db.Column(db.String(120), unique=False, nullable=False)
    birth_year = db.Column(db.String(80), unique=False, nullable=False)
    hair_color = db.Column(db.String(80), unique=False, nullable=False)
    eye_color= db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<People %r>' % self.character_name

    def serialize(self):
        return {
            "id": self.id,
            " character_name": self. character_name,
            " gender ":self.gender ,
             "birth_year":self.birth_year,
            " hair_color ":self.hair_color ,
             "eye_color":self.eye_color,
    
        }
    
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name=db.Column(db.String(120), unique=True, nullable=False)
    diameter   = db.Column(db.String(120), unique=False, nullable=False)
    climate = db.Column(db.String(80), unique=False, nullable=False)
    terrain = db.Column(db.String(80), unique=False, nullable=False)
    population= db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '< Planets %r>' % self.planet_name

    def serialize(self):
        return {
            "id": self.id,
            " planet_name": self. planet_name,
            " diameter  ":self. diameter  ,
             " climate":self. climate,
            "  terrain ":self. terrain ,
             "population":self.population,


        }
    