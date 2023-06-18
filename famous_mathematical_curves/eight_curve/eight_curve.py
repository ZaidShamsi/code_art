import numpy as np
from matplotlib import pyplot as plt

# Eight curve
def eight_curve(a=2):
    phi = np.linspace(0, 2*np.pi, 361)
    x = a*np.sin(phi)
    y = a*np.sin(phi)*np.cos(phi)
    return x, y

x, y = eight_curve()

# shades of blue
# #002D62 -> astros navy
# #F0F8FF -> alice blue

fig = plt.figure(facecolor='#002D62')
ax = fig.add_subplot(111)

ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Eight curve', color='#F0F8FF', fontsize=16, fontname='Candara', fontweight='bold')

# once axis are turned off -> ax.axis('off) -> facecolor will also hide 
# ax.set_facecolor("#005A9C")


ax.plot(x, y, linestyle='-', linewidth=4, color='#F0F8FF')
ax.fill_between(x, y, color='#002D62')

fig.savefig('eight_curve.png')

plt.show()



