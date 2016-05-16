import flask import Flask
import flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foodtracker.db'
db = SQLAlchemy(app)

