from models.__init__ import SerializerMixin, validates, db
from models.workout import WorkOut
from models.category import Category

class Exercise(db.Model, SerializerMixin):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    body_part = db.Column(db.String)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

    # add relationship
    # workout = db.relationship('Workout', back_populates='exercises')
    category = db.relationship('Category', back_populates='exercises')

    # add serialization rules
    serialize_rules = ('-workout.exercises', '-category.exercises')

    def __repr__(self):
        return f"<Exercise #{self.id}: {self.name}, {self.body_part}>"