from routes.__init__ import Resource, make_response
from models.work_exercise import WorkExercise

class WorkExerciseById(Resource):
    def get(self, id):
        try:
            work = WorkExercise.query.filter_by(id=id).first()
            if work:
                return work.to_dict(), 200
        except Exception as e:
            return make_response({"error": str(e)}, 400)