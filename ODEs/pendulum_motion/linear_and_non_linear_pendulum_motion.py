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
metadata = dict(title='linear vs non-linear simple pendulum', artist='ZaidShamsi',
                comment='comparision of linear and non-linear simple pendulum')
writer = FFMpegWriter(fps=24, metadata=metadata)

# ffmpeg executable downloaded from https://github.com/BtbN/FFmpeg-Builds/releases for windows 64
# update the path to ffmpeg.exe (usually located in bin folder)
plt.rcParams['animation.ffmpeg_path'] = r'..\..\ffmpeg.exe'

#---------------------------------------------------------------------------#
# Design: The lengths of the pendulums are set such that in a given time t, #
# the first pendulum completes n oscillations, #
# and each subsequent one completes one more oscillation than the previous. #
#---------------------------------------------------------------------------#

#-------------------------------------------#
# initializing pendulum #
#-------------------------------------------#
start_time = 0 #sec
end_time = 60 #sec
number_of_oscillations = 30
pendulum_string_length = calculate_pendulum_string_length(number_of_oscillations, end_time)
bob_radius = pendulum_string_length/30
bob_color = '#BBC4C2'
pendulum_object = Pendulum(pendulum_string_length, bob_radius, bob_color)

#-------------------------------------------------------#
# solving for theta of using RK4 #
# solution contains [theta, omega] #
# xy_list contains x and y coordinates of pendulum #
#-------------------------------------------------------#
initial_theta_list = [10, 15, 20, 25] #degree
initial_omega = 0
linear_pendulum_x_list = list(range(0, len(initial_theta_list)))
linear_pendulum_y_list = list(range(0, len(initial_theta_list)))
non_linear_pendulum_x_list = list(range(0, len(initial_theta_list)))
non_linear_pendulum_y_list = list(range(0, len(initial_theta_list)))
for index, initial_theta in enumerate(initial_theta_list):
    linear_solver_object = NumericalSolver(pendulum_object.linear_sys_ODEs, [np.deg2rad(initial_theta), initial_omega], grid_size=1440, 
                                        end_time=end_time, start_time=start_time)
    solution = linear_solver_object.RK4()
    theta = solution[:, 0]
    xy_list = pendulum_object.get_cartesian_coordinates(theta)
    linear_pendulum_x_list[index] = xy_list[0]
    linear_pendulum_y_list[index] = xy_list[1]
    # non-linear ODEs
    non_linear_solver_object = NumericalSolver(pendulum_object.non_linear_sys_ODEs, [np.deg2rad(initial_theta), initial_omega], 
                                            grid_size=1440, end_time=end_time, start_time=start_time)
    solution = non_linear_solver_object.RK4()
    theta = solution[:, 0]
    xy_list = pendulum_object.get_cartesian_coordinates(theta)
    non_linear_pendulum_x_list[index] = xy_list[0]
    non_linear_pendulum_y_list[index] = xy_list[1]

#--------------------------------------------------#
# setting up figure and axis to plot each pendulum #
#--------------------------------------------------#
fig, axs = plt.subplots(2, 2, subplot_kw=dict(box_aspect=1), facecolor='black')
fig.suptitle('Linear (light grey) vs Non-linear (bold grey) Simple Pendulum', fontsize=11, color='white')
custom_xlim = (-0.6*pendulum_string_length, 0.6*pendulum_string_length)
custom_ylim = (-1.1*pendulum_string_length, 0.1*pendulum_string_length)

#-------------------------------------------#
# drawing cieling for pendulum #
#-------------------------------------------#
for ax, initial_theta in zip(axs.ravel(), initial_theta_list):
    ax.set_title('$\\theta = {}\degree$'.format(initial_theta), fontsize=9, color='white')
    ax.set_facecolor('black')
    ax.set_xlim(custom_xlim)
    ax.set_ylim(custom_ylim)
    pendulum_object.draw_ceiling(ax, -0.2*pendulum_string_length, 0.2*pendulum_string_length, cieling_color='#BBC4C2')

# plt.show()
#--------------------------------------------------------------------#
# Animating the pendulum waves motion #
# animation might appear slow since video will be written on the fly #
# comment out writer.saving and writer.grab_frame to experiment #
#--------------------------------------------------------------------#
time_steps = linear_solver_object.t
count_of_time_steps = len(time_steps)
count_of_pendulums_drawn = 4
linear_pendulum_components_list = list(range(0, count_of_pendulums_drawn))
non_linear_pendulum_components_list = list(range(0, count_of_pendulums_drawn))
with writer.saving(fig, "linear_and_non_linear_simple_pendulum.mp4", dpi=200):
    for t_index in range(0, count_of_time_steps):
        for p_index, (ax, linear_pendulum_x, linear_pendulum_y, non_linear_pendulum_x, non_linear_pendulum_y) in enumerate(zip(axs.ravel(), 
                linear_pendulum_x_list, linear_pendulum_y_list, non_linear_pendulum_x_list, non_linear_pendulum_y_list)):
            linear_pendulum_components_list[p_index] = pendulum_object.draw_pendulum(ax,
                                                                linear_pendulum_x[t_index], 
                                                                linear_pendulum_y[t_index], string_width=0.5)
            non_linear_pendulum_components_list[p_index] = pendulum_object.draw_pendulum(ax, 
                                                                non_linear_pendulum_x[t_index], 
                                                                non_linear_pendulum_y[t_index], string_width=1.0)
        plt.pause(0.01)
        writer.grab_frame()
        if t_index != count_of_time_steps:
            for linear_pendulum_components, non_linear_pendulum_components in zip(linear_pendulum_components_list,
                                                                                non_linear_pendulum_components_list):
                string, bob = linear_pendulum_components
                string.remove()
                bob.remove()
                string, bob = non_linear_pendulum_components
                string.remove()
                bob.remove()       