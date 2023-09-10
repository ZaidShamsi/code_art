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
oscillations_list = np.linspace(60, 71, 12)
start_time = 0 # sec
end_time = 60 # sec
block_mass = 1 # kg
spring_stiffness_list = [calculate_spring_stiffness(n, end_time, block_mass) for n in oscillations_list]
spring_thickness_list = [spring_stiffness/100 for spring_stiffness in spring_stiffness_list]
air_superiority_blue = '#72A0C1'
celeste = '#B2FFFF'
light_sky_blue = '#87CEFA'
magic_blue = '#0077c0'
block_color_list = 3*[air_superiority_blue, celeste, light_sky_blue, magic_blue]
spring_mass_object_list = [SpringMass(spring_constant=spring_stiffness, mass_of_block=block_mass, block_color=block_color_e)
                           for spring_stiffness, block_color_e in zip(spring_stiffness_list, block_color_list)]

#-------------------------------------------------------#
# solving for x of the mass using RK4 #
# solution object contains [x, v] #
#-------------------------------------------------------#
initial_x = 1 # m
initial_v = 0 # m/sec
x_list = list(range(0, len(spring_stiffness_list)))
for index, spring_mass_object in enumerate(spring_mass_object_list):
    solver_object = NumericalSolver(spring_mass_object.linear_sys_ODEs, [initial_x, initial_v], grid_size=1440,
                                        end_time=end_time, start_time=start_time)
    solution_object = solver_object.RK4()
    x_list[index] = solution_object[:, 0]

#--------------------------------------------------#
# setting up figure and axis to plot spring mass #
#--------------------------------------------------#
fig = plt.figure(facecolor='black')
ax = fig.add_subplot(111)
ax.set_facecolor('black')
ax.set_aspect('equal')

#----------------------------------------#
# setting up spring and block parameters #
#----------------------------------------#
spring_x_left = 0
spring_x_right = 11
block_width = 0.5
block_height = block_width
spring_y_centerline_list = np.linspace(-1.5, 1.5, 12)
block_width = spring_y_centerline_list[1]-spring_y_centerline_list[0]
block_height = block_width
y_up_list = spring_y_centerline_list+0.5*block_height
y_down_list = spring_y_centerline_list-0.5*block_height

#----------------------------------------#
# drawing the wall #
#----------------------------------------#
for index, spring_mass_object in enumerate(spring_mass_object_list):
    spring_mass_object.draw_wall(ax, y_up=y_up_list[index], y_down=y_down_list[index], wall_color='#BBC4C2')

#--------------------------------------------------------------------#
# Animating the pendulum motion #
# animation might appear slow since video will be written on the fly #
# comment out writer.saving and writer.grab_frame to experiment #
#--------------------------------------------------------------------#
time_steps = solver_object.t
count_of_time_steps = len(time_steps)
spring_mass_components_list = list(range(0, len(spring_stiffness_list)))

with writer.saving(fig, "spring_mass_waves.mp4", dpi=200):
    for t_index in range(0, count_of_time_steps):
        if t_index % 1 == 0:
            for s_index, (spring_object, x) in enumerate(zip(spring_mass_object_list, x_list)):
                spring_mass_components_list[s_index] = spring_object.draw_spring_mass(ax, spring_x_left=spring_x_left, 
                                                                                    spring_x_right=spring_x_right+x[t_index], 
                                                                                    spring_y_centerline=spring_y_centerline_list[s_index],
                                                                                    spring_thickness = spring_thickness_list[s_index],
                                                                                    block_width=block_width, 
                                                                                    block_height=block_height)
            plt.pause(0.01)
            writer.grab_frame()
            if t_index != (count_of_time_steps-1):
                for a_spring_components in spring_mass_components_list:
                    spring, block = a_spring_components
                    spring.remove()
                    block.remove()

plt.show()