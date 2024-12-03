from routes.__init__ import Resource
from models.exercise import Exercise

class Exercises(Resource):
    def get(self):
        try:
            serialized_exercises = [exercise.to_dict() for exercise in Exercise.query]
            return serialized_exercises, 200
        except Exception as e:
            return str(e), 400