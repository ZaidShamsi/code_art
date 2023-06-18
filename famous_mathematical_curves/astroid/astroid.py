import numpy as np
from matplotlib import pyplot as plt

# Astroid
def astroid():
    phi = np.linspace(0, 2*np.pi, 361)
    x = 4*np.power(np.cos(phi), 3)
    y = 4*np.power(np.sin(phi), 3)
    return x, y

x, y = astroid()

# Shades of orange
# #FF5733 -> kind of rustic
# #E25822 -> Flame color

# Shades of blue
#007fff -> Azure
#191970 -> Midnight blue
#005A9C -> Dodger blue

# shades of yellow
# #FFEA00 -> bright yellow
# #FFD700 -> gold

fig = plt.figure(facecolor='#005A9C')
ax = fig.add_subplot(111)

ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Astroid', color='#FFEA00', fontsize=16, fontname='Candara', fontweight='bold')

ax.set_facecolor("#005A9C")

ax.plot(x, y, linestyle='-', linewidth=4, color='#FF5733')
ax.fill_between(x, y, color='#E25822')

fig.savefig('astroid.png')

plt.show()

