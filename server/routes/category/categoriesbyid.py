from routes.__init__ import Resource, make_response
from models.category import Category

class CategoryByID(Resource):
    def get(self, id):
        try:
            category = Category.query.filter_by(id=id).first()
            if category:
                return make_response({"error":category.to_dict()}, 200)
        except Exception as e:
            return make_response({"error": str(e)}, 400)