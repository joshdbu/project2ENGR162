from ParticleClass import SmogParticles
from FilterClass import horizontalFilter

# note: to make particle (filterDim, intX, intY, intXVel, intYVel)

bigFilter = horizontalFilter(2.5, 1, 1)

particle = SmogParticles(bigFilter.getDimensions(), 0, 0.5, 1, 0)

xList, yList, timeList = particle.euler(bigFilter)


