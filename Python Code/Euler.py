import matplotlib.pyplot as plt

timeStep = 0.001
timeInit = 0
xInit = 0
yInit = 30
velocity = 20
length = 280

time = timeInit
x = xInit
y = yInit
timeList = []
xList = []
yList = []
timeList.append(timeInit)
xList.append(xInit)
yList.append(yInit)

while y > 0 and x < length:
    slope = -1 * time
    x = velocity * time + xInit
    y = y + slope * timeStep
    time = time + timeStep
    timeList.append(time)
    xList.append(x)
    yList.append(y)

plt.figure(1, dpi = 5000)
plt.plot(timeList, yList)
plt.title('Y-position vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Y-position (cm)')
plt.show()

plt.figure(1, dpi = 5000)
plt.plot(xList, yList)
plt.title('Y-position vs. X-position')
plt.xlabel('X-position (cm)')
plt.ylabel('Y-position (cm)')
plt.ylim([0, yInit])
plt.show()