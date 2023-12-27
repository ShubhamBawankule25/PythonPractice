# Define a circle class with 2 methods
# 1. Circumference
# 2. Area

import math

class circle:
    # pi=3.14  # we can use pi here as class variable
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        area =  math.pi * self.radius **2
        return round(area,3)
    
    
    def circumference(self):
        circumference = 2 * math.pi * self.radius
        return round(circumference,3)
    
c1 = circle(23)
c2 = circle(24)

print(c1.area())
print(c1.circumference())

print(c2.area())
print(c2.circumference())