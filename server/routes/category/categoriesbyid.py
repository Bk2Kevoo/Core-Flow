from routes.__init__ import Resource, make_response, session
from models.category import Category

# class CategoryByID(Resource):
#     def get(self, id):
#         try:
#             category = Category.query.filter_by(id=id).first()
#             if category:
#                 return make_response({"error":category.to_dict()}, 200)
#         except Exception as e:
#             return make_response({"error": str(e)}, 400)

class CategoryByID(Resource):
    def get(self, id):
        try:
            category = Category.query.get(id)
            if not category:
                return make_response({"error": "Category not found"}, 404)

            if "user_id" in session:
                current_exer = [
                    exer.to_dict() for exer in category.exercises
                    if any(work_exercise.workout.user_id == session["user_id"] for work_exercise in exer.work_exercises)
                ]
                serialized_category = {**category.to_dict(), "exercises": current_exer}
                return make_response(serialized_category, 200)

            # If not logged in, return all exercises in the category
            return make_response(category.to_dict(), 200)

        except Exception as e:
            return make_response({"error": str(e)}, 500)

