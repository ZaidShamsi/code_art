import numpy as np
from matplotlib import pyplot as plt

#given step size,
dx = np.pi/8;
#given limits of x domain,
xmin = -np.pi/2;
xmax = np.pi/2;
#x vector,
x = np.arange(start=xmin, stop=xmax, step=dx);
uo = np.cos(x)

print(x, uo)

#plt.plot(x, uo)
#plt.show()
