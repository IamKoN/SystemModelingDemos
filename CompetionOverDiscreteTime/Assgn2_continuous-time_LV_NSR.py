# Simulate the following continuous-time Lotka-Volterra (predatorprey)
# model for 0  t < 50 in Python, with x(0) = y(0) = 0:1, a = b = c = d = 1 and t = 0:01.
# Visualize the simulation results over time and also in a phase space.
# dx / dt = ax - bxy    dy / dt = -cy + dxy
# Then try to reduce the value of t to even smaller values and see how the simulation results are affected by such changes.

from pylab import *

a = b = c = d = 1.0
Dt = 0.01

def init():
    global x, xresult, y, yresult, t, timesteps
    x = y = 0.1
    t = 0.
    xresult = [x]
    yresult = [y]
    timesteps = [t]
    
def observe():
    global x, xresult, y, yresult, t, timesteps
    xresult.append(x)
    yresult.append(y)
    timesteps.append(t)

def update():
    global x, xresult, y, yresult, t, timesteps
    nextx = x + (a * x - b * x * y) * Dt
    nexty = y + (- c * y + d * x * y) * Dt
    x, y = nextx, nexty
    t = t + Dt

init()
while t < 50.:
    update()
    observe()

plot(timesteps, xresult, 'b')
plot(timesteps, yresult, 'r')
show()
plot(xresult, yresult, 'g')
show()
