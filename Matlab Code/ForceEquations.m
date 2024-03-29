% Force equations
partDensity = 1;
diameter = 1;
fluidDensity = 1;
viscosity = 1;
plateCharge = 1;
partCharge = 1;
veloInit = 0;
G = 9.81;
EPSILON = 8.85418 * (10 ^ -12) 
MAX_HEIGHT = 2

% Constant
gravity = (pi / 6.0) * partDensity * G * (diameter ^ 3);
buoyant = (pi / 6.0) * fluidDensity * G * (diameter ^ 3);
plateField = (plateCharge * partCharge) / (2 * pi * EPSILON)

% Time dependent
veloApp = 1;
reynoldsNum = (fluidDensity * abs(veloApp)) / viscosity;
dragCoeff = 24.0 / reynoldsNum;
drag = 0.5 * fluidDensity * dragCoeff * (pi / 4.0) * (diameter ^ 2) * (veloApp ^2);
height = 1;
otherField = (((partCharge ^ 2) * concentration) / 2 * EPSILON) * ((2 * height) - MAX_HEIGHT); 
