# Simple Pendulum
This project started with me wanting to code for pendulum waves.

Important reads:
- [The Simple Pendulum (Pennsylvania State University)](https://www.acs.psu.edu/drussell/Demos/Pendulum/Pendula.html) I found this page while surfing and its amazing. I ended up recreatig all of its animations.
- [Pendulum wave (Wikipedia)](https://en.wikipedia.org/wiki/Pendulum_wave)
- [Runge-Kutta methods (Wikipedia)](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods)

# Equations
- Differential equation
  - $\frac{d^{2}\theta}{dt^{2}} + \frac{g}{L}sin(\theta) = 0$
- Converting it into two first order equations
  - $\frac{d\theta}{dt}=\omega$
  - $\frac{d\omega}{dt}=-\frac{g}{L}sin(\theta)$
- Small angle approximation
  - $sin(\theta) \approxeq \theta$


# Output
## Execution work product of [pendulum_waves.py](pendulum_waves.py) module.
Linear ordinary differential equations (ODEs) are solved for $\theta = 10 \degree$.

https://github.com/ZaidShamsi/code_art/assets/103277308/36c085c8-101d-4caf-ad84-01e43e62b41e

## Execution work product of [linear_pendulum_motion.py](linear_pendulum_motion.py) module. 
This compares and captures the proportionality of time period of simple pendulum on string length. Again, linear ordinary differential equations (ODEs) are solved for $\theta = 10 \degree$

https://github.com/ZaidShamsi/code_art/assets/103277308/a88e68d3-cec8-4980-87b8-ba335718ad75

## Execution work product of [linear_and_non_linear_pendulum_motion.py](linear_and_non_linear_pendulum_motion.py) module. 
This captures the effect of approximation of $sin(\theta) \approxeq \theta$ for small angles. Notice that for $\theta = 10 \degree$ approximation provides acceptable results.

https://github.com/ZaidShamsi/code_art/assets/103277308/cb9d3c40-2db3-40dd-8910-76a84ce43266
