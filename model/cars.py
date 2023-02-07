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

    def __init__(self, make, model, price, year):
        # Adding instance attributes
        self._make = make
        self._model = model
        self._price = price
        self._year = year

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

    def dictionary(self):
        dict = {
            "make" : self.make,
            "model" : self.model,
            "price" : self.price,
            "year" : self.year,
        }
        return dict 

    def __str__(self):
        return json.dumps(self.dictionary)

    def create(self):
        try:
            # creates a Car object from User(db.Model) class, passes initializers
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
            "year" : self.year
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, make="", model="", price="", year=""):
        """only updates values with length"""
        if len(make) > 0:
            self.make = make
        if len(model) > 0:
            self.model = model
        if price > 0:
            self.price(price)
        if year > 0:
            self.year(year)
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

# Function based off of users.py
def initCars():
    """Create database and tables"""
    db.create_all()
    """Tester data for table"""
    car1 = Car(make="Lexus", model="IS 500", price=58000, year=2022)
    car2 = Car(make="Toyota", model="GR Supra 2.0", price=44000, year=2022)
    car3 = Car(make="BMW", model="I8", price=105000, year=2016)
    car4 = Car(make="Hyundai", model="Veloster N", price=30000, year=2021)
    car5 = Car(make="Mercury", model="Marauder", price=25000, year=2004)


    cars = [car1, car2, car3, car4, car5]

    """Builds sample user/note(s) data"""
    for car in cars:
        try:
            car.create()
        except IntegrityError:
            '''fails with bad or duplicate data'''
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {car.id}")
            
            