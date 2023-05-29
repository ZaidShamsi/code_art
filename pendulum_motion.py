from matplotlib import pyplot as plt
import numpy as np
import math

class Pendulum:
    def __init__(self, length_of_string, radius_of_bob, initial_theta, initial_omega):
        # theta -> angular position of pendulum
        # omega -> angular velocity of pendulum
        self.length_of_string = length_of_string
        self.radius_of_bob = radius_of_bob
        self.initial_theta = np.deg2rad(initial_theta)
        self.initial_omega = initial_omega

    def sysODEs(self, y):
        # sysODEs -> Set of ordinary differential equations governing pendulum motion
        # y -> Initial conditons -> [initial_theta, initial_omega]
        g = 9.81
        alpha = -(g*self.length_of_string) / (0.5*self.radius_of_bob**2 + self.length_of_string**2)
        f = [y[1], alpha*y[0]]
        return f

    def getCartesianCoordinates(self, theta):
        x = [self.length_of_string*np.sin(theta), -self.length_of_string*np.cos(theta)]
        return x

    def draw(self, x, y):
        string, = plt.plot([0, x], [0, y], color='k', linewidth=1.0)
        # bob
        theta = np.linspace(0, 2*np.pi, 40)
        xCircle = x + self.radius_of_bob*np.cos(theta);
        yCircle = y + self.radius_of_bob*np.sin(theta);
        bob, = plt.fill(xCircle, yCircle, color='b');
        pendulum_components = [string, bob]
        return pendulum_components

class NumericalSolver(Pendulum):
    def __init__(self, length_of_string, radius_of_bob, initial_theta=20, initial_omega=0, number_of_equations=2, grid_size=600, to_t=30, from_t=0):
        super().__init__(length_of_string, radius_of_bob, initial_theta, initial_omega)
        self.number_of_equations = number_of_equations
        self.t = np.linspace(from_t, to_t, grid_size)

    def RK4(self):
        # RK4 Numerical method is used to solve the second order ODE of simple pendulum
        # k are the slope approximations used in RK4 method
        k = np.zeros((4, self.number_of_equations));

        # step size
        h = self.t[1] - self.t[0]

        # y is solution vector
        # In case of simple pendulum we have only two variables theta, omega
        # So, structure of y goes like y = [theta, omega]
        # preallocating the solution vector
        y = np.zeros((len(self.t), self.number_of_equations));

        # initial values
        y[0, :] = [self.initial_theta, self.initial_omega];

        # Implementing RK4 method
        for j in range(0, len(self.t)-1):
            if math.isnan(y[j, 0]) is True:
                print(self.sysODEs(y))
                print(j)
                break
            for i in range(0, len(k)):
                if i == 0:
                    k[i, :] = self.sysODEs(y[j, :]);
                elif i == 3:
                    k[i, :] = self.sysODEs(y[j, :] + k[i-1, :]*h);
                else:
                    k[i, :] = self.sysODEs(y[j, :] + k[i-1, :]*0.5*h);
            y[j+1, :] = y[j, :] + (1/6)*(k[0, :] + 2*(k[1, :]+k[2, :]) + k[3, :])*h
        return y

string_length_list = np.arange(10, 1, -1)
bob_radii_list = string_length_list/20

pendulum_object_list = [NumericalSolver(string_length_list[i], bob_radii_list[i]) for i in range(0, len(string_length_list))]
solution_list = [pendulum_object_list[i].RK4() for i in range(0, len(pendulum_object_list))]
theta_list = [solution_list[i][:, 0] for i in range(0, len(solution_list))]
x_list = [pendulum_object_list[i].getCartesianCoordinates(theta_list[i]) for i in range(0, len(theta_list))]

plt.axis('equal')
plt.axis('off')
axis_resize_factor = 1.5
largeString = max(string_length_list)
plt.xlim(axis_resize_factor*np.array([-largeString, largeString]))
plt.ylim(axis_resize_factor*np.array([-largeString, largeString]))
cieling_list = np.linspace(-2, 2, 10)
plt.plot([cieling_list[0], cieling_list[-1]], [0, 0], color='k')
for i in range(0, len(cieling_list)):
    plt.plot([cieling_list[i], cieling_list[i]+0.3], [0, 0.5], color='k')

# Animating the pendulum motion
# Initializing the list
pendulum_components_list = list(range(0, len(string_length_list)))
for i in range(0, len(pendulum_object_list[0].t)):
    for j in range(0, len(pendulum_object_list)):
        pendulum_components_list[j] = pendulum_object_list[j].draw(x_list[j][0][i], x_list[j][1][i])
    plt.pause(0.01);
    if i != len(pendulum_object_list[0].t):
        for j in range(0, len(pendulum_components_list)):
            pendulum_components_list[j][0].remove()
            pendulum_components_list[j][1].remove()
