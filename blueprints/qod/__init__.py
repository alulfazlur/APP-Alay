import requests, config
from blueprints import app
from flask import Blueprint
from flask_restful import Api, reqparse, Resource
from flask_jwt_extended import jwt_required
from datetime import date

bp_qod = Blueprint('qod', __name__)
api = Api(bp_qod)

class QuotesOfTheDay(Resource):
	qod_host = "https://quotes.rest/qod"

	def get(self):
		parser = reqparse.RequestParser()
		parser.add_argument('category', location='args', default=None)
		parser.add_argument('language', location='args', default="en")
		
		args = parser.parse_args()

		rq = requests.get(self.qod_host, params={'category': args['category'], 'language': args['language']})
		qod_req = rq.json()

		# for _ in qod_req:
		qod = {}
		qod['quote'] = qod_req['contents']['quotes'][0]['quote'] 
		qod['author'] = qod_req['contents']['quotes'][0]['author']

		# print(qod)

		return qod, 200, {'Content-Type': 'application/json'}

api.add_resource(QuotesOfTheDay, '')