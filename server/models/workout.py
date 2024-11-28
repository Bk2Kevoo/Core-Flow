from models.__init__ import SerializerMixin, validates, db

class Workout(db.Model, SerializerMixin):
    __tablename__ = "workouts"



    # add relationship
    
    # add serialization rules
    serialize_rules = ('-',)

    #add validations
    

    def __repr__(self):
        return f"<Workout {self.name}>"