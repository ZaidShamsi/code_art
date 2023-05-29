import math
import numpy as np
import turtle

drawing_board = turtle.Screen()
drawing_board.setup(width = 1.0, height = 1.0)

turtle.shape("circle")
turtle.shapesize(0.1, 0.1)
turtle.speed(0)

class projectile:
    """First time I am trying to create class. I have named this class 'projectile'."""

    def __init__(self, velocity, theta):
        self.velocity = velocity
        self.theta = math.radians(theta)
        self.t_vec = np.linspace(0, self.time_of_flight(), 101)

    def time_of_flight(self):
        T = 2*self.velocity*math.sin(self.theta)/9.81
        return T

    def x_coordinates(self):
        x = self.velocity*math.cos(self.theta)*self.t_vec
        return x

    def y_coordinates(self):
        y = self.velocity*math.sin(self.theta)*self.t_vec - 0.5*9.81*self.t_vec**2
        return y

    def draw(self):
        x = self.x_coordinates()
        y = self.y_coordinates()
        for i in range(len(self.t_vec)):
            turtle.goto(x[i], y[i])

for i in range(10, 180, 10):
    my_projectile = projectile(60, i)
    my_projectile.draw()

drawing_board.exitonclick()
