import threading
import requests
# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries

# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from model.jokes import initJokes
from model.users import initUsers
from model.cars import initCars

# setup APIs
from api.user import user_api # Blueprint import api definition
from api.car import cars_api

# register URIs
# app.register_blueprint(joke_api) # register api routes
app.register_blueprint(user_api) # register api routes

app.register_blueprint(cars_api)

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

# @app.route('/carID/<int:id>')
# def car_ID(id):
#     # Make a GET request to the car ID API endpoint, allowing the data of a specific car to be retrieved
#     response = requests.get(f'http://192.168.1.23:8049/api/cars/car/{id}')
#     # Parse the JSON response
#     car_data = response.json()
#     # Render the car ID in a template


@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("stub.html")


@app.before_first_request
def activate_job():
    initJokes()
    initUsers()
    initCars()

# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volumes/sqlite.db'
    app.run(debug=True, host="127.0.0.1", port="8091")
