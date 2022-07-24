import numpy
from matplotlib import pyplot as plt

def gaussianIntegral(x):
    fx = 2*(numpy.exp(-x*x) + (numpy.exp(-1/(x*x)))/(x*x))
    return fx

eval = gaussianIntegral(2)
print(eval)

outerIter = 10000
innerIter = 1000
avgLst = []


for o in range(0, outerIter):
    sum = 0
    for i in range(0, innerIter):
        randNum = numpy.random.random()
        sum = sum + gaussianIntegral(randNum)
    avg = sum/innerIter
    avgLst.append(avg)

print(avgLst)

plt.hist(avgLst, bins = 100, ec = 'k')
plt.vlines(1.77, 0, 80, color = 'k', linewidth = 2.0, label = r'$\sqrt{\pi} = 1.77245$')
plt.xlabel(r'Integral Value = $\sqrt{\pi}$')
plt.ylabel('Frequency')
plt.title(r'Evaluation of Gaussian Integral $I = \int_{-\infty}^{\infty} e^{-x^2}$ using Monte Carlo Method')
plt.legend()
plt.show()
