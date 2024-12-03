from routes.__init__ import Resource, make_response, session

class Delete(Resource):
    def delete(self):
        try:
            response = make_response({}, 204)
            # Remove the user from session if they are logged in
            if "user_id" in session:
                del session["user_id"]
            response.delete_cookie("session")
            return response
        except Exception as e:
            return make_response({"error": str(e)}, 422)