# adding 8 people in list and choosing one at random
import random

people = []
for x in range(0, 8):
    people.append(input("Enter the name of persons to be added: "))
print(people)

print('_________________________________________________________________')
index = random.randint(0, 7)

print("Choosing randon person :", people[index])


# adding color making guess game and loop until user says no

colors = ["red", "yellow", "green", "blue", "white", "black", "violet", "indigo", "grey"]
print(colors)

while True:
    color = colors[random.randint(0, len(colors)-1)]
    print(color)
    guess = input("Guess the color i am thinking of :").lower()

    while True:
        if color == guess:
            break
        else:
            guess = input("Try again :")
    print("Correct")

    retry = input("Do you want to play again? :").lower()
    if retry == "yes":
        continue
    elif retry == "no":
        break
    else:
        input("Err Wrong input, type 'Yes' to continue 'No' to End :")

print("Thank you for playing.")
