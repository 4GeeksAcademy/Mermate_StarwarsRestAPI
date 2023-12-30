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
            "is_active":self.is_active,
             
            # do not serialize the password, its a security breach
        }
class  Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120), unique=True, nullable=False)
    gender  = db.Column(db.String(120), unique=False, nullable=False)
    birth_year = db.Column(db.String(80), unique=False, nullable=False)
    hair_color = db.Column(db.String(80), unique=False, nullable=False)
    eye_color= db.Column(db.String(80), unique=False, nullable=False)
   

    

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender ":self.gender ,
            "birth_year":self.birth_year,
            "hair_color ":self.hair_color ,
            "eye_color":self.eye_color,
    
        }
    
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(120), unique=True, nullable=False)
    diameter   = db.Column(db.String(120), unique=False, nullable=False)
    climate = db.Column(db.String(80), unique=False, nullable=False)
    terrain = db.Column(db.String(80), unique=False, nullable=False)
    population= db.Column(db.String(80), unique=False, nullable=False)
  
    

    def __repr__(self):
        return '< Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter  ":self. diameter  ,
            "climate":self. climate,
            "terrain ":self. terrain ,
            "population":self.population,
        }

class   Fav_Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user_relationship = db.relationship(User)
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"), nullable=False)
    planet_relationship = db.relationship(Planet)
    def __repr__(self):
        return '<  Fav_Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "planet_id": self.planet_id,
            "user_id": self.user_id,
        }

class Fav_Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user_relationship = db.relationship(User)
    character_id = db.Column(db.Integer, db.ForeignKey("Character.id"), nullable=False)
    character_relationship = db.relationship(Character)
    def __repr__(self):
        return '<Fav_Characters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "character_id": self.character_id,
            "user_id": self.user_id,
        }