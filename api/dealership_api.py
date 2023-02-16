from flask import jsonify
from __init__ import app
from model.dealership_db import Dealership, session

@app.route('/dealerships')
def get_dealerships():
    dealerships = session.query(Dealership).all()
    
    response = []
    for d in dealerships:
        # removing some sqlachemy bloat or whatever this is
        del d.__dict__["_sa_instance_state"]
        response.append(d.__dict__)

    return jsonify(response)

@app.route('/dealerships/<int:dealership_id>')
def get_dealership(dealership_id):
    dealership = session.query(Dealership).filter_by(id=dealership_id).one()
    return jsonify(dealership.__dict__)

if __name__ == '__main__':
    app.run()

