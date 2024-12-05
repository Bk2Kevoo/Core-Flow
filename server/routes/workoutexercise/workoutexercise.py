from routes.__init__ import Resource, make_response, session, db
from flask import jsonify
from models.workout import WorkOut
from models.work_exercise import WorkExercise

class WorkOutExercise(Resource):
    def get(self, workout_id=None):
        try:
            # Check if the user is logged in
            user_id = session.get("user_id")
            if not user_id:
                return {"error": "User not logged in"}, 401

            # If a workout_id is provided, filter by it
            if workout_id:
                # Query the exercises for a specific workout
                workout_exercises = (
                    db.session.query(WorkExercise)
                    .join(WorkOut, WorkOut.id == WorkExercise.workout_id)
                    .filter(WorkOut.id == workout_id, WorkOut.user_id == user_id)
                    .all()
                )

                if not workout_exercises:
                    return make_response({"message": "No exercises found for this workout"}, 404)

                # Serialize the data
                exercises_data = [
                    {
                        "id": we.id,
                        "sets": we.sets,
                        "reps": we.reps,
                        "weight": we.weight,
                        "exercise_id": we.exercise_id,
                        "exercise_name": we.exercise.name if we.exercise else None,
                    }
                    for we in workout_exercises
                ]

                return jsonify(exercises_data)

            # If no workout_id is provided, return all workouts for the user
            workout_exercises = (
                db.session.query(WorkExercise)
                .join(WorkOut, WorkOut.id == WorkExercise.workout_id)
                .filter(WorkOut.user_id == user_id)
                .all()
            )

            if not workout_exercises:
                return {"message": "No workout exercises found"}, 200

            # Serialize all workout exercises
            data = [
                {
                    "id": we.id,
                    "sets": we.sets,
                    "reps": we.reps,
                    "weight": we.weight,
                    "workout_id": we.workout_id,
                    "exercise_id": we.exercise_id,
                    "exercise_name": we.exercise.name if we.exercise else None,
                    "workout_name": we.workout.name if we.workout else None,
                }
                # the "we" stands for workout exercise
                for we in workout_exercises
            ]

            return jsonify(data)
        except Exception as e:
            # Handle exceptions and return an appropriate error response
            return make_response({"error": str(e)}), 500