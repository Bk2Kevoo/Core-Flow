# from flask import request, g, render_template, session
from werkzeug.exceptions import NotFound
from config import app, api
from routes.workout.workouts import Workouts
from routes.exercise.exercise import Exercises
from routes.category.category import Categories
from routes.category.categoriesbyid import CategoryByID
from routes.exercise.exercisebyid import ExerciseById
from models.user import User
# from models.exercise import Exercise
from routes.auth.login import Login
from routes.auth.logout import Logout
from routes.auth.signup import Signup
from routes.auth.currentuser import CurrentUser
from routes.user.edit import EditUser
from routes.user.delete import Delete

# General Route Concerns
@app.errorhandler(NotFound)
def not_found(error):
    return{"error": error.description}, 404

       

api.add_resource(Workouts, "/workouts")
api.add_resource(Exercises, "/exercises")
api.add_resource(Categories, "/categories")
api.add_resource(CategoryByID, "/categories/<int:id>")
api.add_resource(ExerciseById, "/exercises/<int:id>")
api.add_resource(Login, "/login")
api.add_resource(Logout, "/logout")
api.add_resource(CurrentUser, "/current-user")
api.add_resource(Signup, "/signup")
api.add_resource(EditUser, "/edit")
api.add_resource(Delete, "/user/delete")



if __name__ == '__main__':
    app.run(port=5555, debug=True)