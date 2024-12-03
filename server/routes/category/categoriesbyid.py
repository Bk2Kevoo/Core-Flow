from routes.__init__ import Resource, request, db, g
from models.category import Category

class CategoryByID(Resource):
    
    def get(self, id):
        try:
            category = Category.query.filter_by(id=id).first()
            if category:
                return category.to_dict(), 200
        except Exception as e:
            return str(e), 400