import numpy as np
from matplotlib import pyplot as plt

# Gear
def gear(a = 1, b = 10, n = 12):
    phi = np.linspace(0, 2*np.pi, 600)
    x = (a+(1/b)*np.tanh(b*np.sin(n*phi)))*np.cos(phi)
    y = (a+(1/b)*np.tanh(b*np.sin(n*phi)))*np.sin(phi)
    return x, y

x, y = gear()

# shades of silver (metallic)
# tint of black -> #1f1f1f
# grey (tint of white) -> #c6c5c8, #d4d3d5, #e2e2e3

fig = plt.figure(facecolor='#1f1f1f')
ax = fig.add_subplot(111)

ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Gear', color='#e2e2e3', fontsize=16, fontname='Candara', fontweight='bold')

# once axis are turned off -> ax.axis('off) -> facecolor will also hide 
# ax.set_facecolor("#005A9C")


ax.plot(x, y, linestyle='-', linewidth=4, color='#c6c5c8')
ax.fill_between(x, y, color='#d4d3d5')

fig.savefig('gear.png')

plt.show()
