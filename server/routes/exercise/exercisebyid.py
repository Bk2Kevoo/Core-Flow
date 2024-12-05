from routes.__init__ import Resource, make_response, session
from models.exercise import Exercise

class ExerciseById(Resource):
    def get(self, id):
        try:
            if exercise:= Exercise.query.get(id):
                if "user_id" in session:
                    current_work = [we.to_dict() for we in exercise.work_exercises if session["user_id"] == we.workout.user.id]
                    serialized_exercise = {**exercise.to_dict(), "work_exercises": current_work}
                    return make_response(serialized_exercise, 200)
                return exercise.to_dict(), 200
            else:
                return make_response({"error": "Exercise not found"}, 404)
        except Exception as e:
            return make_response({"error": str(e)}, 500)