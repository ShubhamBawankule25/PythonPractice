# 1st approach
import random

x = 0
people = []

while x < 5:
    people.append(input("Type name to be added to list: "))
    x += 1

print(people)


# 2nd approach
people = []

while len(people) < 5:
    people.append(input("Type name to be added to list: "))
    x += 1

print(people)

# Infinite loop
number = random.randint(1, 10)
guess = int(input("Guess the number i am thinking: "))
while True:
    if guess == number:
        break
    else:
        guess = int(input("Nope, try Again: "))
print("Hey same pinch, that's the number i was thinking about.")
