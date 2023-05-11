from matplotlib import pyplot as plt
import numpy as np

# Given lenghts of the four links:
# a is the length of link O1A
a = 0.3
# d is the length of O1O2
d = 0.5
# b is the length of link AB
b = 0.5
# c is the length of link O2B
c = 0.3
# r is the location of point tracing the curve on link AB
r = b/2

phi = np.linspace(0, 2*np.pi, 181) # rad

# Co-oridnates of point O1
# O1 is the fixed pin on left
xO1 = 0;
yO1 = 0;

# Co-ordinates of point A
xA = a*np.cos(phi);
yA = a*np.sin(phi);

# Co-ordinates of point O2
# O2 is the fixed pin on right
xO2 = d;
yO2 = 0;

# Construct line AO2,
# len of AO2
AO2 = np.sqrt((xA-xO2)**2 + (yA-yO2)**2);

# Angle alpha,
# Alpha is the angle between AO2 and O1O2
cos_alpha = (AO2**2 + d**2 - a**2) / (2*AO2*d)
cos_alpha = np.where(cos_alpha<1.0, cos_alpha, 1.0)
alpha = np.arccos(cos_alpha)

# Angle theta
# Theta is the angle between AO2 and BO2
cos_theta = (AO2**2 + c**2 - b**2) / (2*AO2*c)
cos_theta = np.where(cos_theta<1.0, cos_theta, 1.0)
theta = np.arccos(cos_theta)

# Preallocating delta
delta = np.zeros(len(phi))

# Defining delta
# Delta is the angle made by the link BO2 with x axis
delta[phi <= np.pi] = np.pi + (-alpha[phi <= np.pi] + theta[phi <= np.pi])
delta[phi >= np.pi] = np.pi - (theta[phi >= np.pi] - alpha[phi >= np.pi])

# Coordinates of point B
xB = d + c*np.cos(delta);
yB = c*np.sin(delta);

# Slope of line AB
gamma = np.arctan((yB - yA)/(xB - xA));

# Co-ordiantes of point P
xP = xA + r*np.cos(gamma);
yP = yA + r*np.sin(gamma);

plt.axis('equal')
plt.xlim([-0.5, 1.0])
plt.ylim([-0.5, 1.0])
plt.axis('off')

def plotCircle(center, radius):
    theta = np.linspace(0, 2*np.pi, 361);
    x = center[0] + radius*np.cos(theta);
    y = center[1] + radius*np.sin(theta);
    circleHandle, = plt.plot(x, y, color='r', linewidth=1.0);
    return circleHandle

# Drawing pin joints at O1 and O2
plotCircle([xO1, yO1], 0.01)
plotCircle([xO2, yO2], 0.01)

# Animating the mechanism
for i in range(0, len(phi)):
    pinP = plotCircle([xP[i], yP[i]], 0.01)
    crank1, = plt.plot([0, xA[i]], [0, yA[i]], 'k', linewidth=1.5);
    coupler, = plt.plot([xA[i], xB[i]], [yA[i], yB[i]], 'k', linewidth=1.5);
    crank2, = plt.plot([xB[i], xO2], [yB[i], yO2], 'k', linewidth=1.5);
    pointP = plt.plot(xP[i], yP[i], color = 'k', marker='.', markersize = 1.0);
    plt.pause(0.0001)
    if i != len(phi):
        pinP.remove()
        crank1.remove()
        coupler.remove()
        crank2.remove()

plt.show()
