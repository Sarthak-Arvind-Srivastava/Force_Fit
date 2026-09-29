def calorie_recommendation(tdee, goal):
    if goal == "MG":
        min_calorie = tdee + (tdee * 0.05)
        max_calorie = tdee + (tdee * 0.15)
    elif goal == "FL":
        max_calorie = tdee - (tdee * 0.1)
        min_calorie = tdee - (tdee * 0.25)
    elif goal == "M":
        min_calorie = tdee
        max_calorie = tdee
    return round(min_calorie, 2), round(max_calorie, 2)
########################################################


def protein_recommendation(goal, weight, activity_level):
    if activity_level > 1:
        if goal == "MG":
            min_protein = 1.6 * weight
            max_protein = 1.8 * weight
        elif goal == "FL":
            min_protein = 1.8 * weight
            max_protein = 2.4 * weight
        elif goal == "M":
            min_protein = 1.2 * weight
            max_protein = 1.8 * weight
    else:
        min_protein = 0.8 * weight
        max_protein = 1 * weight
    return round(min_protein, 2), round(max_protein, 2)
########################################################


#def exercise_recommendation(goal, activity_level):
