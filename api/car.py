from flask import Blueprint, request, jsonify, render_template
import requests
from flask_restful import Api, Resource
from __init__ import app, db
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
            # validate description
            desc = body.get('desc')
            if desc is None or len(desc) < 1:
                return {'message': f'Description is missing, or is less than 1 character'}, 210
            # validate body style
            body_style = body.get('body_style')
            if body_style is None or len(body_style) < 1:
                return {'message': f'Body style is missing, or is less than 1 character'}, 210
            # validate engine
            engine = body.get('engine')
            if engine is None or len(engine) < 1:
                return {'message': f'Engine is missing, or is less than 1 character'}, 210
            # validate engine
            owner = body.get('owner')
            if owner is None or len(owner) < 1:
                return {'message': f'Owner is missing, or is less than 1 character'}, 210

            desc = body.get('desc')
            if desc is not None and len(desc) > 0:
                existing_desc = Car.query.filter_by(desc=desc).first()
                if existing_desc is not None:
                    return {'message': f'A car with the same description already exists'}, 400

            car = Car(make=make, model=model, price=price, year=year, desc=desc, body_style=body_style, engine=engine, owner=owner)

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

    class _Update(Resource):
        def put(self, id):
            car = Car.query.get(id)
            if car is None:
                return {'message': f'Car with ID {id} not found'}, 404
            
            body = request.get_json()
            
            # update the car object with new values
            car.make = body.get('make', car.make)
            car.model = body.get('model', car.model)
            car.price = body.get('price', car.price)
            car.year = body.get('year', car.year)
            car.body_style = body.get('body_style', car.body_style)
            car.engine = body.get('engine', car.engine)
            car.owner = body.get('owner', car.owner)
            
            # save the updated car object
            car.update()
            
            # return the updated car object as JSON
            return jsonify(car.read())
            

    class _Delete(Resource):
        def delete(self, id):
            # Retrieve the Car object with the given ID from the database
            car = Car.query.get(id)
            
            # Check if the Car object exists
            if car:
                # If it exists, delete it from the database
                car.delete()
                # Return a success message along with a 200 status code
                return {'message': f'Car with the ID {id} has been removed'}, 200
            else:
                # If the Car object doesn't exist, return a 404 status code along with an error message
                return {'message': f'Car with the ID {id} not found'}, 404


    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    #api.add_resource(_Update, '/update/<int:id>')
    api.add_resource(_Delete, '/delete/<int:id>')


