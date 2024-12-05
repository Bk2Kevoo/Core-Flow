from models.__init__ import SerializerMixin, validates, db
from models.category import Category

class Exercise(db.Model, SerializerMixin):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    body_part = db.Column(db.String)
    # image_url = db.Column(db.String, nullable=True)
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
            Category Id: {self.category_id}>
        """
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "body_part": self.body_part,
            # "image_url": self.image_url 
        }

    
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
