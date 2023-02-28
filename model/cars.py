import json
from __init__ import app, db
from sqlalchemy import Column, Integer, Text, String, Boolean
from sqlalchemy.exc import IntegrityError


class Car(db.Model):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True)
    _make = db.Column(db.String(255), nullable=False, unique = False)
    _model = db.Column(db.String(255), nullable=False, unique = False)
    _price = db.Column(db.Integer, nullable=False, unique = False)
    _year = db.Column(db.Integer, nullable=False, unique = False)
    _desc = db.Column(db.String(255), nullable=False, unique = True)
    _engine = db.Column(db.String(255), nullable=False, unique = False)
    _body_style = db.Column(db.String(255), nullable=False, unique = False)
    _owner = db.Column(db.String(255), nullable=False, unique = False)

    def __init__(self, make, model, price, year, desc, body_style, engine, owner):
        # Adding instance attributes
        self._make = make
        self._model = model
        self._price = price
        self._year = year
        self._desc = desc
        self._body_style = body_style
        self._engine = engine
        self._owner = owner

    # Add getters and setters for make, model, price, year
    @property
    def make(self):
        return self._make
    
    @make.setter
    def make(self, make):
        self._make = make

    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, model):
        self._model = model

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        self._price = price

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, year):
        self._year = year
    
    @property
    def desc(self):
        return self._desc
    
    @desc.setter
    def desc(self, desc):
        self._desc = desc

    @property
    def body_style(self):
        return self._body_style
    
    @body_style.setter
    def body_style(self, body_style):
        self._body_style = body_style

    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, engine):
        self._engine = engine

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self._owner = owner
    

    def dictionary(self):
        dict = {
            "make" : self.make,
            "model" : self.model,
            "price" : self.price,
            "year" : self.year,
            "desc" : self.desc,
            "body_style" : self.body_style,
            "engine" : self.engine,
            "owner" : self.owner
        }
        return dict 

    def __str__(self):
        return json.dumps(self.dictionary)

    def create(self):
        try:
            # creates a Car object from Car(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "id" : self.id,
            "make" : self.make,
            "model" : self.model,
            "price" : self.price,
            "year" : self.year,
            "desc" : self.desc,
            "body_style" : self.body_style,
            "engine" : self.engine,
            "owner" : self.owner        
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, make="", model="", price="", year="", desc="", body_style="", engine="", owner=""):
        """only updates values with length"""
        if len(make) > 0:
            self.make = make
        if len(model) > 0:
            self.model = model
        if price > 0:
            self.price(price)
        if year > 0:
            self.year(year)
        if desc >= 0:
            self.desc(desc)
        if len(body_style) > 0:
            self.body_style(body_style)
        if len(engine) > 0:
            self.engine(engine)
        if len(owner) > 0:
            self.owner(owner)
        db.session.commit()
        return self  
    
    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

# Function to initialize the Cars
def initCars():
    with app.app_context():
        """Create database and tables"""
        # db.init_app(app)
        db.create_all()

        """Data for table"""
        car1 = Car(make="BMW", model="2 Series", price=34000, year=2021, desc="The BMW 2 series is a stylish sports coupe that drives just as well as it looks.", body_style="coupe", engine="2.0L four-cylinder", owner="John Doe")

        cars = [car1]

        """Builds sample user/note(s) data"""
        for car in cars:
            try:
                car.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate car, or error: {car.id}")

