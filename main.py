import threading
import requests
# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries

# import "packages" from "this" project
from __init__ import app # Definitions initialization
from model.jokes import initJokes
from model.users import initUsers
from model.cars import initCars

# setup APIs
from api.user import user_api # Blueprint import api definition
from api.car import cars_api
import api.dealership_api

from __init__ import app
from model.dealership_db import Dealership, session

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


@app.route('/cars/')  
def car():
    url = "https://cars.nighthawkcodingsociety.com/api/cars/"

    response = requests.request("GET", url)

    output = response.json()
    return render_template("cars.html", cars=output)

@app.route('/dealership/')  
def ds():
    return render_template("ds.html")

@app.before_first_request
def activate_job():
    initCars()
    initUsers()

from flask import Flask, request, jsonify, render_template
import sqlite3

# @app.route('/comments')
# def handle_comments():
#     comments = fetch_comments()
#     return render_template("comments.html", comments=comments)

# def delete_all_comments():
#     conn = sqlite3.connect('comments.db')
#     c = conn.cursor()
#     c.execute('DELETE FROM comments')
#     conn.commit()
#     conn.close()

@app.route('/comments', methods=['GET', 'POST'])
def handle_comments_post_get():
    if request.method == 'GET':
        comments = fetch_comments()
        return jsonify(comments)
    if request.method == 'POST':
        username = request.form['username']
        comment = request.form['comment']
        insert_comment(username, comment)
        return "Comment added successfully", 201


# def init_db():
#     conn = sqlite3.connect('comments.db')
#     c = conn.cursor()
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS comments (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT NOT NULL,
#             comment TEXT NOT NULL,
#             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#         )
#     ''')
#     conn.commit()
#     conn.close()

# def fetch_comments():
#     conn = sqlite3.connect('comments.db')
#     c = conn.cursor()
#     c.execute('SELECT * FROM comments')
#     comments = c.fetchall()
#     conn.close()
#     return comments

# def insert_comment(username, comment):
#     conn = sqlite3.connect('comments.db')
#     c = conn.cursor()
#     c.execute("INSERT INTO comments (username, comment) VALUES (?, ?)", (username, comment))
#     conn.commit()
#     conn.close()


# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    # init_db()
    from flask_cors import CORS
    cors = CORS(app)
    app.run(debug=True, host="127.0.0.1", port="8055")
