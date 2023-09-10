import numpy as np
import math

class NumericalSolver():
    def __init__(self, sys_ODEs, initial_conditions, grid_size=1440, 
                 end_time=60, start_time=0):
        # sys_ODEs -> system of ordinary differential equations to be solved
        # initial_conditions -> a list of initial conditions for ODEs
        self.sys_ODEs = sys_ODEs
        self.initial_conditions = initial_conditions
        self.number_of_equations = len(self.initial_conditions)
        self.t = np.linspace(start_time, end_time, grid_size)

    def RK4(self):
        # RK4 Numerical method is used to solve the second order ODE of simple pendulum
        # k are the slope approximations used in RK4 method
        k = np.zeros((4, self.number_of_equations))

        # step size
        h = self.t[1] - self.t[0]

        # y is solution vector
        # In case of simple pendulum we have only two variables theta, omega
        # So, structure of y goes like y = [theta, omega]
        # preallocating the solution vector
        y = np.zeros((len(self.t), self.number_of_equations))

        # initial values
        y[0, :] = self.initial_conditions

        # Implementing RK4 method
        for j in range(0, len(self.t)-1):
            if math.isnan(y[j, 0]) is True:
                print(self.sys_ODEs(y))
                print(j)
                break
            for i in range(0, len(k)):
                if i == 0:
                    k[i, :] = self.sys_ODEs(y[j, :])
                elif i == 3:
                    k[i, :] = self.sys_ODEs(y[j, :] + k[i-1, :]*h)
                else:
                    k[i, :] = self.sys_ODEs(y[j, :] + k[i-1, :]*0.5*h)
            y[j+1, :] = y[j, :] + (1/6)*(k[0, :] + 2*(k[1, :]+k[2, :]) + k[3, :])*h
        return y