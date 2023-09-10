import numpy as np

g = 9.81 # m/sec^2

class Pendulum:
    def __init__(self, length_of_string, radius_of_bob, bob_color):
        self.length_of_string = length_of_string
        self.radius_of_bob = radius_of_bob
        self.bob_color = bob_color

    def linear_sys_ODEs(self, y):
        # sysODEs -> Set of ordinary differential equations governing pendulum motion
        # y -> [initial_theta, initial_omega] -> Initial conditons when pendulum motion starts
        # theta -> angular position of pendulum
        # omega -> angular velocity of pendulum
        alpha = -(g*self.length_of_string) / (0.5*self.radius_of_bob**2 + self.length_of_string**2)
        f = [y[1], alpha*y[0]]
        return f

    def non_linear_sys_ODEs(self, y):
        alpha = -(g*self.length_of_string) / (0.5*self.radius_of_bob**2 + self.length_of_string**2)
        f = [y[1], alpha*np.sin(y[0])]
        return f

    def get_cartesian_coordinates(self, theta):
        xy = [self.length_of_string*np.sin(theta), -self.length_of_string*np.cos(theta)]
        return xy
    
    def draw_ceiling(self, axes_object, x_left, x_right, cieling_color='black'):
        ceiling, = axes_object.plot([x_left, x_right], [0, 0], linewidth=4, color=cieling_color)
        return ceiling

    def draw_pendulum(self, axes_object, x, y, string_width):
        string, = axes_object.plot([0, x], [0, y], color=self.bob_color, linewidth=string_width)
        # bob
        theta = np.linspace(0, 2*np.pi, 40)
        xCircle = x + self.radius_of_bob*np.cos(theta)
        yCircle = y + self.radius_of_bob*np.sin(theta)
        bob, = axes_object.fill(xCircle, yCircle, color=self.bob_color)
        pendulum_components = [string, bob]
        return pendulum_components
    

def calculate_pendulum_string_length(n, t):
    # n, t -> number of oscillations in t seconds
    # t/n = Time period of simple pendulum
    L = g*(t/(2*np.pi*n))**2
    return L