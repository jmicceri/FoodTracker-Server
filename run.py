from flask import Flask
from flask_restful import Api
from api.routes.mealAPI import MealAPI
from api.models.meal import Meal

app = Flask(__name__, static_url_path="")
api = Api(app)

########### Start API Routes #################
from api.routes.mealAPI import MealAPI
api.add_resource(MealAPI, '/foodtracker/api/meal', endpoint='meal')
################# END ########################

if __name__ == '__main__':
	app.run(debug=True)