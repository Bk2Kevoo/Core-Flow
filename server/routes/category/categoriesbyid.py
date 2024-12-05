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
            if category:= Category.query.get(id):
                if "user_id" in session:
                    current_exer= [exer.to_dict() for exer in category.exercises if session["user_id"] == exer.exercise.user.id]
                    serialized_category = {**category.to_dict(), "exercises": current_exer}
                    return make_response(serialized_category, 200)
                return category.to_dict(), 200
            else:
                return make_response({"error": "Category not found"}, 404)
        except Exception as e:
            return make_response({"error": str(e)}, 500)
