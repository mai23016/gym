import random

def personalTrainer(training_days):
    # Categorize exercises by body part
    chest = ["Push-ups", "Chest press with dumbbells", "Incline bench press", "Decline push-ups", "Dumbbell flyes",
             "Cable crossover", "Diamond push-ups", "Medicine ball chest pass", "Chest dips", 
             "Chest squeeze using resistance band"]
    back = ["Pull-ups", "Bent-over barbell rows", "T-bar rows", "Seated rows", "Reverse grip lat pulldowns",
            "Straight-arm pulldowns", "Hyperextensions", "Face pulls", "Cable pull-throughs", "Single-arm dumbbell rows"]
    arms = ["Bicep curls", "Tricep dips", "Hammer curls", "Skull crushers", "Standing dumbbell press", "Push-ups",
            "Seated tricep extensions", "Concentration curls", "Diamond push-ups", "Preacher curls", "Tricep kickbacks",
            "Lateral raises", "Close grip push-ups", "Cable curls"]
    shoulders = ["Shoulder press", "Lateral raise", "Front raise", "Bent-over rear delt fly", "Upright row"]
    legs = ["Squats", "Lunges", "Deadlifts", "Step-ups", "Leg press", "Calf raises", "Bulgarian split squats", 
            "Glute bridges", "Leg curls", "Side lunges", "Wall sits", "Box jumps", "Hip thrusts", "Sumo squats"]
    abs = ["Plank", "Bicycle crunches", "Russian twists", "Leg raises", "Mountain climbers"]
    
    # Combine exercises for upper and lower body workouts
    upper_body_exercises = chest + back + arms + shoulders
    lower_body_exercises = legs + abs
    
    # Plan the weekly training schedule
    training_schedule = []
    for day in range(training_days):
        if day % 2 == 0:
            # Upper body days
            selected_exercises = random.sample(upper_body_exercises, k=random.randint(4, 6))
            training_schedule.append(("Upper Body", selected_exercises))
        else:
            # Lower body days
            selected_exercises = random.sample(lower_body_exercises, k=random.randint(4, 6))
            training_schedule.append(("Lower Body", selected_exercises))
    
    if training_days % 2 != 0:
        # Add a full body day if the number of days is odd
        full_body_exercises = random.sample(upper_body_exercises + lower_body_exercises, k=random.randint(4, 6))
        training_schedule.append(("Full Body", full_body_exercises))
    
    return training_schedule