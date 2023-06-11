import numpy as np
from matplotlib import pyplot as plt
import matplotlib.transforms as transform

def butterfly():
    x = np.linspace(0, 1, 101)
    y = np.power((np.power(x, 2) - np.power(x, 6)), 1/6)
    x = np.append(x, x)
    y = np.append(y, -y)
    return x, y

# Butterfly
x, y = butterfly()

# Shades of pink
# #FF0080 -> Fuchsia
# #A91B60 -> pink

# Shades of green
# #59981A -> green
# #81B622 -> lime green
# #3D550C -> olive green

fig = plt.figure(facecolor='#81B622')
ax = fig.add_subplot(111)

ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Butterfly', color='#3D550C', fontsize=16, fontname='Candara', fontweight='bold')

ax.set_facecolor("#005A9C")

# swapping x and y to orient horizontally
ax.plot(y, x, linestyle='-', linewidth=4, color='#A91B60')
# using fill_betweenx instead of fill_between to fill between curve and y-axis
ax.fill_betweenx(x, y, color='#FF0080')

fig.savefig('butterfly.png')

plt.show()