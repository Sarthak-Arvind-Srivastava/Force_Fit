
########################################################

def bmi_calculation(weight, height):
    bmi = weight / (height / 100) ** 2
    return round(bmi, 2)
########################################################


def bmr_calculation(weight, height, age, gender):
    if gender == "M":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5

    elif gender == "F":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return round(bmr, 2)
########################################################


def tdee_calculation(bmr, activity_level):
    activity_multiplier = {1: 1.2,
                           2: 1.375,
                           3: 1.55,
                           4: 1.725,
                           5: 1.9}
    tdee = bmr * activity_multiplier[activity_level]
    return round(tdee, 2)
########################################################


def name(name):
    name = name.split()
    return name[0].capitalize()
