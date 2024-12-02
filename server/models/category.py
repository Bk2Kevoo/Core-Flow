from models.__init__ import SerializerMixin, validates, re, db

class Category(db.Model, SerializerMixin):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    # Relationship
    exercises = db.relationship('Exercise', back_populates='category')


    def __repr__(self):
        return f'<Category {self.id}: {self.name}>'

    @validates("name")
    def validate_name(self, _, value):
        if not value:
            raise ValueError("name must be present")
        if len(value) < 3:
            raise ValueError("name must be at least 3 characters long")
        return value
