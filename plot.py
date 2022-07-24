from matplotlib import pyplot as plt
import numpy as np

fh = open('./txt/M6WING.txt')

x = []
yUpper = []
yLower = []

for line in fh:
    x.append(float(line.split()[0]))
    yUpper.append(float(line.split()[1]))
    yLower.append(-1 * float(line.split()[1]))

plt.plot(x, yUpper, color = 'k', linestyle = 'solid')
plt.plot(x, yLower, color = 'k', linestyle = 'solid')
plt.xlim(-0.5, 1.5)
plt.ylim(-0.1, 0.1)

plt.show()
