import numpy as np
from matplotlib import pyplot as plt
from archimedean_spiral import ArchimedeanSpiral, intertwine_two_vectors

spiral_1 = ArchimedeanSpiral(7, 5.9, 1, 30)

x_zeros = np.zeros(spiral_1.n*spiral_1.d)
y_zeros = np.zeros(spiral_1.n*spiral_1.d)

# #shades of yellow
# #FFEA00 -> bright yellow
# #FFD700 -> gold

fig = plt.figure(facecolor='black')
ax = fig.add_subplot(111)

x, y = spiral_1.xy_archimedean_spiral()
limit = 1.1*np.max(np.absolute(x))
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)

ax.set_aspect('equal')
# ax.axis('off') # I do not need turn off the axis as I have already made the figure background color black
ax.set_facecolor("black")

# play around with number of rotations to get various designs
number_of_rotations = 11
theta = np.linspace(0, 2*np.pi, number_of_rotations)

for theta_value in theta[0:-1]:
    x_rotated, y_rotated = spiral_1.rotation(theta_value, 'anti-clockwise')
    intertwine_x_points = intertwine_two_vectors(x_rotated, x_zeros)
    intertwine_y_points = intertwine_two_vectors(y_rotated, y_zeros)
    ax.plot(x_rotated, y_rotated, linestyle=':', linewidth=1, color='#FFD700')
    ax.plot(intertwine_x_points, intertwine_y_points, linestyle=':', linewidth=0.1, color='#FFD700')

plt.pause(1)
fig.savefig('archimedean_spiral_design(rotated).png')

for theta_value in theta[0:-1]:
    x_reflected, y_reflected = spiral_1.reflection(theta_value, 'anti-clockwise')
    intertwine_x_points = intertwine_two_vectors(x_reflected, x_zeros)
    intertwine_y_points = intertwine_two_vectors(y_reflected, y_zeros)
    ax.plot(x_reflected, y_reflected, linestyle=':', linewidth=1, color='#FFD700')
    ax.plot(intertwine_x_points, intertwine_y_points, linestyle=':', linewidth=0.1, color='#FFD700')

fig.savefig('archimedean_spiral_design(reflected).png')

plt.show()