import matplotlib.pyplot as plt
from ParticleClass import SmogParticles
from FilterClass import horizontalFilter
import random
import numpy as np

# note: to make particle (filterDim, intX, intY, intXVel, intYVel)

bigFilter = horizontalFilter(3.5, 1.5, 1)
cornersX = [0, 0, 3.5, 3.5, 0]
cornersY = [0, 1.5, 1.5, 0, 0]
darkCornersX = [0, 3.5]
darkCornersY1 = [1.5, 1.5]
darkCornersY2 = [0, 0]
fanPerMin = 0.000006 # kg per minute
minutes = float(input("Enter desired simulation time in \u00B5 minutes: "))
minutes *= 10 ** (-6)
totalMassIn = minutes * fanPerMin
print(totalMassIn / (1*10**(-14)))
#2500 micrograms of PM10 per min
#1000 micrograms of PM2.5 per min # dont need this i think

#41.6667 micrograms per second
# 4.1667 * 10 ** (-8)



numParticles = 0

superXList = []
superYList = []
superTimeList = []
vcdList = []
countPart = []
mass = 0
while mass < totalMassIn:
# for i in range(0, numParticles):
    particle = SmogParticles(bigFilter.getDimensions(), -0.5, random.uniform(0, 1.5), 12, 0)
    # particle = SmogParticles(bigFilter.getDimensions(), -0.5, 1.25, 10, 0)
    xList, yList, timeList = particle.euler(bigFilter)
    superXList.append(xList)
    superYList.append(yList)
    vcdList.append(bigFilter.getVCD())
    # countPart.append(i)
    numParticles += 1
    mass = bigFilter.getTotalMass()
    # print(mass / totalMassIn)



plt.figure(1, dpi = 250, facecolor='#F3F3F3')
ax = plt.axes()
ax.set_facecolor("#F3F3F3")
bx = plt.gca()

bx.set_xticks(np.arange(0, 4, 0.5))
bx.set_yticks(np.arange(0, 2, 0.5))

for i in range(0, len(superXList)):
    plt.plot(superXList[i], superYList[i])
    # plt.text(superXList[i][-1], superYList[i][-1], i, fontsize=6)
    # if i % 100 == 0:
    #     print("on iteration number", i)

plt.plot(cornersX, cornersY, '--', color='black', linewidth=2.5,)
plt.plot(darkCornersX, darkCornersY1, '-', color='black', linewidth=2.5,)
plt.plot(darkCornersX, darkCornersY2, '-', color='black', linewidth=2.5,)
plt.ylim((-0.3,1.8))
plt.xlim((-0.5, 4))
plt.title('Results: Smog Particle Y-position vs. X-position', fontsize=24)
plt.xlabel('Particle X-position (m)')
plt.ylabel('Particle Y-position (m)')



# plt.figure(2, dpi = 250)
# plt.plot(countPart, vcdList)
# plt.title('Particle count vs VCD')
# plt.xlabel('Particle count')
# plt.ylabel('Volumetric charge distribution')

# print(len(vcdList))
# print(len(countPart))
# print(vcdList)

two, ten = bigFilter.calcHowGood()

tempText = "{}% of PM2.5 and ".format(two)
tempText += str(ten)
howGoodText = "Filter removed {}% of\nPM10 particulate\n".format(tempText)
noteText = "Note: Particle Flow is L to R\n{} particles entered filter".format(numParticles)
plt.text(-0.25, 1.5, howGoodText, fontsize=12)
plt.text(-0.25, -0.25, noteText, fontsize=12)
plt.show()


