from matplotlib import pyplot as plt
import numpy as np

# Radius of outer circle
R = 4.245069933;

# Radius of inner cycle
r = 1;

# Angular speed of outer cycle
wR = 0.1;

# Angular speed of inner cycle
wr = 0.8;

# time for the total animation
t = np.linspace(0, 40*np.pi, 500);

# using theta = angular velocity * time
thetaR = wR*t;
thetar = wr*t;

# co-ordinates for tracing out circles
X = R*np.cos(thetaR);
Y = R*np.sin(thetaR);

x = r*np.cos(thetar);
y = r*np.sin(thetar);

plt.plot(X, Y, color=(128/255, 0, 0, 0.8))
plt.axis('equal')
plt.xlim([-1.1*(R), 1.1*(R)])
plt.ylim([-1.1*(R), 1.1*(R)])
plt.plot(x, y, color=(153/255, 0, 0, 0.4))
plt.axis('off')

thetaPlanet = np.linspace(0, 2*np.pi, 50)

# logic for revolution
for i in range(0, len(t)):
    line = plt.plot([X[i], x[i]], [Y[i], y[i]], color=(1, 0, 0, 0.2), linewidth=1.0)

    # Planet outer
    XCircle = X[i] + (R/20)*np.cos(thetaPlanet)
    YCircle = Y[i] + (R/20)*np.sin(thetaPlanet)
    planet1, = plt.fill(XCircle, YCircle, color=(128/255, 0, 0))

    # Planet inner
    xCircle = x[i] + (r/20)*np.cos(thetaPlanet)
    yCircle = y[i] + (r/20)*np.sin(thetaPlanet)
    planet2, = plt.fill(xCircle, yCircle, color=(153/255, 0, 0))

    plt.pause(0.001)

    if i != len(t):
        planet1.remove()
        planet2.remove()

plt.show()
