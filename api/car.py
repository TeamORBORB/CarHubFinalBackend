from flask import Blueprint, request, jsonify, render_template
import requests
from flask_restful import Api, Resource
from __init__ import app
from model.cars import Car

# Creating a Flask blueprint and API routing
cars_api = Blueprint('cars_api', __name__ ,
                    url_prefix='/api/cars')

# API instance from flask_restful
api = Api(cars_api)

# Post method
class CarsAPI:        
    class _Create(Resource):
        def post(self):
            body = request.get_json()
            
            # validate make
            make = body.get('make')
            if make is None or len(make) < 1:
                return {'message': f'Name is missing, or is less than 1 character'}, 210
            # validate model
            model = body.get('model')
            if model is None or len(model) < 1:
                return {'message': f'Model is missing, or is less than 1 character'}, 210
            # validate price
            price = body.get('price')
            if price is None:
                return {'message': f'Price is missing, or is less than 1 character'}, 210
            # validate year
            year = body.get('year')
            if year is None:
                return {'message': f'Year is missing, or is less than 1 character'}, 210
            # validate likes
            likes = body.get('likes')
            if likes is None:
                return {'message': f'Year is missing, or is less than 1 character'}, 210
            # validate body style
            body_style = body.get('body_style')
            if body_style is None:
                return {'message': f'Year is missing, or is less than 1 character'}, 210
            # validate engine
            engine = body.get('engine')
            if engine is None:
                return {'message': f'Year is missing, or is less than 1 character'}, 210
                    
            car = Car(make=make, model=model, price=price, year=year, likes=likes, body_style=body_style, engine=engine)
            
            # creates the info in the database
            info = car.create()
            # success returns json of user
            if info:
                return jsonify(info.read())
            # failure returns error
            return {'message': f'ERROR'}, 210

    class _Read(Resource):
        def get(self):
            cars = Car.query.all()    # retrieve/extract all cars from database
            json_ready = [info.read() for info in cars]  # prepare output in json
        
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')


