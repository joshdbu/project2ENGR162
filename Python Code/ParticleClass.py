from math import pi, atan, sqrt, cos, sin
from random import choice, uniform
from FilterClass import horizontalFilter

# timeStep = float(input("Enter desired timestep in seconds: "))
timeStep = 0.0001
g = 9.81 # gravity
E0 = 8.85418 * 10 ** (-12) # epsilon naught
eV = 1.6021766 * 10 ** (-19) # electron volt- in columbs
pfluid = 1.293 # density fluid (air) in kg per meter^3
# mewFluid = 1.849 * 10 ** (-5)
mewFluid = 15 * 10 ** (-6) # kinematic viscosity

class SmogParticles:
    def __init__(self, filterDim, intX, intY, intXVel, intYVel):
        # constants are 1 and things that need calculated are 0
        self.ppart = 1600 # density in units of kg / m^3
        self.partCharge = choice([-1, 1])* eV # charge in factor of 1 electron volt
        
        self.dpart = uniform(0.5 * 10 ** (-6), 10 * 10 ** (-6))
        # print("diam part is:", self.dpart)
        if self.dpart <= 0.5 * 10 ** (-6):
            self.partCharge *= 41
        elif self.dpart >= 10 * 10 ** (-6):
            self.partCharge *= 407
        else:
            self.partCharge *= (self.dpart - 0.5 * 10 ** (-6)) / (10 * 10 ** (-6) - 0.5 * 10 ** (-6)) * (407 - 41) + 41

        # print(self.partCharge)
        # self.dpart = 2.5 * 10 ** (-6) # could add some random noise of +- 5% to this
        
        self.filterDim = filterDim
        
        self.Dvert = filterDim[1] / 2 # distance above center of charges
        
        self.yCd = 0

        self.pMass = (4/3) * pi * (self.dpart / 2)**3 * self.ppart
        # print(self.pMass)
        # print(self.pMass)
        self.xPos, self.yPos = intX, intY
        self.xVel, self.yVel = intXVel, intYVel
        # self.plateCharge = 1 # charge of bottom pl
        # self.plateChargeDen = 0.005 # charge of bottom pl in columbs per m^2
        self.plateChargeDen = 10 * 10 ** (-7) # charge of bottom pl

        self.fg = self.gravF()
        # print("grav is:", self.fg)
        self.fb = self.bouyF()
        # print("bouy is:", self.fb)
        self.fp = self.plateF()


    def euler(self, filter):
        time = 0
        timeList = [0]
        xList = [self.xPos]
        yList = [self.yPos]
        horizontalFilter.updateChargeDen(filter)

        horizontalFilter.partIn(filter, self.partCharge, self.dpart, self.pMass)

        while self.xPos < 0:
            
            self.updatePos(0, self.fb -self.fg)
            time += timeStep
            timeList.append(time)
            xList.append(self.xPos)
            yList.append(self.yPos)

        while self.yPos > 0 and self.yPos < self.filterDim[1] and self.xPos < self.filterDim[0] and self.xPos > -10:
            # print("time at start of loop was", time)
            # print("y pos is", self.yPos, "x pos is", self.xPos)
            fdy = self.dragF(self.yVel)
            
            fey = self.otherChargeF(horizontalFilter.getVCD(filter)) # note this is other field
            # print("xvel", self.xVel, "yvel", self.yVel)
            # print("xpos", self.xPos, "ypos", self.yPos)
            # self.updatePos(0, fdy + fey + self.fg - self.fb + self.fp)
            # self.updatePos(fdx, 0)
            self.updatePos(0, self.fb - self.fg + self.fp + fdy + fey)
            time = time + timeStep
            timeList.append(time)
            xList.append(self.xPos)
            yList.append(self.yPos)


        if self.xPos > self.filterDim[0]:
            while self.xPos < self.filterDim[0] + 0.5:

                self.updatePos(0, self.fb - self.fg)
                time = time + timeStep
                timeList.append(time)
                xList.append(self.xPos)
                yList.append(self.yPos)

            horizontalFilter.partOut(filter, self.partCharge, self.dpart)

        
        # print("broke out of loop! y pos is", self.yPos, "x pos is", self.xPos)

        return xList, yList, timeList

    def updatePos(self, fi, fk):
        oldXVel, oldYVel = self.xVel, self.yVel

        self.xVel = oldXVel + (fi * timeStep) / self.pMass 
        self.yVel = oldYVel + (fk * timeStep) / self.pMass

        self.yCd = self.calcCd(self.yVel) # note: xCd irrelevent as x vel is same as surrounding air

        avgXVel = (oldXVel + self.xVel) / 2
        avgYVel = (oldYVel + self.yVel) / 2
        
        xAcel = (self.xVel - oldXVel) / timeStep
        # print("xAccel is", xAcel)
        # print(avgXVel)
        # print(avgYVel)

        deltaXPos = avgXVel * timeStep + 0.5 * (fi / self.pMass) * timeStep ** 2
        deltaYPos = avgYVel * timeStep + 0.5 * (fk / self.pMass) * timeStep ** 2

        self.xPos += deltaXPos
        self.yPos += deltaYPos

        self.updateDvert()


    def updateDvert(self):
        self.Dvert = self.yPos - self.filterDim[1] / 2
    
    def calcCd(self, velApt):
        Re = (self.dpart * abs(velApt))/ mewFluid
        
        if Re != 0:
            Cd = 24 / Re
        else:
            Cd = 0
        # print("Cd is", Cd)
        return Cd
    
    def gravF(self):
        fg = (pi / 6) * self.ppart * g * (self.dpart ** 3)
        return fg

    def bouyF(self):
        bf = (pi / 6) * pfluid * g * (self.dpart ** 3)
        return bf

    # def dragF(self, xVelApt, yVelApt):
    #     mag = sqrt(xVelApt ** 2 + yVelApt ** 2)
    #     theta = atan(yVelApt / xVelApt)

    #     df = (1/2) * pfluid * self.yCd * (pi / 4) * self.dpart ** 2 * mag ** 2
    #     dragX = df * cos(theta)
    #     dragY = df * sin(theta)
        
    #     return dragX, dragY
    
    def dragF(self, velApt):
        df = -1 * (1/2) * pfluid * self.yCd * (pi / 4) * self.dpart ** 3 * velApt ** 2
        # print("drag force =", df)
        return df
    
    def plateF(self):
        pf = (self.partCharge * self.plateChargeDen) / (2 * pi * E0)
        return pf

    def otherChargeF(self, VCD):
        of = ((self.partCharge * VCD) / (2 * E0)) * (2 * self.Dvert - self.filterDim[1])
        return of

    def getCharge(self):
        return self.partCharge
