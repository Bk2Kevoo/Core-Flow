from config import app, api, db
from server.models.workout import WorkOuts
from routes.auth.login import Login
from routes.auth.logout import Logout
from routes.auth.signup import Signup
from routes.auth.currentuser import CurrentUser

 # General Route Concerns



if __name__ == '__main__':
    app.run(port=5555, debug=True)