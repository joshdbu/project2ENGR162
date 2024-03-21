from math import pi
from FilterClass import horizontalFilter

# timeStep = float(input("Enter desired timestep in seconds: "))
timeStep = 0.01
g = 9.81 # gravity
E0 = 8.85418 * 10 ** (-12) # epsilon naught
eV = 1.6021766 * 10 ** (-19) # electron volt- in columbs
pfluid = 1.293 # density fluid (air) in kg per meter^3
mewFluid = 1.849 * 10 ** (-5)

class SmogParticles:
    def __init__(self, filterDim, intX, intY, intXVel, intYVel):
        # constants are 1 and things that need calculated are 0
        self.ppart = 1620 # density in units of kg / cm^3
        self.partCharge = 75 * eV # charge in factor of 1 electron volt
        self.dpart = 2.5 * 10 ** (-6) # could add some random noise of +- 5% to this
        
        self.filterDim = filterDim
        
        self.Dvert = filterDim[1] / 2 # distance above center of charges
        
        self.yCd = 0

        self.pMass = (4/3) * pi * (self.dpart / 2)**2 * self.ppart
        self.xPos, self.yPos = intX, intY
        self.xVel, self.yVel = intXVel, intYVel
        self.plateCharge = 0.01 # charge of bottom pl
        self.fg = self.gravF()
        self.fb = self.bouyF()
        self.fp = self.plateF()


    def euler(self, filter):
        time = 0
        timeList = [0]
        xList = [self.xPos]
        yList = [self.yPos]
        
        while self.yPos > 0 and self.yPos < self.filterDim[1] and self.xPos < self.filterDim[0]:
            # print("time at start of loop was", time)
            # print("y pos is", self.yPos, "x pos is", self.xPos)
            fdy = -self.dragF(self.yVel)
            fey = self.otherChargeF(horizontalFilter.getVCD(filter)) # note this is other field
            
            self.updatePos(0, fdy + fey + self.fg - self.fb + self.fp)
            time = time + timeStep
            timeList.append(time)
            xList.append(self.xPos)
            yList.append(self.yPos)
        
        print("broke out of loop! y pos is", self.yPos, "x pos is", self.xPos)

        return xList, yList, timeList

    def updatePos(self, fi, fk):
        oldXVel, oldYVel = self.xVel, self.yVel

        self.xVel = oldXVel + (fi * timeStep) / self.pMass 
        self.yVel = oldYVel + (fk * timeStep) / self.pMass

        self.yCd = self.calcCd(self.yVel) # note: xCd irrelevent as x vel is same as surrounding air

        avgXVel = (oldXVel + self.xVel) / 2
        avgYVel = (oldYVel + self.yVel) / 2
        
        deltaXPos = avgXVel * timeStep + 0.5 * (fi / self.pMass) * timeStep ** 2
        deltaYPos = avgYVel * timeStep + 0.5 * (fi / self.pMass) * timeStep ** 2

        self.xPos += deltaXPos
        self.yPos += deltaYPos

        self.updateDvert()


    def updateDvert(self):
        self.Dvert = self.yPos - self.filterDim[1] / 2
    
    def calcCd(self, velApt):
        Re = (pfluid * self.dpart * abs(velApt))/ mewFluid
        Cd = 24 / Re
        return Cd
    
    def gravF(self):
        fg = (pi / 6) * self.ppart * g * (self.dpart ** 3)
        return fg

    def bouyF(self):
        bf = (pi / 6) * pfluid * g * (self.dpart ** 3)
        return bf

    def dragF(self, velApt):
        df = (1/2) * pfluid * self.yCd * (pi / 4) * self.dpart ** 2 * velApt ** 2
        return df
    
    def plateF(self):
        pf = (self.plateCharge * self.partCharge) / (2 * pi * E0)
        return pf

    def otherChargeF(self, VCD):
        of = ((self.partCharge * VCD) / (2 * E0)) * (2 * self.Dvert - self.filterDim[1])
        return of

    def getCharge(self):
        return self.partCharge
