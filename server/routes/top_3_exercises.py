# Create a route that will RETRIEVE the top three exercises based on the count of how many times they appear in WORKOUTEXERCISE
from models.__init__ import Resource
from models.work_exercise import WorkExercise
from models.exercise import Exercise
from __init__ import make_response

class ExerciseTop(Resource):
    def get(self):
        try:
            top_3_exercises = WorkExercise.query.filter([exercise.to_dict() for exercise in WorkExercise.query])
            
            if top_3_exercises:
                return make_response({"error": "Can not find whe top 3"}, 400)
        except Exception as e:
            return make_response({"error": str(e)}, 400)


# class TopThreeProductionsByCrewMemberCount(Resource):
#     def get(self):
#         try:
#             # all_productions = Production.query.all()
#             # sorted_productions = sorted(all_productions, key=lambda production: len(production.crew_members), reverse=True)
#             # return make_response([prod.to_dict() for prod in sorted_productions[:3]], 200)
#             top_three_productions = db.session.query(
#                 Production, db.func.count(CrewMember.id).label("crew_member_count")
#             ).join(CrewMember, Production.id == CrewMember.production_id).group_by(Production.id).order_by(crew_member_count.desc()).limit(3)
#             return make_response([{production: prod.to_dict(), "count": count} for prod, count in top_three_productions], 200)
#         except Exception as e:
#             return {"error": str(e)}, 500

# api.add_resource(TopThreeProductionsByCrewMemberCount, "/productions/top-three-most-crew-members")