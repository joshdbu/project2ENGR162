import matplotlib.pyplot as plt
from ParticleClass import SmogParticles
from FilterClass import horizontalFilter
import random

# note: to make particle (filterDim, intX, intY, intXVel, intYVel)

bigFilter = horizontalFilter(3.5, 1.5, 1)
cornersX = [0, 0, 3.5, 3.5, 0]
cornersY = [0, 1.5, 1.5, 0, 0]

#2500 micrograms of PM10 per min
#1000 micrograms of PM2.5 per min # dont need this i think

#41.6667 micrograms per second
# 4.1667 * 10 ** (-8)



numParticles = 1000

superXList = []
superYList = []
superTimeList = []
vcdList = []
countPart = []

for i in range(0, numParticles):
    particle = SmogParticles(bigFilter.getDimensions(), -0.5, random.uniform(0, 1.5), 1, 0)
    xList, yList, timeList = particle.euler(bigFilter)
    superXList.append(xList)
    superYList.append(yList)
    vcdList.append(bigFilter.getVCD())
    countPart.append(i)



plt.figure(1, dpi = 250)

for i in range(0, len(superXList)):
    plt.plot(superXList[i], superYList[i])
    # plt.text(superXList[i][-1], superYList[i][-1], i, fontsize=6)
    # if i % 100 == 0:
    #     print("on iteration number", i)

plt.plot(cornersX, cornersY, color='black')

plt.ylim((-0.5,2))
plt.xlim((-0.5, 4))
plt.title('Y-position vs. X-position')
plt.xlabel('X-position (m)')
plt.ylabel('Y-position (m)')

plt.figure(2, dpi = 250)
plt.plot(countPart, vcdList)
plt.title('Particle count vs VCD')
plt.xlabel('Particle count')
plt.ylabel('Volumetric charge distribution')

# print(len(vcdList))
# print(len(countPart))
# print(vcdList)


howGoodText = "Filter was able to remove {}% of PM2.5 particulate\nNote: Particle Flow is L to R".format(round(bigFilter.calcHowGood()), 2)
plt.text(-0.25, 1.6, howGoodText, fontsize=12)
plt.show()


