weight = eval(input("Enter your weight (kg): "))
height = eval(input("Enter your height (m): "))

bmi = weight / (height * height)

print("BMI =", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal Weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")

    
