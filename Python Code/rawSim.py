from ParticleClass import SmogParticles
from FilterClass import horizontalFilter
import random

# note: to make particle (filterDim, intX, intY, intXVel, intYVel)

bigFilter = horizontalFilter(3.5, 1.5, 1)
cornersX = [0, 0, 3.5, 3.5, 0]
cornersY = [0, 1.5, 1.5, 0, 0]
darkCornersX = [0, 3.5]
darkCornersY1 = [1.5, 1.5]
darkCornersY2 = [0, 0]
fanPerMin = 0.000006 # kg per minute
minutes = float(input("Enter desired simulation time in minutes: "))
totalMassIn = minutes * fanPerMin

iterationsForDay = 1440 / minutes

# print(totalMassIn / (1*10**(-14)))
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
    # xList, yList, timeList = particle.euler(bigFilter)
    particle.euler(bigFilter)
    # superXList.append(xList)
    # superYList.append(yList)
    # vcdList.append(bigFilter.getVCD())
    # countPart.append(i)
    numParticles += 1
    mass = bigFilter.getTotalMass()
    # print("program completion:", 100 * mass / totalMassIn, "percent")



two, ten = bigFilter.calcHowGood()

tempText = "{}% of PM2.5 and ".format(two)
tempText += str(ten)
howGoodText = "\nFilter removed {}% of PM10 particulate".format(tempText)
noteText = "{} particles entered filter".format(numParticles)
moreText = "{} particles were captured by filter\n".format(numParticles - bigFilter.getTotalOut())

morenoteText = "Over 1 Day, {} particles would enter the filter".format(round(iterationsForDay * numParticles))
moremoremoreText = "{} particles would be captured by the filter\n\n\n".format(round(iterationsForDay * bigFilter.getTotalOut()))

print(howGoodText)
print(noteText)
print(moreText)
print(morenoteText)
print(moremoremoreText)
