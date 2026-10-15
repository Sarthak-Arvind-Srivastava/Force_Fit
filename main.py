from user_info import user_info
from recommendation import (
    calorie_recommendation,
    protein_recommendation,
    fat_recommendation,
    carbohydrate_recommendation,
    diet_recommendation,
    exercise_recommendation
)
from calculations import (
    bmi_calculation,
    bmr_calculation,
    tdee_calculation,
    name
)
########################################################


def main():

    user_data = user_info()

    print("x" * 40)
    print()
    print(
        f"Hello {name(user_data["name"])},\n"
        "This info is for you.\n"
        "There are some Diet and Exercise recommendation at the end"
    )
########################################################
    print()
    bmi = bmi_calculation(
        user_data["weight"],
        user_data["height"]
    )

    if bmi < 18.5:
        print(f"BMI = {bmi} You are Underweight")
    elif 18.5 <= bmi <= 24.9:
        print(f"BMI = {bmi} Your Weight is Normal")
    elif 24.9 < bmi <= 29.9:
        print(f"BMI = {bmi} You are Overweight")
    elif 29.9 < bmi:
        print(f"BMI = {bmi} You are Obese")
########################################################
    print()
    bmr = bmr_calculation(
        user_data["weight"],
        user_data["height"],
        user_data["age"],
        user_data["gender"]
    )

    print(f"BMR = {bmr} kcal/day")
    print("This is your estimated resting calorie requirement.")
########################################################
    print()
    tdee = tdee_calculation(
        bmr,
        user_data["activity_level"]
    )

    print(f"TDEE = {tdee} kcal/day")
    print("This is your estimated total calorie requirement.")
########################################################
    print()
    calorie_suggestion = calorie_recommendation(
        tdee,
        user_data["goal"]
    )

    print(f"{calorie_suggestion} kcal/day")
    print(f"This is your daily calorie intake suggestion as per your goal")
########################################################
    print()
    protein_suggestion = protein_recommendation(
        user_data["goal"],
        user_data["weight"],
        user_data["activity_level"]
    )

    print(f"{protein_suggestion} g/day")
    print(f"This is your daily protein intake suggestion as per your goal")
########################################################
    print()
    min_cal, max_cal = calorie_suggestion
    target_calories = round((min_cal + max_cal) / 2, 2)
    fat_grams = fat_recommendation(
        target_calories,
        user_data["goal"]
    )

    print(f"{fat_grams} g/day")
    print(f"This is your daily fat intake suggestion as per your goal")
########################################################
    print()
    min_protein, max_protein = protein_suggestion
    protein = round((min_protein + max_protein) / 2)

    carbohydrate_grams = carbohydrate_recommendation(
        target_calories,
        protein,
        fat_grams
    )

    print(f"{carbohydrate_grams} g/day")
    print(f"This is your daily carbohydrate intake suggestion as per your goal")
########################################################
    print()
    print(f"Food you should Eat")
    print("-" * 25)

    diet = diet_recommendation(
        user_data["diet_preference"]
    )

    print(diet)
########################################################
    print()
    print(f"Excercise you should do")
    print("-" * 25)

    exercise = exercise_recommendation(
        user_data["goal"]
    )

    print(exercise)


main()
