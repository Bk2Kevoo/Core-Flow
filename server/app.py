from werkzeug.exceptions import NotFound
from flask import render_template
from config import app, api
from routes.workout.workouts import Workouts
from routes.exercise.exercise import Exercises
from routes.category.category import Categories

from routes.category.categoriesbyid import CategoryByID
from routes.exercise.exercisebyid import ExerciseById
from routes.workout.workoutbyid import WorkoutById
from routes.workoutexercise.workoutexercisebyid import WorkExerciseById
from routes.workoutexercise.workoutexercise import WorkOutExercise



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
api.add_resource(WorkoutById, "/workouts/<int:id>")

api.add_resource(Exercises, "/exercises")
api.add_resource(ExerciseById, "/exercises/<int:id>")

api.add_resource(Categories, "/categories")
api.add_resource(CategoryByID, "/categories/<int:id>")

api.add_resource(WorkOutExercise, '/workout-exercises')
api.add_resource(WorkExerciseById, '/workout-exercises/<int:id>')

api.add_resource(Login, "/login")
api.add_resource(Logout, "/logout")
api.add_resource(CurrentUser, "/current-user")
api.add_resource(Signup, "/signup")
api.add_resource(EditUser, "/edit")
api.add_resource(Delete, "/delete-account")



if __name__ == '__main__':
    app.run(port=5555, debug=True)