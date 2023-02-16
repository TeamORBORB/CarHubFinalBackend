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

if __name__ == '__main__':
    app.run()

