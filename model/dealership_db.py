# contact me before changing any of this code


from sqlalchemy import create_engine, Column, Integer, String, Floatl
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from __init__ import db 
from sqlalchemy.exc import IntegrityError


class Dealership(db.Model):
    __tablename__ = 'dealership'
    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String)
    _address = db.Column(db.String, primary_key=True)
    _latitude = db.Column(db.Float)
    _longitude = db.Column(db.Float)

    def __init__(self, name, address, latitude, longitude ):
        self._name = name    
        self._address = address
        self._latitude = latitude
        self._longitude = longitude


# name setter
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

# address setter
    @property
    def address(self):
        return self._address
    
    @address.setter
    def name(self, address):
        self._address = address

# latitude setter
    @property
    def latitude(self):
        return self._latitude
    
    @latitude.setter
    def latitude(self, latitude):
        self._latitude = latitude

# longitude  setter
    @property
    def longitude(self):
        return self._longitude
    
    @longitude.setter
    def longitude(self, longitude):
        self._longitude = longitude


    # output content using str(object) is in human readable form
    # output content using json dumps, this is ready for API response
    def __str__(self):
        return json.dumps(self.read())

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
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
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None    

    def __repr__(self):
        return f'<name {self.name}>'

db.drop_all()
db.create_all()
session = db.session

dealership1 = Dealership(name='RB Carco - Auto Buying', address='11639 Iberia Pl, San Diego, CA 92128', latitude=33.015500, longitude=-117.078660)
dealership2 = Dealership(name='Interstate Auto Buyers', address='16644 W Bernardo Dr #452, San Diego, CA 92127', latitude=33.015202, longitude=117.083382)
dealership3 = Dealership(name='Rancho Santa Fe Autos', address='16077 San Dieguito Rd #3311, Rancho Santa Fe, CA 92067', latitude=32.990768, longitude=-117.196480)
dealership4 = Dealership(name='Aaron Ford of Poway', address='12740 Poway Rd, Poway, CA 92064', latitude=32.956190, longitude=117.055360)
dealership5 = Dealership(name='Pedder Hyundai of Poway', address='13910 Poway Rd, Poway, CA 92064', latitude=32.9563814, longitude=117.0297427)
dealership6 = Dealership(name='Mossy Nissan Poway', address='14100 Poway Road, Padre Woods, Poway, CA 92064', latitude=32.956937, longitude=-117.026533)
dealership7 = Dealership(name='Carco Of Poway', address='12538 Poway Rd, Poway, CA 92064', latitude=32.9529165, longitude=-117.0591852)


dealerships = [dealership1, dealership2, dealership3, dealership4, dealership5, dealership6, dealership7]

session.add(dealerships)


session.commit()
