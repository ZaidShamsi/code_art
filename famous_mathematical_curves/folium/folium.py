import numpy as np
from matplotlib import pyplot as plt

# Folium
def folium(a=2, b=3):
    phi = np.linspace(0, 2*np.pi, 600)
    r = (np.cos(phi)*(4*a*(np.sin(phi)**2)-b))
    x = r*np.cos(phi)
    y = r*np.sin(phi)
    return x, y

x, y = folium()

# shades of blue
# #B9D9EB -> columbia blue
# #041E42 -> Dallas cowboys blue

fig = plt.figure(facecolor='#B9D9EB')
ax = fig.add_subplot(111)

ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Folium', color='#041E42', fontsize=16, fontname='Candara', fontweight='bold')

# once axis are turned off -> ax.axis('off) -> facecolor will also hide 
# ax.set_facecolor("#005A9C")


ax.plot(x, y, linestyle='-', linewidth=4, color='#041E42')
ax.fill_between(x, y, color='#B9D9EB')

fig.savefig('folium.png')

plt.show()