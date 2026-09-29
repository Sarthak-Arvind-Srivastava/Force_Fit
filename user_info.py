def user_info():
    
    name = input("Enter your name: ")

    while True:
        try:
            age = int(input("Enter your age: "))
            if age > 0:
                break
        except ValueError:
            print("Age must be greater than 0")

    while True:
        try:
            weight = float(input("Enter your Weight(in kg): "))
            if weight > 0:
                break
        except ValueError:
            print("Please use numbers only")

    while True:
        try:
            height = float(input("Enter your Height(in cm): "))
            if height > 0:
                break
        except ValueError:
            print("Please use numbers only")

    while True:
        gender = input("""Enter Gender:
Male (M)
Female (F)
-> """).upper()
        if gender in ["M", "F"]:
            break
        print("Invalid input! Valid output is M/F")

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
        except ValueError:
            print("Invalid input! Valid output is in range of 1-5")
    while True:
        try:
            current_daily_calorie_intake = int(
                input("Enter your current daily calorie intake: "))
            if current_daily_calorie_intake > 0:
                break
        except ValueError:
            print("Please use numbers only")
    while True:
        goal = input("""
Enter your Goal:
1. Muscle Gain (MG)
2. Fat Loss (FL)
3. Maintenance (M)
-> """).upper()
        if goal in ["MG", "FL", "M"]:
            break
        print("Invalid input! Valid output is MG, FL, M")

    return {"name": name,
            "age": age,
            "weight": weight,
            "height": height,
            "gender": gender,
            "activity_level": activity_level,
            "current_daily_calorie_intake": current_daily_calorie_intake,
            "goal": goal
            }
