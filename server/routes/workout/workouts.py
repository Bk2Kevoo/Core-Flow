from routes.__init__ import Resource, make_response
from models.workout import WorkOut

class Workouts(Resource):
    def get(self):
        try:
            # Querying all workouts from the WorkOut model
            serialized_workouts = [workout.as_dict() for workout in WorkOut.query]
            return make_response(serialized_workouts, 200)
        except Exception as e:
            return {"error": str(e)}, 500
