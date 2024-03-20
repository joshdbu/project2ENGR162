import matplotlib.pyplot as plt
from AirParticleClass import AirParticles

part = AirParticles(0, 0, 2, 3)
t, x, y = part.euler()

plt.figure(1, dpi = 500)
plt.plot(t, y)
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
