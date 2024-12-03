from routes.__init__ import Resource, request, db, make_response, session, g
from models.user import User
# from flask_restful import reqparse

class CurrentUser(Resource):
    def get(self, id):
        try:
            if "user_id" in session:
                if user := db.session.get(User, session["user_id"]):
                    return make_response(user.to_dict(), 200)
                del session["user_id"]
                return make_response({"error": "user_id in session does not exist, it has been removed"}, 400)
            return make_response({"error": "Please Login!"}, 401)
        except Exception as e:
            return make_response({"error": str(e)}, 422)
    
    def patch(self, id):
        try:
            if not g.current:
                return make_response({"error": "User not found"}, 404)
            
            # Parse request data
            data = request.get_json()

            # Update user attributes only if provided
            for attr, value in data.items():
                if hasattr(g.current, attr):
                    setattr(g.current, attr, value)
                else:
                    return make_response({"error": f"Invalid attribute: {attr}"}, 400)

            db.session.commit()

            # Return the updated user data
            return make_response(g.current.to_dict(rules=("user",)), 202)

        except Exception as e:
            return {"error": str(e)}, 422
