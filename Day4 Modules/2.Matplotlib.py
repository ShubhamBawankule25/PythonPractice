import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [100, 200, 300, 400]

plt.plot(x, y)
plt.show()

legend = ["jan", "Feb", "Mar", "Apr"]
plt.xticks(x, legend)

plt.plot(x, y)
plt.show()

plt.bar(x,y)
plt.show()
