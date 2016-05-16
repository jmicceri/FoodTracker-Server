import flask import Flask
import flask_sqlalchemy import SQLAlchemy
import flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foodtracker.db'
db = SQLAlchemy(app)

class Meal(db.Model):
	__tablename__ = 'Meal'
	name = Column(String(50))
	photo = Column(String(50))
	rating = Column(Integer)


	def __init__(self, name=None, photo=None, rating=None)
		self.name = name
		self.photo = photo
		self.rating = rating

