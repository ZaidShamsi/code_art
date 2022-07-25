from matplotlib import pyplot as plt
import numpy as np

# number of particles constituting inner circle
n = 361;

# radius of outer circle
R = 10;

# radius of inner circle
r = R/(1 + 1);

# angular velocity of inner circle
w = 10;

# velocity of inner circle center
v = w*r;

# time for whole animation
t = 2*np.pi*(R-r)/v;

# outer length
o_l = 0.5*r;

def plotCircle(r, n, xShift, yShift):
    theta = np.linspace(0, 2*np.pi, n);
    x = xShift + r*np.cos(theta);
    y = yShift + r*np.sin(theta);
    circleHandle, = plt.plot(x, y, color=(1, 173/255, 1/255), linewidth=1.0);
    return circleHandle

plt.axis('equal')
plt.axis('off')
factor = 1.1;
plt.xlim([-factor*(R+o_l), factor*(R+o_l)])
plt.ylim([-factor*(R+o_l), factor*(R+o_l)])
outerCircle = plotCircle(R, n, 0, 0)
centerCircle = plotCircle((R-r), n, 0, 0)

# horizontal line
h_line = plt.plot([0, 0], [-R, R], color=(1, 173/255, 1/255), linewidth=1.0)

# vertical line
v_line = plt.plot([-R, R], [0, 0], color=(1, 173/255, 1/255), linewidth=1.0)

discretized_t = np.linspace(0, t, 140);
thetaPlanet = np.linspace(0, 2*np.pi, 50);

# logic to roll the circle
for i in range(0, len(discretized_t)):
    if i == 0:
        theta = np.linspace(0, 2*np.pi, 361);
    elif i > 0 and i <= len(discretized_t):
        theta = theta - w*(discretized_t[i]-discretized_t[i-1]);
    xShift = (R-r)*np.cos(w*discretized_t[i]);
    yShift = (R-r)*np.sin(w*discretized_t[i]);
    xX = r*np.cos(theta);
    yY = r*np.sin(theta);
    xX = xShift + xX;
    yY = yShift + yY;

    xX_0 = xShift + (r+o_l)*np.cos(theta[1]);
    yY_0 = yShift + (r+o_l)*np.sin(theta[1]);

    xX_90 = xShift + (r+o_l)*np.cos(theta[90]);
    yY_90 = yShift + (r+o_l)*np.sin(theta[90]);

    xX_180 = xShift + (r+o_l)*np.cos(theta[181]);
    yY_180 = yShift + (r+o_l)*np.sin(theta[181]);

    xX_270 = xShift + (r+o_l)*np.cos(theta[270]);
    yY_270 = yShift + (r+o_l)*np.sin(theta[270]);

    l_h, = plt.plot([xX_180, xX_0], [yY_180, yY_0], color=(1, 173/255, 1/255), linewidth=1.0)
    l_v, = plt.plot([xX_270, xX_90], [yY_270, yY_90], color=(1, 173/255, 1/255), linewidth=1.0)

    # small circle at theta = 0 degree
    sC_0 = plotCircle(r/20, n, xX[theta == theta[1]], yY[theta == theta[1]]);
    x_circle_0 = xX_0 + r/25*np.cos(thetaPlanet);
    y_circle_0 = yY_0 + r/25*np.sin(thetaPlanet);
    planet_0, = plt.fill(x_circle_0, y_circle_0, color=(1, 173/255, 1/255));

    # small circle at theta = 90 degree
    sC_piby2 = plotCircle(r/20, n, xX[theta == theta[90]], yY[theta == theta[90]]);
    x_circle_1 = xX_90 + r/25*np.cos(thetaPlanet);
    y_circle_1 = yY_90 + r/25*np.sin(thetaPlanet);
    planet_1, = plt.fill(x_circle_1, y_circle_1, color=(1, 173/255, 1/255));

    sC_pi = plotCircle(r/20, n, xX[theta == theta[181]], yY[theta == theta[181]]);
    x_circle_2 = xX_180 + r/25*np.cos(thetaPlanet);
    y_circle_2 = yY_180 + r/25*np.sin(thetaPlanet);
    planet_2, = plt.fill(x_circle_2, y_circle_2, color=(1, 173/255, 1/255));

    sC_3piby2 = plotCircle(r/20, n, xX[theta == theta[270]], yY[theta == theta[270]]);
    x_circle_3 = xX_270 + r/25*np.cos(thetaPlanet);
    y_circle_3 = yY_270 + r/25*np.sin(thetaPlanet);
    planet_3, = plt.fill(x_circle_3, y_circle_3, color=(1, 173/255, 1/255));

    if i > 0:
        plt.plot([xX_0, xX_0_Old], [yY_0, yY_0_Old], color=(1, 173/255, 1/255), linewidth=1.0)
        plt.plot([xX_90, xX_90_Old], [yY_90, yY_90_Old], color=(1, 173/255, 1/255), linewidth=1.0)
        plt.plot([xX_180, xX_180_Old], [yY_180, yY_180_Old], '-',  color=(1, 173/255, 1/255), linewidth=1.0)
        plt.plot([xX_270, xX_270_Old], [yY_270, yY_270_Old], '-',  color=(1, 173/255, 1/255), linewidth=1.0)

    innerCircle, = plt.plot(xX, yY, color=(1, 173/255, 1/255));

    xX_0_Old = xX_0;
    yY_0_Old = yY_0;

    xX_90_Old = xX_90;
    yY_90_Old = yY_90;

    xX_180_Old = xX_180;
    yY_180_Old = yY_180;

    xX_270_Old = xX_270;
    yY_270_Old = yY_270;

    plt.pause(0.001)

    # deleting the previously drawn curves to create an animation effect
    if i != len(discretized_t):
        innerCircle.remove()
        sC_0.remove()
        sC_piby2.remove()
        sC_pi.remove()
        sC_3piby2.remove()
        l_h.remove()
        l_v.remove()
        planet_0.remove()
        planet_1.remove()
        planet_2.remove()
        planet_3.remove()

plt.show()
