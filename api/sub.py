from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.subs import Sub

user_api = Blueprint('sub_api', __name__,
                   url_prefix='/api/subs')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(subs_api)

class SubsAPI:        
    class _Create(Resource):
        def post(self):
            body = request.get_json()
            sbs = body.get('sbs')
            if sbs is None or len(sbs) < 2:
                return {'message': f'Subscriber is missing, or is less than 2 characters'}, 210
            uo = Sub(sbs=sbs)
            sub = uo.create()
            if sub:
                return jsonify(sub.read())
            # failure returns error
            return {'message': f'User ID {sbs} is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            users = Sub.query.all() 
            json_ready = [sub.read() for sub in subs] 
            return jsonify(json_ready)
    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')