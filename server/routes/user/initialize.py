from models.workout import WorkOut
from models.work_exercise import WorkExercise
from models.user import User
from models.exercise import Exercise
from models.__init__ import db

class UserInitializer:
    def __init__(self, user_id):
        self.user_id = user_id

    def initialize(self):
        """Initialize a new user with default workouts and exercises."""
        # Fetch the user from the database
        user = db.session.query(User).filter_by(id=self.user_id).first()
        if not user:
            raise ValueError("User not found")
        # Add default workouts for the new user
        self._add_default_workouts(user)
        # Add exercises to the workouts
        self._add_exercises_to_workouts()
        return {"message": "User initialized with default workouts and exercises."}

    def _add_default_workouts(self, user):
        """Create and add default workouts for the user."""
        default_workouts = [
            WorkOut(name="Beginner Full Body", user_id=user.id),
            WorkOut(name="Cardio Session", user_id=user.id),
        ]
        db.session.bulk_save_objects(default_workouts)
        db.session.commit()

    def _add_exercises_to_workouts(self):
        """Assign exercises to the created workouts."""
        exercises = db.session.query(Exercise).all()
        workouts = db.session.query(WorkOut).filter_by(user_id=self.user_id).all()
        if not workouts:
            raise ValueError("No workouts found for user")
        for workout in workouts:
            for exercise in exercises:
                work_exercise = WorkExercise(
                    sets=3,
                    reps="10-15",
                    weight=20,  # You can randomize this or add logic
                    workout_id=workout.id,
                    exercise_id=exercise.id
                )
                db.session.add(work_exercise)

        db.session.commit()

