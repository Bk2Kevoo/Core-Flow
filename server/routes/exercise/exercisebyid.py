from routes.__init__ import Resource, make_response
from models.exercise import Exercise

class ExerciseById(Resource):
    def get(self, id):
        try:
            exercise = Exercise.query.filter_by(id=id).first()
            if exercise:
                return exercise.to_dict(), 200
        except Exception as e:
            return make_response({"error": str(e)}, 400)