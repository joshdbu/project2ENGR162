import matplotlib.pyplot as plt
from AirParticleClass import AirParticles
import math as m
import random

allTimes = []
allX = []
allY = []
allVx = []
allVy = []
angles = []

magVel = 2.5
print("Positive velocity for tailwind and negative velocity for headwind.")
windVel = int(input("Enter wind velocity (m/s): "))
string = ''
if windVel < 0:
    string = 'head'
elif windVel > 0:
    string = 'tail'
filterHeight = 150
filterSize = 100

for height in range(filterHeight, filterHeight + filterSize + 1, 10):
    rand = 0 #random.randint(-1, 1)
    #angle = - 10 + (round(height / 100.0, 1) - filterHeight / 100.0) * 20 + rand
    angle = - 10 + round((height - filterHeight) / 100.0, 2) * 20
    print(angle)
    angles.append(angle)
    rad = (angle / 180) * m.pi
    xVel = magVel * m.cos(rad)
    yVel = magVel * m.sin(rad)
    part = AirParticles(0, height / 100.0, xVel, yVel, windVel)
    t, x, y, vx, vy = part.euler()
    allTimes.append(t)
    allX.append(x)
    allY.append(y)
    allVx.append(vx)
    allVy.append(vy)
    
plt.figure(1, dpi = 250, facecolor='#F3F3F3')
ax = plt.axes()
ax.set_facecolor("#F3F3F3")
plt.title(f'Air Particle Y- vs. X-position ({abs(windVel)} m/s {string}wind)')
plt.xlabel('X-position (m)')
plt.ylabel('Y-position (m)')

index = 0
i = 0
while angles[i] < 0:
    i = i + 1
index = i

for i in range(index - 1, -1, -1):
    
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
    #if allY[i][0] > allY[i][-1]:
    allY[i].reverse()
    allX[i].reverse()
    colors.reverse()
    plt.scatter(allX[i], allY[i], c = colors, s = 1)    

for i in range(index, len(allTimes), 1):
    
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
    #if allY[i][0] > allY[i][-1]:
    allY[i].reverse()
    allX[i].reverse()
    colors.reverse()
    plt.scatter(allX[i], allY[i], c = colors, s = 1)
    """
    plt.figure(2, dpi = 500)
    plt.plot(allTimes[i], allX[i])
    
    plt.figure(3, dpi = 500)
    plt.plot(allTimes[i], allY[i])
    
    plt.figure(4, dpi = 500)
    plt.plot(allTimes[i], allVx[i])
    
    plt.figure(5, dpi = 500)
    plt.plot(allTimes[i], allVy[i])
    """
    
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
