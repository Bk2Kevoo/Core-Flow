from flask import request, g, render_template, session
from werkzeug.exceptions import NotFound

from config import app, api, db
from server.models.workout import WorkOuts
from routes.auth.login import Login
from routes.auth.logout import Logout
from routes.auth.signup import Signup
from routes.auth.currentuser import CurrentUser

# General Route Concerns
@app.errorhandler(NotFound)
def not_found(error):
    return{"error": error.description}, 404

@app.before_request
def before_request():
    path_dict = {}
    if request.endpoint in path_dict:
        id = request.view_args.get("id")
        if record := db.session.get(path_dict.get(request.endpoint), id):
            key_name = "workout" if request.endpoint == "workoutbyid" else "categories"
            setattr(g, key_name, record)
        else:
            return {
                "error": f"Could not find a {path_dict.get(request.endpoint).__name__} with id #{id}"
            }, 404



if __name__ == '__main__':
    app.run(port=5555, debug=True)