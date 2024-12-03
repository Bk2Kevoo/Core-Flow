from models.__init__ import SerializerMixin,db, validates
from models.user import User
from models.work_exercise import WorkExercise 

class WorkOut(db.Model, SerializerMixin):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # Relationship to User
    user = db.relationship("User", back_populates="work_outs")

    # Relationship to WorkExercise
    work_exercises = db.relationship("WorkExercise", back_populates="workout")

    serialize_rules = ("-user", "-work_exercises")

    def __repr__(self):
        return f"""
            Workout #{self.id}:
                Name: {self.name}
                Date: {self.date}
                User Id: {self.user_id}
        """
    
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "date": self.date,
            "user_id": self.user_id
        }


@validates("user_id")
def validate_user_id(self, _, user_id):
    if not isinstance(user_id, int):
        raise TypeError("User ids must be integers")
    elif user_id < 1:
        raise ValueError(
            f"{user_id} has to be a positive integer"
        )
    elif not db.session.get(User, user_id):
        raise ValueError(f"{user_id} must belong to an existing User")
    return user_id
     