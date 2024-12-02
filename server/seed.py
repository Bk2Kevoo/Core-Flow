#!/usr/bin/env python3
from faker import Faker
from config import app
from models.__init__ import db
from models.workout import WorkOut
from models.category import Category
from models.work_exercise import WorkExercise
from models.exercise import Exercise
from models.user import User

fake = Faker()

with app.app_context():
    # Clear existing data
    WorkExercise.query.delete()
    WorkOut.query.delete()
    User.query.delete()
    Exercise.query.delete()
    Category.query.delete()
    db.session.commit()

    # Categories
    cat1 = Category(name="Barbell Workout")
    cat2 = Category(name="Calisthenics")
    cats = [cat1, cat2]

    db.session.add_all(cats)
    db.session.commit()

    # Exercises (linked to categories via category_id)
    ex1 = Exercise(name="Squats", body_part="Legs", category_id=cat1.id)
    ex2 = Exercise(name="Pullups", body_part="Back & Biceps", category_id=cat2.id)
    ex3 = Exercise(name="Pushups", body_part="Chest & Triceps", category_id=cat2.id)
    exercises = [ex1, ex2, ex3]

    db.session.add_all(exercises)
    db.session.commit()

    # User 
    user1 = User(name="Kevin", email="kevin@email.com")
    user1.password = ("password10!!")
    
    db.session.add(user1)
    db.session.commit()

    # Workouts
    workout1 = WorkOut(name="Strength Training", date=fake.date_time_this_month(), user_id=user1.id)
    workout2 = WorkOut(name="Bodyweight Circuit", date=fake.date_time_this_month(), user_id=user1.id)
    workouts = [workout1, workout2]

    db.session.add_all(workouts)
    db.session.commit()

    # Work Exercises (Associating Workouts with Exercises)
    work_ex1 = WorkExercise(
        sets=5,
        reps="10-15",
        weight=225,
        workout_id=workout1.id,
        exercise_id=ex1.id  
    )
    work_ex2 = WorkExercise(
        sets=4,
        reps="10-15",
        weight=0,
        workout_id=workout2.id,
        exercise_id=ex2.id  
    )
    work_ex3 = WorkExercise(
        sets=4,
        reps="30-50",
        weight=0,
        workout_id=workout2.id,
        exercise_id=ex3.id  
    )
    work_exs = [work_ex1, work_ex2, work_ex3]

    db.session.add_all(work_exs)
    db.session.commit()

    print("Seeding done!")
