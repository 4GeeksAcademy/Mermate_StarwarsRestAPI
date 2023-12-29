from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    #favourite_planet = db.relationship('Planet', backref='User', lazy=True)
    #favourite_people = db.relationship('People', backref='User', lazy=True)

   

#class Person(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
   # name = db.Column(db.String(50), nullable=False)
   # addresses = db.relationship('Address', backref='person', lazy=True)

#class Address(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #email = db.Column(db.String(120), nullable=False)
   # person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
        #nullable=False)

  
    

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
            "character_name": self. character_name,
            "gender ":self.gender ,
            "birth_year":self.birth_year,
            "hair_color ":self.hair_color ,
            "eye_color":self.eye_color,
    
        }
    
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name=db.Column(db.String(120), unique=True, nullable=False)
    diameter   = db.Column(db.String(120), unique=False, nullable=False)
    climate = db.Column(db.String(80), unique=False, nullable=False)
    terrain = db.Column(db.String(80), unique=False, nullable=False)
    population= db.Column(db.String(80), unique=False, nullable=False)
    

    def __repr__(self):
        return '< Planet %r>' % self.planet_name

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self. planet_name,
            "diameter  ":self. diameter  ,
            "climate":self. climate,
            "terrain ":self. terrain ,
            "population":self.population,
        }

class  Favourite_planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User")
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"), nullable=False)
    planet = db.relationship("Planet")
    def __repr__(self):
        return '<favourite_planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "planet_id": self.planet_id,
            "user_id": self.user_id,
        }

class  Favourite_people(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User")
    people_id = db.Column(db.Integer, db.ForeignKey("people.id"), nullable=False)
    people = db.relationship("People")
    def __repr__(self):
        return '<favourite_people %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "planet_id": self.planet_id,
            "user_id": self.user_id,
        }
