from models.__init__ import SerializerMixin, validates, db

class WorkExercise(db.Model, SerializerMixin):
    __tablename__ = "work_exercises"



    # add relationship
    
    # add serialization rules
    serialize_rules = ('-',)

    #add validations
    

    def __repr__(self):
        return f"<WorkExercise {self.name}>"