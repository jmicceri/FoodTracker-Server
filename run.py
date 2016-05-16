from flask import Flask
from api.routes.mealAPI import MealAPI
app = Flask(__name__)

@app.route('/api')
def hello():
	cmd = ''
	return "Hello World"

if __name__ == '__main__':
	app.run()
