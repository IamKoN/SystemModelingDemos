from pylab import *

r1 = 0.1
r2 = 0.3

K1 = 80.0
K2 = 50.0

Dt = 0.01

def initialize(x0, y0):
    global x, y, xresult, yresult, t, timesteps
    x0 = 1.2
    y0 = 1.5
    x = x0
    y = y0
    xresult = [x]
    yresult = [y]

    t = 0.
    timesteps = [t]

def observe():
    global x, y, xresult, yresult, t, timesteps
    xresult.append(x)
    yresult.append(y)
    timesteps.append(t)

def update():
    global x, y, xresult, yresult, t, timesteps
    nextx = x + r1 * x * (1 - x / K1) * Dt
    nexty = y + r2 * y * (1 - y / K2) * Dt
    x = nextx
    y = nexty
    t = t + Dt

for x0 in arange(0, 2, .1):
    for y0 in arange(0, 2, .1):
        initialize(x0, y0)
        while t < 50.:
            update()
            observe()
        plot(xresult, yresult)

show()
plot(timesteps, xresult)
show()





