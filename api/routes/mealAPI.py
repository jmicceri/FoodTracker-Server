from flask import Flask
from ..models.meal import Meal
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/roger/data/sqlite/foodtracker.db'
db = SQLAlchemy(app)

class MealAPI(Resource):
	# CRUD calls:
	# CREATE 
	# READ
	# UPDATE
	# DELETE

	def get(self):
		meals = Meal.query.all()
		return meals

	def post(self, Meal):
		args = reqargs[]		meal = Meal()
		db.session.add(meal)
		db.session.commit()
		return jsonify(meals)