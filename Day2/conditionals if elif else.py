grade1 = float(input("Enter first test's grade: "))
grade2 = float(input("Enter second test's grade: "))
absence = float(input("Number of days absent: "))
totalClasses = float(input("Number of total classes: "))

avgGrade = (grade1 + grade2) / 2
attendance = (totalClasses - absence) / totalClasses

print("Avg Grade: ", avgGrade)
print("Attendance: ", str(attendance * 100) + "%")

# Passing criterion
# Avg Grade 6.0+
# attendance 80%

if (avgGrade >= 6):
    if (attendance >= 0.8):
        print("Student is approved")
    else:
        print("Student failed due to attendance less than 80%.")
elif (attendance >= 0.8):
    print("Student failed due to grade less than 6.")
else:
    print("Student failed due to not meeting passing criteria.")
