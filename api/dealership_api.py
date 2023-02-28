# contact me before changing any of this code

from __init__ import app 
from flask import jsonify, request
from flask import Flask
from model.dealership_db import Dealership, session
from sqlalchemy import create_engine, engine_from_config
import sqlalchemy


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
    #print(data)
    name = data.get('name')
    address = data.get('address')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if not all([name, address, latitude, longitude]):
        return jsonify({'message': 'Missing data', "message_type": "error"})

    dealership = Dealership(name=name, address=address, latitude=latitude, longitude=longitude)

    try:
        session.add(dealership)
        session.commit()
    except sqlalchemy.exc.IntegrityError:
        return jsonify({"message": "Address already exists", "message_type": "error"})

    return jsonify({"message": 'Data inserted successfully', "message_type": "success"})

if __name__ == '__main__':
    app.run()
