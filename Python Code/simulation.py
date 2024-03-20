from ParticleClass import SmogParticles
from FilterClass import horizontalFilter

bigFilter = horizontalFilter(2.5, 1, 1)

particle = SmogParticles(bigFilter.getDimensions(), 0, 0.5, 1, 0)

particle.euler(bigFilter)