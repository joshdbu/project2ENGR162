clc
clear

timeStep = 0.001;
timeInit = 0;
xInit = 50;
yInit = 280;
velocity = -20;
wallX = 0;

time = timeInit;
x = xInit;
y = yInit;

timeList = zeros(1, (yInit / abs(velocity)) / timeStep + 1);
xList = zeros(1, (yInit / abs(velocity)) / timeStep + 1);
yList = zeros(1, (yInit / abs(velocity)) / timeStep + 1);
timeList(1) = timeInit;
xList(1) = xInit;
yList(1) = yInit;

n = 2;
while x > wallX && y > 0
    slope = -1 * time; % equation here
    x = x + slope * timeStep;
    y = velocity * time;
    time = time + timeStep;
    timeList(n) = time;
    xList(n) = x;
    yList(n) = y;
    n = n + 1;
end

timeList(n:end) = [];
xList(n:end) = [];
yList(n:end) = [];

plot(timeList, xList);
title('X-position vs. Time');
xlabel('Time (s)');
ylabel('X-position (cm)');

figure
plot(xList, yList);
title('Y-position vs. X-position');
xlabel('X-position (cm)');
ylabel('Y-position (cm)');
ylim([0, yInit]);
