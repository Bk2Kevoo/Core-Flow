from models.__init__ import SerializerMixin, validates, db
from models.workout import WorkOut
from models.exercise import Exercise

class WorkExercise(db.Model, SerializerMixin):
    __tablename__ = "work_exercises"

    id = db.Column(db.Integer, primary_key=True)
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.String)
    weight = db.Column(db.Float, nullable=True)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"))
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"))

    # Relationship to WorkOut
    workout = db.relationship("WorkOut", back_populates="work_exercises")

    # Relationship to Exercise
    exercise = db.relationship("Exercise", back_populates="work_exercises")
    
    serialize_rules = ("-workout.work_exercises", "-exercise.work_exercises",)

    def __repr__(self):
        return f"""
            <WorkExercise #{self.id}:
                Sets: {self.sets}
                Reps: {self.reps}
                Weight: {self.weight}
                Workout Id: {self.workout_id}
                Exercise Id: {self.exercise_id}>
        """

    @validates("workout_id")
    def validate_workout_id(self, _, workout_id):
        if not isinstance(workout_id, int):
            raise TypeError("Workout ids must be integers")
        elif workout_id < 1:
            raise ValueError(
                f"{workout_id} has to be a positive integer"
            )
        elif not db.session.get(WorkOut, workout_id):
            raise ValueError(f"{workout_id} must belong to an existing WorkOut")
        return workout_id
        
    @validates("exercise_id")
    def validate_exercise_id(self, _, exercise_id):
        if not isinstance(exercise_id, int):
            raise TypeError("Exercise ids must be integers")
        elif exercise_id < 1:
            raise ValueError(
                f"{exercise_id} has to be a positive integer"
            )
        elif not db.session.get(Exercise, exercise_id):
            raise ValueError(f"{exercise_id} must belong to an existing Exercise") 
        return exercise_id





