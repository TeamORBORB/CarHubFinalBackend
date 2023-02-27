# contact me before changing any of this code

from __init__ import app 
from flask import jsonify, request
from flask import Flask
from model.dealership_db import Dealership, session
from sqlalchemy import create_engine, engine_from_config


print("Connecting to database...")

@app.route('/dealerships')
def get_dealerships():
    
    dealerships = session.query(Dealership).all()

    response = []
    for d in dealerships:
        try:
            del d.__dict__["_sa_instance_state"]
        except:
            pass
        response.append(d.__dict__)

    return jsonify(response)

@app.route('/dealerships', methods=['POST'])
def submit():
    data = request.json
    name = data.get('name')
    address = data.get('address')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if not all([name, address, latitude, longitude]):
        return jsonify({'error': 'Missing data'})

    dealership = Dealership(name=name, address=address, latitude=latitude, longitude=longitude)
    session.add(dealership)
    session.commit()

    return 'Data inserted successfully'

if __name__ == '__main__':
    app.run()
