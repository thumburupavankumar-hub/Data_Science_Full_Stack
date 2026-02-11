"""

Problem 1.4: BMI Calculator with Categories (Easy)
Write a program that calculates BMI (Body Mass Index) and categorizes it.

Formula: BMI = weight (kg) / (height (m))²

Categories:

Below 18.5: Underweight
18.5-24.9: Normal weight
25-29.9: Overweight
30 and above: Obese
Hint: First calculate BMI using the formula (use ** for power or multiply height by itself). Then use if-elif-else to categorize.

"""

print("BMI Calculator with Categories")

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (meters): "))

BMI = weight / (height ** 2)

print("Your BMI is:", round(BMI, 2))

if BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal weight")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")