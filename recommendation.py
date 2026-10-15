import psycopg2

with open("info.txt", "r") as f:
    connection_info = f.read()

with psycopg2.connect(connection_info) as conn:
    with conn.cursor() as cur:
        cur.execute("select * from food_nutrition_chart")
        food_result = cur.fetchall()
# ------------------------------------------------------#
with open("info_2.txt", "r") as f:
    connection_info_2 = f.read()

with psycopg2.connect(connection_info_2) as conn:
    with conn.cursor() as cur:
        cur.execute("select * from muscle_gain_exercise")
        mg_exercise_result = cur.fetchall()

        cur.execute("select * from fat_loss_exercise")
        fl_exercise_result = cur.fetchall()

        cur.execute("select * from weight_maintenance_exercise")
        wm_exercise_result = cur.fetchall()
########################################################


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


def fat_recommendation(Target_calories, goal):
    if goal == "MG":
        fat_g = (Target_calories * 0.30) / 9
    elif goal == "FL":
        fat_g = (Target_calories * 0.20) / 9
    elif goal == "M":
        fat_g = (Target_calories * 0.25) / 9
    return round(fat_g, 2)
########################################################


def carbohydrate_recommendation(Target_calories, protein, fat):
    carbohydrate_g = (Target_calories - (protein * 4) - (fat * 9)) / 4
    return round(carbohydrate_g, 2)
########################################################


def diet_recommendation(diet_preference, food_result=food_result):
    V_category = ["Grain", "Prepared Grain", "Legume",
                  "Dal", "Dairy", "Fat", "Vegetable", "Fruit", "Nuts"]
    NV_category = ["Animal Protein", "Meat"]
    EB_category = ["Animal Protein"]

    result = []

    for i in food_result:
        if diet_preference == "V":
            if i[1] in V_category:
                result.append(i[0])

        elif diet_preference == "NV":
            if i[1] in NV_category + V_category:
                result.append(i[0])

        elif diet_preference == "EB":
            if i[1] in EB_category + V_category:
                result.append(i[0])

    return ", ".join(result)
########################################################


def exercise_recommendation(goal, mg_exercise_result=mg_exercise_result, fl_exercise_result=fl_exercise_result, wm_exercise_result=wm_exercise_result):

    result = []

    if goal == "MG":
        result.extend(i[0] for i in mg_exercise_result)
    elif goal == "FL":
        result.extend(i[0] for i in fl_exercise_result)
    elif goal == "M":
        result.extend(i[0] for i in wm_exercise_result)

    return ", ".join(result)

