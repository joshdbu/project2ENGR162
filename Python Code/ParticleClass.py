from math import pi

timeStep = input("Enter desired timestep in seconds: ")
g = 9.81 # gravity
E0 = 8.85418 * 10 **(-12) # epsilon naught
pfluid = 1 # density fluid
filterLength = 0 # filter length
mewFluid = 1


class Particles:
    def __init__(self, intX, intY, intXVel, intYVel):
        # constants are 1 and things that need calculated are 0
        self.ppart = 1620 # in units of kg / cm^3
        self.partCharge = 1
        self.dpart = 2.5 * 10 ** (-6) # could add some random noise of +- 5% to this
        
        self.Cd = 0
        self.vapt = 0 # velocity apperant
        
        self.q = 0
        self.chgDen = 0
        self.Dvert = 0 # distance above center of charges
        
        self.pMass = (4/3) * pi * (self.dpart / 2)**2 * self.ppart
        self.xPos, self.yPos = intX, intY
        self.xVel, self.yVel = intXVel, intYVel
        self.plateCharge = 1
        self.fg = self.gravF()
        self.fb = self.bouyF()


    def euler(self):
        time = 0
        timeList = [0]
        xList = [self.xPos]
        yList = [self.yPos]
        
        while self.yPos > 0 and self.xPos < filterLength:
            fd = self.dragF()
            fe = self.field() # note this is other field
            
            self.xPos, self.yPos = self.updatePos(fd, fe)
            time = time + timeStep
            timeList.append(time)
            xList.append(self.xPos)
            yList.append(self.yPos)

    def updatePos(self, fi, fk):
        oldXVel, oldYVel = self.xVel, self.yVel

        self.xVel = (fi * timeStep) / self.pMass 
        self.yVel = (fk * timeStep) / self.pMass

        avgXVel = (oldXVel + self.xVel) / 2
        avgYVel = (oldYVel + self.yVel) / 2
        
        deltaXPos = avgXVel * timeStep + 0.5 * (fi / self.pMass) * timeStep ** 2
        deltaYPos = avgYVel * timeStep + 0.5 * (fi / self.pMass) * timeStep ** 2

        self.xPos += deltaXPos
        self.yPos += deltaYPos

    # def updateDvert
    
    def calcCd(self):
        Re = (pfluid * self.dpart * abs(self.vapt))/ mewFluid
        Cd = 24 / Re
        return Cd
    
    def gravF(self):
        fg = (pi / 6) * self.ppart * g * (self.dpart ** 3)
        return fg

    def bouyF(self):
        bf = (pi / 6) * pfluid * g * (self.dpart ** 3)
        return bf

    def dragF(self):
        df = (1/2) * pfluid * self.calcCd() * (pi / 4) * self.dpart ** 2 * self.vapt ** 2
        return df
    
    def plateF(self):
        pf = (self.plateCharge * self.partCharge) / (2 * pi * self.E0)

    
