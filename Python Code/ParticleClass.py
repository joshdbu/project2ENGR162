from math import pi
g = 9.81


class Particles:
    def __init__(self, a, v, intX, intY, intXVel, intYVel):
        # constants are 1 and things that need calculated are 0
        self.ppart = 1
        self.dpart = 1
        self.pfluid = 1
        self.avert = a
        self.vvert = v
        self.Cd = 0
        self.vapt = 0
        self.mewFluid = 1
        self.q = 0
        self.chgDen = 0
        self.E0 = 8.85418 * 10^(-12)
        self.Dvert = 0 # distance above center of charges
        self.H = 0
        self.pMass = (4/3) * pi * (self.dpart / 2)^2 * self.ppart
        self.xPos, self.yPos = intX, intY
        self.xVel, self.yVel = intXVel, intYVel

     def euler(self):
        time = 0
        timeList = [0]
        xList = [self.xPos]
        yList = [self.yPos]
        
        while self.yPos > 0 and self.xPos < self.H:
            fd = self.dragF()
            fe = self.field()
            
            self.xPos, self.yPos = self.updatePos(fd, fe)
            time = time + self.timeStep
            timeList.append(time)
            xList.append(self.xPos)
            yList.append(self.yPos)
        
    def updatePos(self, fi, fk):
        oldXVel, oldYVel = self.xVel, self.yVel

        deltaX
        deltaX = 


    
    def calcCd(self):
        Re = (self.pfluid * self.dpart * abs(self.vapt))/ self.mewFluid
        Cd = 24 / Re
        return Cd
    
    def gravF(self):
        fg = (pi / 6) * self.ppart * g * (self.dpart ^ 3)
        return fg

    def bouyF(self):
        bf = (pi / 6) * self.pfluid * g * (self.dpart ^ 3)
        return bf

    def dragF(self):
        df = (1/2) * self.pfluid * self.calcCd() * (pi / 4) * self.dpart ^ 2 * self.vapt ^ 2
        return df

    
