from flask import request, make_response, session
from models.__init__ import Resource #Api endpoints 
from models.user import User

class Login(Resource):
    def post(self):
        if request.content_type != 'application/json':
            return make_response({"error": "Content-Type must be 'application/json'"}, 400)
        try: 
            # Parse the JSON data
            data = request.get_json()
            # Ensure data is valid
            if not data:
                return make_response({"error": "Invalid JSON data"}, 400) # bad request
            # Find a User by the email AND password if it matches
            user = User.query.filter_by(email=data.get("email", "")).first()
            if user and user.auth(data.get("password", "")):
                session["user_id"] = user.id
                return make_response(user.to_dict(), 200) #OK
            else:
                return make_response({"error": "Try again, Invalid Credentials"}, 401) # Unauthorized
        except Exception as e:
            return make_response({"error": str(e)}, 400)


# Content-Type