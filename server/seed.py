# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from config import app
from models.__init__ import db
from models.category import Category
from models.exercise import Exercise
from models.workexercise import WorkExercise
from models.workout import Workout

fake = Faker()
with app.app_context():
    print("Starting seed...")
    # Seed code goes here!
    Category.query.delete()
    Exercise.query.delete()
    WorkExercise.query.delete()
    Workout.query.delete()

    #Workouts
    workout1 = Workout(name="Leg Day")
    workout2 = Workout(name="Push Day")
    workout3 = Workout(name="Pull Day")
    workouts = [workout1, workout2, workout3]

    #WorkExercises
    work_ex1 = WorkExercise(
        sets="5"
        reps="10-15"
        weight="225 lbs."
    )
    work_ex2 = WorkExercise(
        sets="4"
        reps="10-15"
        weight="Bodyweight"
    )
    work_ex3 = WorkExercise(
        sets="4"
        reps="30-50"
        weight="Bodyweight"
    )
    work_exs = [work_ex1, work_ex2, work_ex3]

    #Exercises
    ex1 = (
        name="Squats"
        body_part="Legs"
    )
    ex2 = (
        name="Pullups"
        body_part="Back & Biceps"
    )
    ex3 = (
            name="Pushups"
            body_part="Chest & Triceps"
        )
    exs = [ex1, ex2, ex3]


    #Categories
    cat1 = Category(name="Barbell Workout")
    cat2 = Category(name="Calisthenics")
    cat3 = Category(name="Calisthenics")
    cats = [cat1, cat2, cat3]


    #Commit all instances to db
    db.session.add_all(workouts)
    db.session.add_all(work_exs)
    db.session.add_all(exs)
    db.session.add_all(cats)
    db.session.commit()

    print("Seeding done!")