from flask import Flask
from models.meal import Meal
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foodtracker.db'
db = SQLAlchemy(app)

class MealAPI(Resource):
	def get(Meal):
		print("Requesting Meals")
		meals = Meal.query.all()
		return jsonify(meals)

	def post(self, Meal):
		meal = Meal()
		db.session.add(meal)
		db.session.commit()
		meals = Meal.query.all()
		return jsonify(meals)

#api.add_resource(MealRoute, '/foodtracker/api/meal', endpoint='meal')