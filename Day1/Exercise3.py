# Circumference and area

import math

radius = float(input("Enter value of Radius:"))

area = round(math.pi * radius ** 2,3)

circumference = round(2 * math.pi * radius,3)

print("Area:", area, "Circumference:", circumference)