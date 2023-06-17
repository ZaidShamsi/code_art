import numpy as np
from matplotlib import pyplot as plt

# Logarithmic spiral
def logarithmic_spiral(k = 0.1):
    phi = np.linspace(0, 6*np.pi, 721)
    x = np.exp(k*phi)*np.cos(phi)
    y = np.exp(k*phi)*np.sin(phi)
    return x, y

x, y = logarithmic_spiral()

# shades of yellow
# #FFEA00 -> bright yellow
# #FFD700 -> gold

fig = plt.figure(facecolor='black')
ax = fig.add_subplot(111)

ax.set_aspect('equal')
# ax.axis('off') # I do not need turn off the axis as I have already made the figure background color black
ax.set_title('Logarithmic spiral', color='#FFD700', fontsize=16, fontname='Candara')
ax.set_facecolor("black")

ax.plot(x, y, linestyle='-', linewidth=4, color='#FFD700')

fig.savefig('logarithmic_spiral.png')

plt.show()