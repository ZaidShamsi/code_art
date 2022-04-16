#Understanding the gradient of a function
#function considered - a sphere with radius of 5 z = f(x, y);
#z = sqrt(25-x^2- y^2)
#Let's start with contour plots of this surface
#contour plots are just the cross-section that you will get at a particular height ie z.
#so equation of our contour will be f(x, y) = some constant c.

#First let's consider z = 4x^2 + y^2
#contours will be y = sqrt(c - 4x^2)

from matplotlib import pyplot as plt
import numpy as np
import math
import turtle


wn = turtle.Screen()
#wn.setup(width = scalingFactor, height = scalingFactor)
zara = turtle.Turtle()
zara.speed(0)
print(wn.screensize())

x = np.linspace(-1.118033988749894, 1.118033988749894, 100)
y = np.sqrt(5-4*x**2)

scalingFactor = 30

x = x*scalingFactor
y = y*scalingFactor


for i in range(len(x)-1):
    zara.penup()
    zara.goto(x[i], y[i])
    zara.pendown()
    zara.goto(x[i+1], y[i+1])

    zara.penup()
    zara.goto(x[i], -y[i])
    zara.pendown()
    zara.goto(x[i+1], -y[i+1])



zara.penup()
zara.goto(math.sqrt(1.25)*scalingFactor, 0*scalingFactor)
zara.pendown()
zara.goto(math.sqrt(1.25)*8*scalingFactor, 0*scalingFactor)


zara.penup()
zara.goto(1*scalingFactor, 1*scalingFactor)
zara.pendown()
zara.goto(8*scalingFactor, 2*scalingFactor)


zara.penup()
zara.goto(0*scalingFactor, math.sqrt(5)*scalingFactor)
zara.pendown()
zara.goto(0*scalingFactor, math.sqrt(5)*2*scalingFactor)


wn.exitonclick()


'''
x = np.linspace(-0.5, 0.5, 100)
y = np.sqrt(1-4*x**2)
plt.plot(x, y)
plt.plot(x, -y)
'''

'''
x = np.linspace(-2, 2, 100)
y = np.sqrt(16-4*x**2)
plt.plot(x, y)
plt.plot(x, -y)

plt.plot(x, y)
plt.plot(x, -y)
plt.xlim(-4, 4)
plt.show()
'''
