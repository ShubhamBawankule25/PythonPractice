<<<<<<< HEAD:Day4 Modules/3. Exercise.py
import matplotlib.pyplot as plt
import time as t

time = []
mistakes = 0

print('This program help you type faster, you have to type the word "programming" as fast as you can five times')
input("Press Enter to start")

while len(time) < 5:
    start = t.time()
    word = input("Type the word:")
    end = t.time()
    time_d = end - start
    time.append(time_d)

    if (word.lower() != "programming"):
        mistakes += 1

print("------------------------------------------------------------------")

print("You have made " + str(mistakes) + " mistakes.")
print("Lets see your evaluation")
x = [1, 2, 3, 4, 5]
legend = ["1", "2", "3", "4", "5"]
plt.xticks(x, legend)
y = time

plt.xlabel("Attempts")
plt.ylabel("Time in seconds")
plt.title("Your evaluation")

plt.bar(x, y)
plt.show()

=======
import matplotlib.pyplot as plt
import time as t

time = []
mistakes = 0

print('This program help you type faster, you have to type the word "programming" as fast as you can five times')
input("Press Enter to start")

while len(time) < 5:
    start = t.time()
    word = input("Type the word:")
    end = t.time()
    time_d = end - start
    time.append(time_d)

    if (word.lower() != "programming"):
        mistakes += 1

print("------------------------------------------------------------------")

print("You have made " + str(mistakes) + " mistakes.")
print("Lets see your evaluation")
x = [1, 2, 3, 4, 5]
legend = ["1", "2", "3", "4", "5"]
plt.xticks(x, legend)
y = time

plt.xlabel("Attempts")
plt.ylabel("Time in seconds")
plt.title("Your evaluation")

plt.bar(x, y)
plt.show()


>>>>>>> f8eef7abfd042b314f67960e81a6cab6dc0276a2:Modules/3. Exercise.py
