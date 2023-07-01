from matplotlib import pyplot as plt
from logarithmic_spiral import LogarithmicSpiral, intertwine_two_vectors

spiral_1 = LogarithmicSpiral(0.4, -0.4, 0.15, 6, 30)
x, y = spiral_1.xy_logarithmic_spiral()

# intertwine_x_points = intertwine_two_vectors(x, [0]*spiral_1.n*spiral_1.d)
# intertwine_y_points = intertwine_two_vectors(y, [0]*spiral_1.n*spiral_1.d)

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
# ax.plot(intertwine_x_points, intertwine_y_points, linestyle='-', linewidth=0.5, color='#FFD700')

fig.savefig('logarithmic_spiral.png')

plt.show()