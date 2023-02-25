from flask import jsonify, request
from __init__ import app
from model.dealership_db import Dealership, session
from sqlalchemy import create_engine


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


# @app.route('/dealership_submit', methods=['POST'])
# def submit():
    name = request.form['name']
    address = request.form['address']
    latitude = float(request.form['latitude'])
    longitude = float(request.form['longitude'])

    conn = engine.connect()
    ins = dealership_table.insert().values(name=name, address=address, latitude=latitude, longitude=longitude)
    conn.execute(ins)

    return 'Data inserted successfully'

#if __name__ == '__main__':
    app.run()