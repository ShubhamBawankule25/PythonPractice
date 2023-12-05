# Booleans and conditionals basic

myAge = 25

userAge = int(input("Type in Your Age: "))

if myAge > userAge:
    print("User is younger than owner")
elif myAge < userAge:
    print("User is older than owner")
else:
    print("User is same age as Owner")