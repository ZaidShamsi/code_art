import numpy as np
from matplotlib import pyplot as plt

xAirfoil = np.array([])
yAirfoil = np.array([])

xCamber = np.array([])
yCamber = np.array([])

fAirfoil = open('0714Airfoil.txt')
fCamber = open('0714Camber.txt')

for l in fAirfoil:
    xAirfoil = np.append(xAirfoil, float(l.split()[0]))
    yAirfoil = np.append(yAirfoil, float(l.split()[1]))

for l in fCamber:
    xCamber = np.append(xCamber, float(l.split()[0]))
    yCamber = np.append(yCamber, float(l.split()[1]))

hfont = {'fontname':'Helvetica'}

#plt.subplot(2, 1, 1)
plt.plot(xAirfoil, yAirfoil, marker = '.', color = 'brown', linestyle = 'None')
plt.xlim([-0.05, 1.05])
plt.xlabel('x\c', fontweight = 'bold', **hfont)
plt.ylabel('t\c', fontweight = 'bold', **hfont)
#plt.grid(b = True, which = 'major', linestyle = '-')
#plt.grid(b = True, which = 'minor', linestyle = ':')
#plt.minorticks_on()

'''
plt.subplot(2, 1, 2)
plt.plot(xCamber, yCamber, color = 'brown')
plt.xlim([0, 1])
plt.xlabel('x\c', fontweight = 'bold', **hfont)
plt.ylabel('z\c', fontweight = 'bold', **hfont)
plt.grid(b = True, which = 'major', linestyle = '-')
plt.grid(b = True, which = 'minor', linestyle = ':')
plt.minorticks_on()
'''

#plt.tight_layout()
plt.show()
