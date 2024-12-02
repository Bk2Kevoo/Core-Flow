from routes.__init__ import Resource, g, request, db

class ExerciseById(Resource):
    def get(self, id):
        if g.exercise:
            return g.exercise.to_dict(rules=("workexercise",)), 200
        return {"Message": f"Could not find Exercise with id #{id}"}, 404
    
