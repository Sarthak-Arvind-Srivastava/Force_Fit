def user_info():

    while True:
        name = input("Enter your name: ").strip()
        if name:
            break
        print("Please Enter the name")
#####################################################################
    while True:
        try:
            age = int(input("Enter your age: "))
        except ValueError:
            print("Please use valid whole number for age greater than '0' only")
        else:
            if 1 <= age <= 130:
                break
            print("Please use valid age range between '1' to '130' only")
#####################################################################
    while True:
        try:
            weight = float(input("Enter your Weight(in kg): "))
        except ValueError:
            print("Please use valid number weight greater than '10' only")
        else:
            if 10 <= weight <= 350:
                break
            print("Please use valid weight range between '10' to '350' only")
#####################################################################
    while True:
        try:
            height = float(input("Enter your Height(in cm): "))
        except ValueError:
            print("Please use valid number height greater than '50' only")
        else:
            if 50 <= height <= 280:
                break
            print("Please use valid height range between '50' to '280' only")
#####################################################################
    while True:
        gender = input("""Enter Gender:
For Male (Enter 'M')
For Female (Enter 'F')
-> """).strip().upper()
        if gender in ["M", "F"]:
            break
        print("Invalid input! Valid input is M/F")
#####################################################################
    while True:
        try:
            activity_level = int(input("""
Enter your Activity Level(1-5):

1. Sedentary
   - Little or no exercise
   - Mostly sitting
   - < 4000 steps/day

2. Lightly Active
   - Light exercise 1-3 days/week
   - Walking or exercise around 30-60 min/day
   - ~4000-7000 steps/day

3. Moderately Active
   - Exercise 4-5 days/week
   - Around 1 hour exercise daily
   - ~7000-10000 steps/day

4. Very Active
   - Hard exercise 6-7 days/week
   - 1.5-2 hours training daily
   - Physical job or sports

5. Athlete / Extremely Active
   - Intense training 2+ times/day
   - Competitive sports
   - Manual labor + training

-> """))
            if 1 <= activity_level <= 5:
                break
            print("Activity level must be between 1 and 5.")
        except ValueError:
            print("Invalid input! Valid input is in range of 1-5")
#####################################################################
    while True:
        try:
            current_daily_calorie_intake = int(
                input("Enter your current daily calorie intake: "))
            if 500 <= current_daily_calorie_intake <= 15000:
                break
            print("Please enter a value between 500 and 15000 kcal.")
        except ValueError:
            print("Please use numbers only")
#####################################################################
    while True:
        goal = input("""
        Enter your Goal:
        1. MG -> Muscle Gain
           (30% of daily calories from fat)

        2. FL -> Fat Loss
           (Fat % Range -> 20% - 25%)
           (20% of daily calories from fat)

        3. M -> Maintenance
           (Fat % Range -> 25% - 30%)
           (25% of daily calories from fat)
        -> """).strip().upper()

        if goal in ["MG", "FL", "M"]:
            break
        print("Invalid input! Valid input are MG, FL, M")
#####################################################################
    while True:
        diet_preference = input("""
        Enter your Preferred Diet:
        1. Vegetarian (Enter 'V')
        2. egg-based (Enter 'EB')
        3. Non-Vegetarian (Enter 'NV')
        -> """).strip().upper()

        if diet_preference in ["V", "EB", "NV"]:
            break
        print("Invalid input! Valid input are V, EB, NV")
#####################################################################
    while True:
        try:
            number_of_meals_per_day = int(
                input(
                    "Enter the number of meals per day you would have."
                    "(Select 3 or 4 only): "
                ))
            if number_of_meals_per_day in [3, 4]:
                break
            print("Please select 3 or 4 only")
        except ValueError:
            print("Please use numbers only")

    return {
        "name": name,
        "age": age,
        "weight": weight,
        "height": height,
        "gender": gender,
        "activity_level": activity_level,
        "current_daily_calorie_intake": current_daily_calorie_intake,
        "goal": goal,
        "diet_preference": diet_preference,
        "number_of_meals_per_day": number_of_meals_per_day
    }
