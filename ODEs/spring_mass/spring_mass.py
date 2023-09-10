import numpy as np
from matplotlib.patches import Rectangle

class SpringMass:
    def __init__(self, spring_constant, mass_of_block, block_color):
        self.spring_constant = spring_constant
        self.mass_of_block = mass_of_block
        self.block_color = block_color

    def linear_sys_ODEs(self, y):
        # sysODEs -> Set of ordinary differential equations governing pendulum motion
        # y -> [initial_x, initial_v] -> Initial conditons when pendulum motion starts
        # y[1] -> v -> dx/dt
        # y[0] -> x
        omega_square = (self.spring_constant/self.mass_of_block)
        f = [y[1], -omega_square*y[0]]
        return f
    
    def draw_wall(self, axes_object, y_up, y_down, wall_color='black'):
        wall, = axes_object.plot([0, 0], [y_up, y_down], linewidth=4, color=wall_color)
        return wall

    def draw_spring_mass(self, axes_object, spring_x_left, spring_x_right, spring_y_centerline, spring_thickness,
                         block_width, block_height):
        number_of_zig_zag = 12
        spring_x = np.linspace(spring_x_left, spring_x_right, number_of_zig_zag)
        factor = int((number_of_zig_zag-2)/2)
        spring_y = [spring_y_centerline] + factor*[spring_y_centerline+0.5*block_height, spring_y_centerline-0.5*block_height] + [spring_y_centerline]
        spring, = axes_object.plot(spring_x, spring_y,
                                   color=self.block_color, linewidth=spring_thickness)
        # block
        block = axes_object.add_patch(Rectangle((spring_x_right, (spring_y_centerline-0.5*block_height)),
                                                 block_width, block_height, color =self.block_color))
        spring_mass_components = [spring, block]
        return spring_mass_components
    

def calculate_spring_stiffness(n, t, m):
    # n, t -> number of oscillations in t seconds
    # t/n = Time period of simple pendulum
    k = m*((2*np.pi*n)/t)**2
    return k