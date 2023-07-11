import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FFMpegWriter
from pendulum import Pendulum, calculate_pendulum_string_length

#-------------------------------------------#
# importing RK4 solver that is one level up #
#-------------------------------------------#
import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)
from numerical_solver import NumericalSolver

#------------------------------------------------------------#
# setting up writer object to save mp4 video #
#------------------------------------------------------------#
metadata = dict(title='pendulum motion', artist='ZaidShamsi',
                comment='pendulum motion: varying string length')
writer = FFMpegWriter(fps=24, metadata=metadata)

# ffmpeg executable downloaded from https://github.com/BtbN/FFmpeg-Builds/releases for windows 64
# update the path to ffmpeg.exe (usually located in bin folder)
plt.rcParams['animation.ffmpeg_path'] = r'..\..\ffmpeg.exe'

#-------------------------------------------#
# initializing n pendulums #
# pendulum_object_list contains n pendulums #
#-------------------------------------------#
start_time = 0 #sec
end_time = 60 #sec
pendulum_1_string_length = calculate_pendulum_string_length(60, end_time)
string_length_list = [factor*pendulum_1_string_length for factor in np.linspace(1, 3, 3)]
largest_string = max(string_length_list)
bob_radius = largest_string/30
bob_color_list = ['red', 'green', 'blue']
pendulum_object_list = [Pendulum(string_length, bob_radius, bob_color) 
                        for string_length, bob_color in zip(string_length_list, bob_color_list)]

#-------------------------------------------------------#
# solving for theta of each pendulum using RK4 #
# solution object contains [theta, omega] #
# xy_list contains x and y coordinates of each pendulum #
#-------------------------------------------------------#
initial_theta = 10 #degree
initial_omega = 0
solver_object_list = [NumericalSolver(pendulum_object.linear_sys_ODEs, [np.deg2rad(initial_theta), initial_omega], grid_size=1440,
                                      end_time=end_time, start_time=start_time) 
                 for i, pendulum_object in enumerate(pendulum_object_list)]
solution_list = [solver_object.RK4() for solver_object in solver_object_list]
theta_list = [solution_object[:, 0] for solution_object in solution_list]
xy_list = [pendulum_object.get_cartesian_coordinates(theta) 
           for pendulum_object, theta in zip(pendulum_object_list, theta_list)]

#--------------------------------------------------#
# setting up figure and axis to plot each pendulum #
# drawing cieling on each axis for pendulum #
#--------------------------------------------------#
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, subplot_kw=dict(box_aspect=1), facecolor='black')
fig.suptitle('(Linear) Simple Pendulum: time period relation with string length', fontsize=11, color='white')
axs = [ax1, ax2, ax3]
custom_xlim = (-0.6*largest_string, 0.6*largest_string)
custom_ylim = (-1.1*largest_string, 0.1*largest_string)
# plt.setp(axs, xlim=custom_xlim, ylim=custom_ylim)

# subplots 1, 2, 3
for index, ax in enumerate(axs):
    ax.set_title('pendulum length = ${}l$'.format(index+1), fontsize=9, color='white')
    ax.set_facecolor('black')
    ax.set_xlim(custom_xlim)
    ax.set_ylim(custom_ylim)
    pendulum_object_list[index].draw_ceiling(ax, -0.2*largest_string, 0.2*largest_string, cieling_color='#BBC4C2')

# subplot 4
pendulum_object_list[index].draw_ceiling(ax4, -0.2*largest_string, 0.2*largest_string, cieling_color='#BBC4C2')
ax4.set_title('$\\theta = {}\degree$'.format(initial_theta), fontsize=9, color='white')
ax4.set_facecolor('black')
ax4.set_xlim(custom_xlim)
ax4.set_ylim(custom_ylim)

#--------------------------------------------------------------------#
# Animating the pendulum motion #
# animation might appear slow since video will be written on the fly #
# comment out writer.saving and writer.grab_frame to experiment #
#--------------------------------------------------------------------#
time_steps = solver_object_list[0].t
count_of_time_steps = len(time_steps)
count_of_pendulums_drawn = 6
pendulum_components_list = list(range(0, count_of_pendulums_drawn))
with writer.saving(fig, "pendulum_motion(varying_string_length).mp4", dpi=200):
    for t_index in range(0, count_of_time_steps):
        if t_index % 1 == 0:
            for p_index, (pendulum_object, pendulum_xy, ax) in enumerate(zip(pendulum_object_list, xy_list, axs)):
                pendulum_components_list[p_index] = pendulum_object.draw_pendulum(ax, pendulum_xy[0][t_index], 
                                                                                pendulum_xy[1][t_index],
                                                                                string_width=1.0)
                pendulum_components_list[p_index+3] = pendulum_object.draw_pendulum(ax4, pendulum_xy[0][t_index], 
                                                                                    pendulum_xy[1][t_index],
                                                                                    string_width=1.0)
            plt.pause(0.01)
            writer.grab_frame()
            if t_index != count_of_time_steps:
                for a_pendulum_components in pendulum_components_list:
                    string, bob = a_pendulum_components
                    string.remove()
                    bob.remove()