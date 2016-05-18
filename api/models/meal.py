from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/roger/data/sqlite/foodtracker.db'
db = SQLAlchemy(app)

class Meal(db.Model):
	__tablename__ = 'Meal'
	_id = db.Column(Integer, primary_key=True)
	name = db.Column(String(50))
	photo = db.Column(String(50))
	rating = db.Column(Integer)


	def __init__(self, name=None, photo=None, rating=None):
		self.name = name
		self.photo = photo
		self.rating = rating

	def __repr__(self):
		return '<Meal %r>' % self.Meal