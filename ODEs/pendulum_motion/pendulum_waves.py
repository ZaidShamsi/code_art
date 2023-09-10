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
metadata = dict(title='pendulum waves', artist='ZaidShamsi',
                comment='pendulum waves')
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
# initializing n pendulums #
# pendulum_object_list contains n pendulums #
#-------------------------------------------#
oscillations_list = np.linspace(60, 71, 12)
start_time = 0 #sec
end_time = 60 #sec
string_length_list = [calculate_pendulum_string_length(n, end_time) for n in oscillations_list]
largest_string = max(string_length_list)
bob_radius = largest_string/30
bob_color_list = 3*['red', 'green', 'yellow', 'blue']
pendulum_object_list = [Pendulum(string_length_list[i], bob_radius, bob_color_list[i]) for i in range(0, len(string_length_list))]

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
#--------------------------------------------------#
fig = plt.figure(facecolor='black')
ax = fig.add_subplot(111)
ax.set_aspect('equal')
custom_xlim = (-0.6*largest_string, 0.6*largest_string)
custom_ylim = (-1.1*largest_string, 0.1*largest_string)
ax.set_xlim(custom_xlim)
ax.set_ylim(custom_ylim)
ax.set_facecolor('black')


#-------------------------------------------#
# drawing cieling for pendulum #
#-------------------------------------------#
pendulum_object_list[0].draw_ceiling(ax, -0.2*largest_string, 0.2*largest_string, cieling_color='#BBC4C2')

#--------------------------------------------------------------------#
# Animating the pendulum waves motion #
# animation might appear slow since video will be written on the fly #
# comment out writer.saving and writer.grab_frame to experiment #
#--------------------------------------------------------------------#
time_steps = solver_object_list[0].t
count_of_time_steps = len(time_steps)
pendulum_components_list = list(range(0, len(string_length_list)))
with writer.saving(fig, "pendulum_waves.mp4", dpi=200):
    for t_index in range(0, count_of_time_steps):
        for p_index, (pendulum_object, pendulum_xy) in enumerate(zip(pendulum_object_list, xy_list)):
            pendulum_components_list[p_index] = pendulum_object.draw_pendulum(ax, 
                                                                            pendulum_xy[0][t_index], 
                                                                            pendulum_xy[1][t_index], string_width=0.4)
        plt.pause(0.01)
        writer.grab_frame()
        if t_index != count_of_time_steps:
            for a_pendulum_components in pendulum_components_list:
                string, bob = a_pendulum_components
                string.remove()
                bob.remove()