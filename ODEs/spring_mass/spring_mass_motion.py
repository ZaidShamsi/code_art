import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FFMpegWriter
from spring_mass import SpringMass, calculate_spring_stiffness

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
metadata = dict(title='spring motion', artist='ZaidShamsi',
                comment='spring mass motion: single spring mass system')
writer = FFMpegWriter(fps=24, metadata=metadata)

# ffmpeg executable downloaded from https://github.com/BtbN/FFmpeg-Builds/releases for windows 64
# update the path to ffmpeg.exe (usually located in bin folder)
plt.rcParams['animation.ffmpeg_path'] = r'..\..\ffmpeg.exe'

#-------------------------------------------#
# initializing a spring mass #
#-------------------------------------------#
start_time = 0 # sec
end_time = 60 # sec
block_mass = 1 # kg
spring_1_stiffness = calculate_spring_stiffness(60, end_time, block_mass)
spring_thickness = spring_1_stiffness/10
block_color = '#6CB4EE' # argentinan blue
spring_mass_object = SpringMass(spring_constant=spring_1_stiffness, mass_of_block=block_mass, block_color=block_color)

#-------------------------------------------------------#
# solving for x of the mass using RK4 #
# solution object contains [x, v] #
#-------------------------------------------------------#
initial_x = 2 # m
initial_v = 0 # m/sec
solver_object = NumericalSolver(spring_mass_object.linear_sys_ODEs, [initial_x, initial_v], grid_size=1440,
                                      end_time=end_time, start_time=start_time)
solution_object = solver_object.RK4()
x = solution_object[:, 0]

#--------------------------------------------------#
# setting up figure and axis to plot spring mass #
#--------------------------------------------------#
fig = plt.figure(facecolor='black')
ax = fig.add_subplot(111)
# ax.set_title('Spring Mass system', fontsize=11, color='white')
ax.set_facecolor('black')
ax.set_aspect('equal')

#----------------------------------------#
# setting up spring and block parameters #
#----------------------------------------#
spring_x_left = 0
spring_x_right = 5
spring_y_centerline = 1
block_width = 0.5
block_height = 0.5
y_up = spring_y_centerline+0.5*block_height
y_down = spring_y_centerline-0.5*block_height

#----------------------------------------#
# drawing the wall #
#----------------------------------------#
spring_mass_object.draw_wall(ax, y_up=y_up, y_down=y_down, wall_color='#BBC4C2')

#--------------------------------------------------------------------#
# Animating the pendulum motion #
# animation might appear slow since video will be written on the fly #
# comment out writer.saving and writer.grab_frame to experiment #
#--------------------------------------------------------------------#
time_steps = solver_object.t
count_of_time_steps = len(time_steps)
with writer.saving(fig, "spring_mass_motion.mp4", dpi=200):
    for t_index in range(0, count_of_time_steps):
        if t_index % 1 == 0:
            spring_mass_components = spring_mass_object.draw_spring_mass(ax, spring_x_left=spring_x_left, 
                                                                                spring_x_right=spring_x_right+x[t_index], 
                                                                                spring_y_centerline=spring_y_centerline,
                                                                                spring_thickness = spring_thickness,
                                                                                block_width=block_width, 
                                                                                block_height=block_height)
            plt.pause(0.01)
            writer.grab_frame()
            if t_index != (count_of_time_steps-1):
                spring, block = spring_mass_components
                spring.remove()
                block.remove()

plt.show()