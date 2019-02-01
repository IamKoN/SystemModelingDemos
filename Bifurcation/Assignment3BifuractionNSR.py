import pylab as PL

x0 = 0.1
samplingStartTime = 1000
sampleNumber = 100

resultA = []
resultX = []

r = 0
da = 0.005

def f(x):
    return r * x * (1 - x)

while r <= 4.0:
    x = x0
    for t in range(samplingStartTime):
        x = f(x)
    for t in range(sampleNumber):
        x = f(x)
        resultA.append(r)
        resultX.append(x)
    r += da

PL.plot(resultA, resultX, 'bo')
PL.show()
