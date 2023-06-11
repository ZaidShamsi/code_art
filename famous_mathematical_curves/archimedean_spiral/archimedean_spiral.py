import numpy as np
from matplotlib import pyplot as plt

# Archimedean spiral
def archimedean_spiral(number_of_rotations):
    phi = np.linspace(0, number_of_rotations*np.pi, number_of_rotations*360)
    x = np.multiply(phi, np.cos(phi))
    y = np.multiply(phi, np.sin(phi))
    return x, y

x, y = archimedean_spiral(10)

# shades of yellow
# #FFEA00 -> bright yellow
# #FFD700 -> gold

fig = plt.figure(facecolor='black')
ax = fig.add_subplot(111)

ax.set_aspect('equal')
# ax.axis('off') # I do not need turn off the axis as I have already made the figure background color black
ax.set_title('Archimedean spiral', color='#FFD700', fontsize=16, fontname='Candara')
ax.set_facecolor("black")

ax.plot(x, y, linestyle='-', linewidth=4, color='#FFD700')

fig.savefig('archimedean_spiral.png')

plt.show()
