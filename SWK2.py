import numpy as np

# Value at which cos is needed to be evaluated
x = 0.3 * np.pi

# Actual value of cos(x)
actualVal = np.cos(x)

# Initializing the variable to store the sum of terms of Maclaurin series
macVal1 = 1

# Tolerance value based on number of significant digits required
epsilon = 1*10**(-9)

# Sum of first two terms of Maclaurin series
macVal2 = macVal1 + (-1)**1*x**(2*1)/np.math.factorial(2*1)

# Calculating the error (difference between exact value and value obtained
# by Maclaurin terms approximation)
error = abs(macVal2 - macVal1)

# Initializing the iterator
i = 2

while error > epsilon:
    macVal1 = macVal2
    macVal2 = macVal1 + (-1)**i*x**(2*i)/np.math.factorial(2*i)
    error = abs(macVal2 - macVal1)
    i = i + 1

print(macVal1)
print(macVal2)
print(np.cos(x))
print(i)
