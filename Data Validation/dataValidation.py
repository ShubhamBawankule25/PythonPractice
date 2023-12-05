data_val = False

while data_val == False:
    grade1 = (input("Enter first test's grade: "))
    try:
        grade1 = float(grade1)
        print("Grade1 is :", grade1)
    except:
        print("Invalid Grade, Only Enter Grades and separate by decimals where applicable")
        continue

    if grade1 < 1 or grade1 > 10:
        print("Grade should be between 1 to 10.")
        continue
    else:
        data_val = True


data_val = False

while data_val == False:
    grade2 = (input("Enter second test's grade: "))
    try:
        grade2 = float(grade2)
        print("Grade2 is :", grade2)
    except:
        print("Invalid Grade, Only Enter Grades and separate by decimals where applicable")
        continue

    if grade2 < 1 or grade2 > 10:
        print("Grade should be between 1 to 10.")
        continue
    else:
        data_val = True

data_val = False

while data_val == False:
    totalClasses = (input("Number of total classes: "))
    try:
        totalClasses = int(totalClasses)
        print("Total classes are :", totalClasses)
    except:
        print("Invalid Number of Classes")
        continue

    if totalClasses <= 0:
        print("Classes cannot be zero.")
        continue
    else:
        data_val = True

data_val = False
while data_val == False:
    absence = (input("Number of days absent: "))
    try:
        absence = int(absence)
        print("Absence's are :", absence)
    except:
        print("Invalid Number Of Absences")
        continue

    if absence > totalClasses:
        print("Absences cannot be more than Total classes.")
        continue
    else:
        data_val = True

print("-------------------------------------------------------")

avgGrade = (grade1 + grade2) / 2
attendance = (totalClasses - absence) / totalClasses

print("Avg Grade: ", avgGrade)
print("Attendance: ", str(attendance * 100) + '%')

# Passing criterion
# Avg Grade 6.0+
# attendance 80%

if (avgGrade >= 6 and attendance >= 0.8):
    print("Student is approved")
elif (avgGrade < 6 and attendance < 0.8):
    print("Student failed due to not meeting passing criteria.")
elif (attendance >= 0.8):
    print("Student failed due to grade less than 6.")
else:
    print("Student failed due to attendance less than 80%.")