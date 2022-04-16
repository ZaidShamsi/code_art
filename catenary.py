#python program to calculate hyperbolic cosine from first principles.
from matplotlib import pyplot as plt
import numpy as np
import math

#Angle value for which hyperbolic cosine needs to be calculated
beta = 1.5

#Initializing sum variable to store sum of terms
sum = 0

#Taking input from the user for precision
precision = float(input('Enter the required level of precision\n'))

#Initializing error variable to compare with precision
error = 0.1

#Making sure that precision is less than error to ensure that next while loop run at least once
while precision > error:
    precision = float(input('Level of precision should be at least less than 0.1. Kindly enter again\n'))

i = 0
while error > precision:
    term = beta**i/np.math.factorial(i)
    hyperbolicCosine = sum + term
    error = hyperbolicCosine - sum
    sum = hyperbolicCosine
    i += 2

print('The value of cosh({}) is equal to {}.'.format(beta, hyperbolicCosine))

#The above is not a funciton, you can not call it with every value of beta like you do in your calculator.
#What you can do with the above piece of code is to by hand change the value of beta (in line 7) then
#print the result that is being stored in the variable 'hyperbolicCosine' after evey iteration (in line 25).
#Therefore in the part 2 we will defien a fucntion for the same cause.

#---------------------------------------------------------------------------------------------------------#
#Part 2
#defining a hyperbolic cosine function to use in plotting catenary curves.
def hyperbolicCosine(beta, precision = 1e-05):
    sum = 0
    error = 0.1
    for i in range(0, 10000, 2):
        term = beta**i/math.factorial(i)
        hyperbolicCosine = sum + term
        error = hyperbolicCosine - sum
        sum = hyperbolicCosine
        if np.any(error) > precision:
            continue
        else:
            break

    return hyperbolicCosine
#-----------------------------------------------------------------------------------------------------------#
#Part 3
#catenary curve
xStart = float(input('''Enter the starting point of 'x'\n'''))
xEnd = float(input('''Enter the end point of 'x'\n'''))
xIncrement = float(input('''Enter the incremental value for 'x'\n'''))

aStart = float(input('''Enter the starting point of 'a'\n'''))
#a while loop to ensure "'a' Minimum" is greater than 0
while aStart < 0:
    aStart = float(input('''Minimum value of 'a' should be greater than 0. Kindly enter again\n'''))

aEnd = float(input('''Enter the end point of 'a'\n'''))
aIncrement = float(input('''Enter the incremental value for 'a'\n'''))

xPoints = int((xEnd - xStart)/xIncrement + 1)
aPoints = int((aEnd - aStart)/aIncrement + 1)

x = np.linspace(xStart, xEnd, xPoints)
a = np.linspace(aStart, aEnd, aPoints)

for aValue in a:
    y = aValue * hyperbolicCosine(x/aValue)
    plt.plot(x, y, label = 'a = {}'.format(aValue))

plt.xlim(xEnd, xStart)
#plt.ylim(1, 4)

plt.xlabel('Position(x)')
plt.ylabel('Amplitude(y)')
plt.title('Catenary curves')

plt.grid()
plt.legend()

plt.show()
