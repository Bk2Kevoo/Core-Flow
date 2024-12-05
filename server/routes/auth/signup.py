# routes/signup.py
from routes.__init__ import Resource, request, db, make_response, session
from models.user import User
from sqlalchemy.exc import IntegrityError
from routes.user.initialize import UserInitializer  # Import the UserInitializer class

class Signup(Resource):
    def post(self):
        try:
            data = request.json
            email = data.get("email")
            name = data.get("name")
            password = data.get("password")
            if not email or not name or not password:
                return make_response({"error": "Email, name, and password are required."}, 400)
            # Create the new user
            user = User(email=email, name=name)
            user.password = password  # You may want to hash the password before saving
            # Add the user to the database
            db.session.add(user)
            db.session.commit()
            # Initialize user with default workouts and exercises
            user_initializer = UserInitializer(user.id)
            initialization_result = user_initializer.initialize()
            session["user_id"] = user.id
            # Return the user data along with initialization result
            return make_response({
                "message": f"Welcome {user.name}, you now have some Workouts have fun!",
                **user.to_dict(), 
                "initialization_message": initialization_result["message"]
            }, 201)  # Created
        except IntegrityError as e:
            # Handle database integrity errors (e.g., duplicate email)
            return make_response({"error": str(e.orig)}, 422)
        except Exception as e:
            # Handle other errors
            return make_response({"error": str(e)}, 422)  # Unprocessable Entity
