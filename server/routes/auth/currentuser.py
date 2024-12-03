from routes.__init__ import Resource, request, db, make_response, session
from models.user import User

class CurrentUser(Resource):
    def get(self):
        try:
            if "user_id" in session:
                if user := db.session.get(User, session["user_id"]):
                    return make_response(user.to_dict(), 200)
                del session["user_id"]
                return make_response({"error": "user_id in session does not exist, it has been removed"}, 400)
            return make_response({"error": "Please Login!"}, 401)
        except Exception as e:
            return make_response({"error": str(e)}, 422)
