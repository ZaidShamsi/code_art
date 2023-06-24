import numpy as np
from matplotlib import pyplot as plt

def butterfly():
    x = np.linspace(0, 1, 101)
    y = np.power((np.power(x, 2) - np.power(x, 6)), 1/6)
    # mirror along x
    x = np.append(x, x)
    y = np.append(y, -y)
    # mirror along y
    x = np.append(-x, x)
    y = np.append(y, y)
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
# #ECF87F -> yellow green

fig = plt.figure(facecolor='#3D550C')
ax = fig.add_subplot(111)

ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Butterfly', color='#ECF87F', fontsize=16, fontname='Candara', fontweight='bold')

# once axis are turned off -> ax.axis('off) -> facecolor will also hide 
# ax.set_facecolor("#005A9C")

ax.plot(x, y, linestyle='-', linewidth=4, color='#A91B60')
ax.fill_between(x, y, color='#FF0080')

fig.savefig('butterfly.png')

plt.show()