print("This program calculates your Body Mass Index")

height = float(input("Enter your Height in Feet : "))
weight = float(input("Enter your Weight in Kg: "))

heightMtrs = height * 0.3048
BMI = weight / (heightMtrs ** 2)

print("Height", round(heightMtrs,2))
print("Weight", weight)
print("BMI", round(BMI,2))

# <= 18.5 Underweight
# > 18.5 and <= 24.9 Normalweight
# > 24.9 and <= 29.9Overweight
# >= 30 Obesity

if BMI <= 18.5 :
    print("person is Under-weight")
elif (BMI > 18.5 and BMI <= 24.9) :
    print("person is Normal-weight")
elif (BMI > 24.9 and BMI <= 29.9) :
    print("person is Over-weight")
else:
    print("Person is Obese")
