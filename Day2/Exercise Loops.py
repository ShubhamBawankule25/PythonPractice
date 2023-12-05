# adding 8 people in list and choosing one at random
import random

# people = []
# while len(people) < 8:
#     people.append(input("Enter the name of persons to be added: "))
# print(people)
#
# print('_________________________________________________________________')
# index = random.randint(0, 7)
#
# print(people[index])


# adding color making guess game and loop until user says no

color = ["red", "yellow", "green", "blue", "white", "black", "violet", "indigo", "grey"]
print(color)

while True:
    index = random.randint(0, len(color) - 1)
    answer = (color[index])
    print(answer)
    prompt1 = input("Guess the color Iam thinking of: ")
    while True:
        if prompt1.lower() == answer:
            print("Hey that's the color i was thinking about!!!!")
            break
        else:
            prompt1 = input("Nope, Try again: ")

    prompt2 = input("Do you want to guess again?")
    if prompt2.lower() == "no":
        break
print("Thank you for playing")
