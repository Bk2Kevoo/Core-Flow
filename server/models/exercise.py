from models.__init__ import SerializerMixin, validates, db, re
from models.category import Category

class Exercise(db.Model, SerializerMixin):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    body_part = db.Column(db.String)
    image = db.Column(db.String)
    # workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

    # add relationship
    category = db.relationship('Category', back_populates='exercises')
    work_exercises = db.relationship("WorkExercise", back_populates="exercise")

    # Serialization rules
    serialize_rules = ("-category", "-work_exercises") 

    def __repr__(self):
        return f"""
        <Exercise #{self.id}: 
            Name: {self.name}
            BodyPart: {self.body_part}
            Image: {self.image}
            Category Id: {self.category_id}>
        """
    
@validates("category_id")
def validate_category_id(self, _, category_id):
    if not isinstance(category_id, int):
        raise TypeError("Category ids must be integers")
    elif category_id < 1:
        raise ValueError(
            f"{category_id} has to be a positive integer"
        )
    elif not db.session.get(Category, category_id):
        raise ValueError(f"{category_id} must belong to an existing Category")
    return category_id

@validates("image")
def validate_image(self, _, image):
    if not isinstance(image, str):
        raise TypeError("Images must be strings")
    elif not re.match(r"^https?:\/\/.*\.(?:png|jpeg|jpg)$", image):
        raise ValueError(
            f"{image} has to be a string of a valid url ending in png, jpeg or jpg"
            )
    return image