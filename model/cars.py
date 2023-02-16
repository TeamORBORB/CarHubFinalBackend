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
    _likes = db.Column(db.Integer, nullable=False, unique = False)
    _engine = db.Column(db.String(255), nullable=False, unique = False)
    _body_style = db.Column(db.String(255), nullable=False, unique = False)


    def __init__(self, make, model, price, year, likes, body_style, engine):
        # Adding instance attributes
        self._make = make
        self._model = model
        self._price = price
        self._year = year
        self._likes = likes
        self._body_style = body_style
        self._engine = engine

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
    def likes(self):
        return self._likes
    
    @likes.setter
    def likes(self, likes):
        self._likes = likes

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
        
    def dictionary(self):
        dict = {
            "make" : self.make,
            "model" : self.model,
            "price" : self.price,
            "year" : self.year,
            "likes" : self.likes,
            "body_style" : self.body_style,
            "engine" : self.engine
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
            "likes" : self.likes,
            "body_style" : self.body_style,
            "engine" : self.engine
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, make="", model="", price="", year="", likes="", body_style="", engine=""):
        """only updates values with length"""
        if len(make) > 0:
            self.make = make
        if len(model) > 0:
            self.model = model
        if price > 0:
            self.price(price)
        if year > 0:
            self.year(year)
        if likes >= 0:
            self.likes(likes)
        if len(body_style) > 0:
            self.body_style(body_style)
        if len(engine) > 0:
            self.engine(engine)
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
        db.init_app(app)
        db.create_all()

        """Data for table"""
        car1 = Car(make="BMW", model="2 Series", price=34000, year=2021, likes=0, body_style="coupe", engine="2.0L four-cylinder")
        car2 = Car(make="BMW", model="3 Series", price=41000, year=2021, likes=0, body_style="sedan", engine="2.0L four-cylinder")
        car3 = Car(make="BMW", model="4 Series", price=51000, year=2021, likes=0, body_style="coupe", engine="2.0L four-cylinder")
        car3 = Car(make="BMW", model="4 Series", price=51000, year=2021, likes=0, body_style="coupe", engine="2.0L turbo 4-cylinder")
        car4 = Car(make="BMW", model="5 Series", price=54000, year=2021, likes=0, body_style="sedan", engine="2.0L turbo 4-cylinder")
        car5 = Car(make="BMW", model="7 Series", price=83000, year=2021, likes=0, body_style="sedan", engine="3.0L turbo inline-6")
        car6 = Car(make="BMW", model="X1", price=35000, year=2021, likes=0, body_style="SUV", engine="2.0L turbo 4-cylinder")
        car7 = Car(make="BMW", model="X2", price=40000, year=2021, likes=0, body_style="SUV", engine="2.0L turbo 4-cylinder")
        car8 = Car(make="BMW", model="X3", price=44000, year=2021, likes=0, body_style="SUV", engine="2.0L turbo 4-cylinder")
        car9 = Car(make="BMW", model="X4", price=50000, year=2021, likes=0, body_style="SUV", engine="2.0L turbo 4-cylinder")
        car10 = Car(make="BMW", model="X5", price=56000, year=2021, likes=0, body_style="SUV", engine="3.0L turbo inline-6")
        car11 = Car(make="BMW", model="X6", price=64000, year=2021, likes=0, body_style="SUV", engine="3.0L turbo inline-6")
        car12 = Car(make="BMW", model="Z4", price=50000, year=2021, likes=0, body_style="convertible", engine="2.0L turbo 4-cylinder")
        car20 = Car(make="Mercedes-Benz", model="A-Class", price=34000, year=2021, likes=0, body_style="sedan", engine="2.0L turbo 4-cylinder")
        car21 = Car(make="Mercedes-Benz", model="C-Class", price=45000, year=2021, likes=0, body_style="sedan", engine="2.0L turbo 4-cylinder")
        car22 = Car(make="Mercedes-Benz", model="E-Class", price=54000, year=2021, likes=0, body_style="sedan", engine="2.0L turbo 4-cylinder")
        car23 = Car(make="Mercedes-Benz", model="S-Class", price=90000, year=2021, likes=0, body_style="sedan", engine="3.0L turbo inline-6")
        car24 = Car(make="Mercedes-Benz", model="GLE-Class", price=54000, year=2021, likes=0, body_style="SUV", engine="3.5L V6")
        car25 = Car(make="Mercedes-Benz", model="GLC-Class", price=48000, year=2021, likes=0, body_style="SUV", engine="2.0L Inline-4 Turbo")
        car26 = Car(make="Tesla", model="Model 3", price=38000, year=2021, likes=0, body_style="Sedan", engine="Electric")
        car27 = Car(make="Tesla", model="Model S", price=79000, year=2021, likes=0, body_style="Sedan", engine="Electric")
        car28 = Car(make="Tesla", model="Model X", price=88000, year=2021, likes=0, body_style="SUV", engine="Electric")
        car29 = Car(make="Tesla", model="Model Y", price=41000, year=2021, likes=0, body_style="SUV", engine="Electric")
        car30 = Car(make="Jaguar", model="F-PACE", price=45000, year=2021, likes=0, body_style="SUV", engine="2.0L Inline-4 Turbo")
        car31 = Car(make="Jaguar", model="I-PACE", price=70000, year=2021, likes=0, body_style="SUV", engine="Electric")
        car32 = Car(make="Jaguar", model="E-PACE", price=40000, year=2021, likes=0, body_style="SUV", engine="2.0L Inline-4 Turbo")
        car33 = Car(make="Jaguar", model="XE", price=45000, year=2021, likes=0, body_style="Sedan", engine="2.0L Inline-4 Turbo")
        car34 = Car(make="Jaguar", model="XF", price=52000, year=2021, likes=0, body_style="Sedan", engine="2.0L Inline-4 Turbo")
        car35 = Car(make="Land Rover", model="Range Rover Evoque", price=45000, year=2021, likes=0, body_style="SUV", engine="2.0L Inline-4 Turbo")
        car36 = Car(make="Land Rover", model="Range Rover Sport", price=65000, year=2021, likes=0, body_style="SUV", engine="3.0L V6 Supercharged")
        car37 = Car(make="Land Rover", model="Range Rover", price=85000, year=2021, likes=0, body_style="SUV", engine="3.0L V6 Supercharged")


        cars = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10,
        car11, car12, car20,
        car21, car22, car23, car24, car25, car26, car27, car28, car29, car30,
        car31, car32, car33, car34, car35, car36, car37]

        """Builds sample user/note(s) data"""
        for car in cars:
            try:
                car.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate car, or error: {car.id}")
                