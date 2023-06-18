import numpy as np
from matplotlib import pyplot as plt

# Lemniscate
def lemniscate():
    phi = np.linspace(-np.pi/4, np.pi/4, 91)
    # this gives the curve co-ordinates for the positive x-axis
    x = np.cos(phi)*np.sqrt(2*np.cos(2*phi))
    y = np.sin(phi)*np.sqrt(2*np.cos(2*phi))
    # mirrored along y to get complete curve
    x = np.append(-x, x)
    y = np.append(y, y)
    return x, y

x, y = lemniscate()

# old paper color -> #E0C9A6
# burnt paper -> #C08826
# burnt orange -> #CC5500

fig = plt.figure(facecolor='#E0C9A6')
ax = fig.add_subplot(111)

ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Lemniscate', color='#CC5500', fontsize=16, fontname='Candara', fontweight='bold')

# once axis are turned off -> ax.axis('off) -> facecolor will also hide 
# ax.set_facecolor("#005A9C")


ax.plot(x, y, linestyle='-', linewidth=4, color='#CC5500')
ax.fill_between(x, y, color='#E0C9A6')

fig.savefig('lemniscate.png')

plt.show()

