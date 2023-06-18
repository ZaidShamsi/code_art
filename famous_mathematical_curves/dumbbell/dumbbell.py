import numpy as np
from matplotlib import pyplot as plt

# Dumbbell
def dumbbell(a=2):
    # this generates the curve in first quadrant
    x = np.linspace(0, 1, 101)
    y = a**2*(x**4 - x**6)**(1/2)
    # this mirrors the curve along x
    x = np.append(x, x)
    y = np.append(y, -y)
    # this mirrors the curve along y
    x = np.append(-x, x)
    y = np.append(y, y)
    return x, y

x, y = dumbbell(a=1)

# #c0c0c0 -> lightgrey
# #282C35 -> ebony color
# #e5e4e2 -> platinum

fig = plt.figure(facecolor='#c0c0c0')
ax = fig.add_subplot(111)

ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Dumbbell', color='#282C35', fontsize=16, fontname='Candara', fontweight='bold')

# once axis are turned off -> ax.axis('off) -> facecolor will also hide 
# ax.set_facecolor("#005A9C")


ax.plot(x, y, linestyle='-', linewidth=4, color='#e5e4e2')
ax.fill_between(x, y, color='#282C35')

fig.savefig('dumbbell.png')

plt.show()