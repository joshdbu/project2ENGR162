import matplotlib.pyplot as plt
from AirParticleClass import AirParticles
import math as m
import random

allTimes = []
allX = []
allY = []

magVel = 3
windVel = -2
filterHeight = 150
filterSize = 100

for height in range(filterHeight, filterHeight + filterSize + 1, 100):            
    rand = random.randint(-5, 5)
    angle = - 10 + (round(height / 100.0, 1) - filterHeight / 100.0) * 20 + rand
    rad = (angle / 180) * m.pi
    xVel = magVel * m.cos(rad)
    yVel = magVel * m.sin(rad)
    part = AirParticles(0, height / 100.0, xVel, yVel, windVel)
    t, x, y = part.euler()
    allTimes.append(t)
    allX.append(x)
    allY.append(y)
    
for i in range(len(allTimes)):
    """
    deltaT = 15
    colors = []
    numTimes = len(allTimes[i])
    b = 0
    for j in range(numTimes):
        if j < numTimes / 2:
            r = round((j / (numTimes / 2)), 2)
            g = 1
        else:
            r = 1
            g = round(1 - ((j - (numTimes / 2)) / (numTimes / 2)), 2)
        colors.append([r, g, b])
    """
    plt.figure(1, dpi = 500)
    plt.scatter(allX[i], allY[i], c = 'r')

plt.title('Y-position vs. X-position')
plt.xlabel('X-position (cm)')
plt.ylabel('Y-position (cm)')
plt.show()
"""
part = AirParticles(0, 0, 2.6, -1.5)
t, x, y = part.euler()

plt.figure(1, dpi = 500)
plt.plot(t, x)
plt.title('X-position vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('X-position (cm)')
plt.show()

plt.figure(2, dpi = 500)
plt.plot(t, y)
plt.title('Y-position vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Y-position (cm)')
plt.show()


plt.figure(3, dpi = 500)
plt.plot(x, y)
plt.title('Y-position vs. X-position')
plt.xlabel('X-position (cm)')
plt.ylabel('Y-position (cm)')
plt.show()
"""
