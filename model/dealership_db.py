from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from __init__ import db

class Dealership(db.Model):
    __tablename__ = 'dealership'
    #id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)


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


session.add(dealership1)
session.add(dealership2)
session.add(dealership3)
session.add(dealership4)
session.add(dealership5)
session.add(dealership6)
session.add(dealership7)

session.commit()
