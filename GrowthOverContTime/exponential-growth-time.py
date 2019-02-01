from pylab import show, plot

a = 1.1
xresult = []
yresult = []
result = []
timesteps=[]
x=0
y=0
t=0

def initialize():
    global x, y, xresult, yresult, t, timesteps ###
    x = 1.
    y = 1.
    xresult = [x]
    yresult = [y]
    t = 0. ###
    timesteps = [t] ###
    
def observe():
    global x, y, xresult, yresult, t, timesteps ###
    xresult.append(x)
    yresult.append(y)
    timesteps.append(t) ###

def update():
    global x, y, xresult, yresult, t, timesteps ###
    #x = a * x
    nextx = 0.5*x + y
    nexty = -0.5*x + y
    x,y = nextx, nexty
    t = t + 0.1 ###

def updateFib():
    global x, y, result, t, timesteps ###
    #x = a * x

    nexty = x
    x = x + y
    y = nexty
    result.append(y)
    
    
    t = t + 0.1 ###
initialize()
while t < 3.: ###
    updateFib()
    #update()
    observe()

plot(timesteps, xresult, 'g-') ###
plot(timesteps, yresult, 'b--') ###
plot(xresult, yresult) ###
print(result)
show()
