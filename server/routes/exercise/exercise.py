from routes.__init__ import Resource, make_response
from models.exercise import Exercise

class Exercises(Resource):
    def get(self):
        try:
            serialized_exercises = [exercise.to_dict() for exercise in Exercise.query]
            return make_response(serialized_exercises, 200)
        except Exception as e:
            return make_response({"error": str(e)}, 400)