from routes.__init__ import Resource, make_response
from models.workout import WorkOut

class WorkoutById(Resource):
    def get(self, id):
        try:
            workout = WorkOut.query.filter_by(id=id).first()
            if workout:
                return workout.to_dict(), 200
        except Exception as e:
            return make_response({"error": str(e)}, 400)