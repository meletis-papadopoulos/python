height = float(input("What's your height in (centimetres)? "))
weight = float(input("What's your weight in (kilograms)? "))
bmi = round(weight / ((height / 100) ** 2), 2)

if bmi < 16.0:
    classification = "Severely Underweight"
elif bmi <= 18.4:
    classification = "Underweight"
elif bmi <= 24.9:
    classification = "Normal"
elif bmi <= 29.9:
    classification = "Overweight"
elif bmi <= 34.9:
    classification = "Moderately Obese"
elif bmi <= 39.9:
    classification = "Severely Obese"
else:
    classification = "Morbidly Obese"

print(f"Your BMI of {bmi} makes you {classification}")