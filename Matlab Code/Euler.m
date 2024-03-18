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

while x > wallX && y > 0
    slope = 1; % equation here
    x = x + slope * timeStep;
    y = velocity * time;
    time = time + timeStep;
end