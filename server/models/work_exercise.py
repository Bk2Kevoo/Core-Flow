from models.__init__ import SerializerMixin, validates, re, db

class WorkExercise(db.Model, SerializerMixin):
    __tablename__ = "work_exercises"

    id = db.Column(db.Integer, primary_key=True)
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.String)
    weight = db.Column(db.Float, nullable=True)
    # we are doing it of type string in case our formating 
    duration = db.Column(db.String)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id", name="fk_work_exercises_to_workouts"))
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id", name="fk_work_exercises_to_exercises"))

    def __repr__(self):
        return 


@validates("workout_id")
def validate_workout_id
