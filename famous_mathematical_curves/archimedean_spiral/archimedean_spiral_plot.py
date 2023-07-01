from archimedean_spiral import ArchimedeanSpiral
from matplotlib import pyplot as plt

spiral_1 = ArchimedeanSpiral(0, 0.2, 6, 180)
x, y = spiral_1.xy_archimedean_spiral()

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

# fig.savefig('archimedean_spiral.png')

plt.show()