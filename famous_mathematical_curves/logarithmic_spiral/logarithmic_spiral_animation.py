import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FFMpegWriter
from logarithmic_spiral import LogarithmicSpiral

metadata = dict(title='logarithmic spiral', artist='ZaidShamsi',
                comment='logarithmic spiral curve')
writer = FFMpegWriter(fps=15, metadata=metadata)

# ffmpeg executable downloaded from https://github.com/BtbN/FFmpeg-Builds/releases for windows 64
# update the path to ffmpeg.exe (usually located in bin folder)
plt.rcParams['animation.ffmpeg_path'] = r'..\..\ffmpeg.exe'

spiral_1 = LogarithmicSpiral(0.4, -0.4, 0.15, 6, 90)

# #shades of yellow
#FFEA00 -> bright yellow
#FFD700 -> gold

fig = plt.figure(facecolor='black')
ax = fig.add_subplot(111)

x, y = spiral_1.xy_logarithmic_spiral()
limit = 1.1*np.max(np.absolute(x))
ax.set_xlim(-limit, limit)
ax.set_ylim(-limit, limit)

ax.set_aspect('equal')
# ax.axis('off') # I do not need turn off the axis as I have already made the figure background color black
ax.set_title('eadem mutata resurgo', color='#FFD700', fontsize=16, fontname='Candara')
ax.set_facecolor("black")

# Animating the mechanism
theta = np.linspace(0, 2*np.pi, 361)
with writer.saving(fig, "logarithmic_spiral(rotation).mp4", 100):
    for i, theta_value in enumerate(theta):
        x_rotated, y_rotated = spiral_1.rotation(theta_value, 'anti-clockwise')
        spiral_object, = ax.plot(x_rotated, y_rotated, linestyle='-', linewidth=2, color='#FFD700')
        plt.pause(0.01)
        writer.grab_frame()
        if i != len(theta):
            spiral_object.remove()

plt.show()