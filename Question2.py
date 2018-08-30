import matplotlib
matplotlib.use('TkAgg')
from pylab import *
import copy as cp

geoDR = 0.9 #geometric/exponential decay rate of fans
linDR = 0.1 # decay rate of fans
linGR = 0.1 # growth rate of fans

r = 0.1 # init logistic growth rate
K = 15000.0 # carrying capacity of stadium
Dt = 3.0

resList = ['w', 'w', 'w', 'w', 'w', 'w', 'l', 'w', 't', 't', 'w', 'l', 'l', 'w', 'w', 'l', 'w', 'w']
counterList = [0] * len(resList)
def initialize():
    global x, xresult, y, yresult, t, timesteps

    x = 8000.0 # initial fan population at first game
    #x = x0
    xresult = [x]

    y = 1.0
    #y = y0
    yresult = [y]

    t = 0.00
    timesteps = [t]

def observe():
    global x, xresult, y, yresult, t, timesteps
    xresult.append(x)
    yresult.append(y)
    timesteps.append(t)

def update():
    global x, xresult, y, yresult, t, timesteps,  games

    #for i, res in enumerate(resList, start=1):
    for i in range(len(resList)):
        t = t + Dt
        if i < 1:
            res1 = 'w'
            res2 = 'w'
        elif i < 2:
            res1 = resList[i - 1]
            res2 = 'w'
        else:
            res1 = resList[i - 1]
            res2 = resList[i - 2]
            
        if (counterList[i] < 1):
            print("Result {}:\t{}".format(i + 1, resList[i]), "\t One game ago:", res1, "\t Two games ago:", res2, "\t Game #", (i+1))
            print (x)
            counterList[i] = counterList[i]+1
            
        if x <= K:
            if (res1 == 'w' and res2 == 't') or (res1 == 't' and res2 == 'w'):
                x = x + x * linGR
            elif (res1 == 'w' and res2 == 'w'):
                x = x + r * x * (1 - x / K) * Dt
                
            elif (res1 == 'l' and res2 == 'l'):
                x = x * geoDR
            else:
                x = x - x * linDR
        else:
            x = 15000.0
        
        #y = y + r * (y - x * y)   
        #for x0 in arange(0, 2, .1):
        #for y0 in arange(0, 2, .1):
# initialize(x0, y0)
initialize()
while t < 100.:
    update()
    observe()
#plot(yresult, xresult, 'b')
#show()

plot(timesteps, xresult, 'r')
show()