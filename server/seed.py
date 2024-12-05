from faker import Faker
from config import app
from models.__init__ import db
from models.workout import WorkOut
from models.category import Category
from models.work_exercise import WorkExercise
from models.exercise import Exercise
from models.user import User 

fake = Faker()

# A list of more realistic categories
categories = [
    "Arms", "Legs", "Quads", "Back", "Chest", "Shoulders", "Core", "Cardio", "Full Body", "Calisthenics"
]

# A list of exercises corresponding to categories
exercises_data = {
    "Arms": ["Dumbbell Skull Crusher", "Bicep Curls", "Tricep Dips", "Hammer Curls"],
    "Legs": ["Barbell Squats", "Lunges", "Leg Press", "Calf Raises", "Romanian Deadlift"],
    "Quads": ["Front Squats", "Leg Extensions", "Bulgarian Split Squats", "Step Ups"],
    "Back": ["Deadlifts", "Pull Ups", "Lat Pulldowns", "Barbell Rows", "T-Bar Row"],
    "Chest": ["Bench Press", "Push Ups", "Chest Flys", "Incline Dumbbell Press"],
    "Shoulders": ["Overhead Press", "Lateral Raises", "Front Raises", "Arnold Press"],
    "Core": ["Plank", "Russian Twists", "Leg Raises", "Mountain Climbers"],
    "Cardio": ["Treadmill Running", "Jump Rope", "Cycling", "Rowing Machine", "HIIT"],
    "Full Body": ["Kettlebell Swings", "Clean and Press", "Burpees", "Thrusters"],
    "Calisthenics": ["Push Ups", "Pull Ups", "Dips", "Muscle-Ups", "Handstands"]
}

# Map exercises to their image URLs (you can use the appropriate file paths or URLs)
# exercise_images = {
#     "Dumbbell Skull Crusher": "/images/dumbbell_skull_crusher.jpg",
#     "Bicep Curls": "/images/bicep_curls.jpg",
#     "Tricep Dips": "/images/tricep_dips.jpg",
#     "Hammer Curls": "/images/hammer_curls.jpg",
#     "Barbell Squats": "/images/barbell_squats.jpg",
#     "Lunges": "/images/lunges.jpg",
#     "Leg Press": "/images/leg_press.jpg",
#     "Calf Raises": "/images/calf_raises.jpg",
#     "Romanian Deadlift": "/images/romanian_deadlift.jpg",
#     "Front Squats": "/images/front_squats.jpg",
#     "Leg Extensions": "/images/leg_extensions.jpg",
#     "Bulgarian Split Squats": "/images/bulgarian_split_squats.jpg",
#     "Step Ups": "/images/step_ups.jpg",
#     "Deadlifts": "/images/deadlifts.jpg",
#     "Pull Ups": "/images/pull_ups.jpg",
#     "Lat Pulldowns": "/images/lat_pulldowns.jpg",
#     "Barbell Rows": "/images/barbell_rows.jpg",
#     "T-Bar Row": "/images/t_bar_row.jpg",
#     "Bench Press": "/images/bench_press.jpg",
#     "Push Ups": "/images/push_ups.jpg",
#     "Chest Flys": "/images/chest_flys.jpg",
#     "Incline Dumbbell Press": "/images/incline_dumbbell_press.jpg",
#     "Overhead Press": "/images/overhead_press.jpg",
#     "Lateral Raises": "/images/lateral_raises.jpg",
#     "Front Raises": "/images/front_raises.jpg",
#     "Arnold Press": "/images/arnold_press.jpg",
#     "Plank": "/images/plank.jpg",
#     "Russian Twists": "/images/russian_twists.jpg",
#     "Leg Raises": "/images/leg_raises.jpg",
#     "Mountain Climbers": "/images/mountain_climbers.jpg",
#     "Treadmill Running": "/images/treadmill_running.jpg",
#     "Jump Rope": "/images/jump_rope.jpg",
#     "Cycling": "/images/cycling.jpg",
#     "Rowing Machine": "/images/rowing_machine.jpg",
#     "HIIT": "/images/hiit.jpg",
#     "Kettlebell Swings": "/images/kettlebell_swings.jpg",
#     "Clean and Press": "/images/clean_and_press.jpg",
#     "Burpees": "/images/burpees.jpg",
#     "Thrusters": "/images/thrusters.jpg",
#     "Pull Ups": "/images/pull_ups.jpg",
#     "Dips": "/images/tricep_dips.jpg",
#     "Muscle-Ups": "/images/muscle_ups.jpg",
#     "Handstands": "/images/handstands.jpg"
# }

with app.app_context():
    # Clear existing data
    WorkExercise.query.delete()
    WorkOut.query.delete()
    User.query.delete()
    Exercise.query.delete()
    Category.query.delete()
    db.session.commit()

    # Create categories
    cats = []
    for category_name in categories:
        cat = Category(name=category_name)
        cats.append(cat)
    db.session.add_all(cats)
    db.session.commit()

    # Create exercises linked to categories, with unique image URLs
    exercises = []
    for category_name, exercise_list in exercises_data.items():
        category = Category.query.filter_by(name=category_name).first()
        for exercise_name in exercise_list:
            # Fetch the image URL from the exercise_images mapping
            # image_url = exercise_images.get(exercise_name, "/images/default_exercise.jpg")  # Default if not found
            exercise = Exercise(name=exercise_name, body_part=category_name, category_id=category.id,)
            exercises.append(exercise)

    db.session.add_all(exercises)
    db.session.commit()

    # Create multiple users
    num_users = 5  
    users = []
    for _ in range(num_users):
        user = User(name=fake.name(), email=fake.email())
        user.password = ("Password11!!")
        users.append(user)

    db.session.add_all(users)
    db.session.commit()

    # Workouts (linked to users)
    workout_names = [
        "Strength Training", "Bodyweight Circuit", "HIIT", "Endurance Training",
        "Core Workout", "Full Body Routine", "CrossFit", "Cardio Blast",
        "Muscle Building", "Circuit Training"
    ]

    workouts = []
    for user in users:
        workout1 = WorkOut(
            name=fake.random_element(workout_names),
            date=fake.date_time_this_month(),
            user_id=user.id
        )
        workout2 = WorkOut(
            name=fake.random_element(workout_names),
            date=fake.date_time_this_month(),
            user_id=user.id
        )
        workouts.append(workout1)
        workouts.append(workout2)

    db.session.add_all(workouts)
    db.session.commit()

    # Work Exercises (Associating Workouts with Exercises)
    work_exs = []
    for workout in workouts:
        # Randomly select a subset of exercises (for example, 3 exercises per workout)
        selected_exercises = fake.random_elements(exercises, length=3, unique=True)
        for exercise in selected_exercises:
            weights = [20, 25, 40, 55, 80]  # List of solid weights in lbs

            work_ex = WorkExercise(
                sets=fake.random_int(min=3, max=6),
                reps=f"{fake.random_int(min=5, max=15)}-{fake.random_int(min=15, max=25)}",
                weight=fake.random_element(weights),
                workout_id=workout.id,
                exercise_id=exercise.id
            )
            work_exs.append(work_ex)

    db.session.add_all(work_exs)
    db.session.commit()

    print("Seeding done!")