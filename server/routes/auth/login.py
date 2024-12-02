from routes.__init__ import Resource, request, db, make_response, session
from models.user import User

class Login(Resource):
    def post(self):
        try:
            data = request.json
            # Find a User by the email AND password if it matches
            user = User.query.filter_by(email=data.get("email", "")).first()
            if user and user.authenticate(data.get("password", "")):

                #If it is successfull then login the user
                session["user_id"] = user.id
                return make_response(user.to_dict(), 200)
            else:
                return make_response({"error": "Try again, Invalid Credentials"}, 401)
        except Exception as e:
            return make_response({"error": str(e)}, 400)