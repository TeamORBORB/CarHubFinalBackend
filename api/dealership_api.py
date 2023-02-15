from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from __main__ import app, db
from model.dealership_db import Dealership, session

@app.route('/dealerships')
def get_dealerships():
    dealerships = session.query(Dealership).all()
    return jsonify([d.__dict__ for d in dealerships])

@app.route('/dealerships/<int:dealership_id>')
def get_dealership(dealership_id):
    dealership = session.query(Dealership).filter_by(id=dealership_id).one()
    return jsonify(dealership.__dict__)

if __name__ == '__main__':
    app.run()

