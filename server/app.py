# from flask import request, g, render_template, session
from werkzeug.exceptions import NotFound
from models.__init__ import request
from models.category import Category
from config import app, api, db
from routes.workout.workouts import Workouts
from routes.exercise.workexercise import Exercises
from routes.category.category import Categories
from routes.category.categoriesbyid import CategoryByID
from models.user import User
# from models.exercise import Exercise
from routes.auth.login import Login
from routes.auth.logout import Logout
from routes.auth.signup import Signup
from routes.auth.currentuser import CurrentUser

# General Route Concerns
@app.errorhandler(NotFound)
def not_found(error):
    return{"error": error.description}, 404

       

api.add_resource(Workouts, "/workouts")
api.add_resource(Exercises, "/exercises")
api.add_resource(Login, "/login")
api.add_resource(Categories, "/categories")
api.add_resource(CategoryByID, "/categories/<int:id>")

# api.add_resource(Logout, "/logout")
# api.add_resource(Signup, "/signup")
# api.add_resource(WorkoutsByID, "/Workouts")


if __name__ == '__main__':
    app.run(port=5555, debug=True)