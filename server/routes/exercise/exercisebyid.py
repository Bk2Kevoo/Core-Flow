from routes.__init__ import Resource, g, db
from models.exercise import Exercise

class ExerciseById(Resource):
    def get(self, id):
        try:
            exercise = Exercise.query.filter_by(id=id).first()
            if exercise:
                return exercise.to_dict(), 200
        except Exception as e:
            return str(e), 400