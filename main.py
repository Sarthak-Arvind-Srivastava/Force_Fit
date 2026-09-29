from user_info import user_info
from recommendation import (
    calorie_recommendation,
    protein_recommendation
)
from calculations import (
    bmi_calculation,
    bmr_calculation,
    tdee_calculation
)


def main():

    user_data = user_info()

########################################################
    print()
    bmi = bmi_calculation(
        user_data["weight"],
        user_data["height"]
    )

    if bmi < 18.5:
        print(f"BMI = {bmi} you are Underweight")
    elif 18.5 <= bmi <= 24.9:
        print(f"BMI = {bmi} your Weight is Normal")
    elif 24.9 < bmi <= 29.9:
        print(f"BMI = {bmi} you are Overweight")
    elif 29.9 < bmi:
        print(f"BMI = {bmi} you are Obese")

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

    print(f"{calorie_suggestion} kcal/day\nThis is your daily calorie intake suggestion as per your goal")

########################################################
    print()
    protein_suggestion = protein_recommendation(
        user_data["goal"],
        user_data["weight"],
        user_data["activity_level"]
    )

    print(f"{protein_suggestion} g/day\nThis is your daily protein intake suggestion as per your goal")


main()
