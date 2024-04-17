import matplotlib.pyplot as plt
from ParticleClass import SmogParticles
from FilterClass import horizontalFilter
import random
import numpy as np

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

numParticles = 0

superXList = []
superYList = []
superTimeList = []
vcdList = []
countPart = []
mass = 0
while mass < totalMassIn:
    particle = SmogParticles(bigFilter.getDimensions(), -0.5, random.uniform(0, 1.5), 12, 0)
    xList, yList = particle.euler(bigFilter)
    superXList.append(xList)
    superYList.append(yList)
    vcdList.append(bigFilter.getVCD())
    numParticles += 1
    mass = bigFilter.getTotalMass()
    
# , facecolor='#F3F3F3'

plt.figure(1, dpi = 250)
ax = plt.axes()
ax.set_facecolor("#F3F3F3")
bx = plt.gca()

bx.set_xticks(np.arange(0, 4, 0.5))
bx.set_yticks(np.arange(0, 2, 0.5))

for i in range(0, len(superXList)):
    plt.plot(superXList[i], superYList[i])
    
plt.plot(cornersX, cornersY, '--', color='black', linewidth=2.5,)
plt.plot(darkCornersX, darkCornersY1, '-', color='black', linewidth=2.5,)
plt.plot(darkCornersX, darkCornersY2, '-', color='black', linewidth=2.5,)
plt.ylim((-0.3,1.8))
plt.xlim((-0.5, 4))
plt.title('Results: Smog Particle Y-position vs. X-position', fontsize=12)
plt.xlabel('Particle X-position (m)')
plt.ylabel('Particle Y-position (m)')

two, ten = bigFilter.calcHowGood()

tempText = "{}% of PM2.5 and ".format(two)
tempText += str(ten)
howGoodText = "Filter removed {}% of PM10 particulate\n".format(tempText)
noteText = "Note: Particle Flow is L to R\n{} particles entered filter".format(numParticles)
plt.text(-0.25, 1.5, howGoodText, fontsize=12)
plt.text(-0.25, -0.25, noteText, fontsize=12)
plt.show()