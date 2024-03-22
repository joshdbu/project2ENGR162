import math as m
import random
from numpy import sign

g = 9.81
timeStep = 0.001 #input("Enter desired timestep in seconds: ")

class AirParticles:
    
    def __init__(self, intX, intY, intXVel, intYVel, windVel):
        self.ppart = 1.229
        self.dpart = 3 * 10 ** (-10)
        self.pfluid = 1.229
        self.mewFluid = 18.18 * 10 ** (-6)
        self.Cd = 0.47
        self.windVel = windVel
        self.pMass = (4/3) * m.pi * ((self.dpart / 2) ** 2) * self.ppart
        self.xPos, self.yPos = intX, intY
        self.xVel, self.yVel = intXVel, intYVel
        self.xVapt = self.xVel - self.windVel
        self.vapt = m.sqrt(self.xVapt ** 2 + self.yVel ** 2)
        
    def euler(self):
        time = 0
        timeList = [0]
        xList = [self.xPos]
        yList = [self.yPos]
        vxList = [self.xVapt]
        vyList = [self.yVel]
        
        randy = random.uniform(0.95, 1.05)
        n = 0
        while time < 15:
            angle = m.atan(abs(self.yVel / self.xVapt))
            fdmag = self.dragF(self.vapt)
            fdx = -1 * sign(self.xVapt) * fdmag * m.cos(angle) 
            fdy = -1 * sign(self.yVel) * fdmag * m.sin(angle) * randy
            self.updatePos(fdx, fdy)
            time = time + timeStep
            timeList.append(time)
            xList.append(self.xPos)
            yList.append(self.yPos)
            vxList.append(self.xVapt)
            vyList.append(self.yVel)
            #print(f"x: {self.xVapt}   y: {self.yVel}")
            #print(f"fx: {fdx}  fy: {fdy}")
            #print(self.vapt)
            n += 1
        #print(n)
        #print(angle)
        #print(fdy)
        
        return(timeList, xList, yList, vxList, vyList)
            
    def updatePos(self, fi, fk):
        oldXVapt, oldYVel = self.xVapt, self.yVel

        self.xVapt = ((fi * timeStep) / self.pMass) + oldXVapt
        self.yVel = ((fk * timeStep) / self.pMass) + oldYVel
        #print(f"x: {self.xVel}   y: {self.yVel}")
        self.vapt = m.sqrt(self.xVapt ** 2 + self.yVel ** 2)

        avgXVapt = (oldXVapt + self.xVapt) / 2
        self.xVel = avgXVapt + self.windVel
        avgYVel = (oldYVel + self.yVel) / 2
        
        deltaXPos = self.xVel * timeStep + 0.5 * (fi / self.pMass) * timeStep ** 2
        deltaYPos = avgYVel * timeStep + 0.5 * (fk / self.pMass) * timeStep ** 2

        self.xPos += deltaXPos
        self.yPos += deltaYPos

    def dragF(self, velo):
        df = (1/2) * self.pfluid * self.Cd * (m.pi / 4) * self.dpart ** 2 * velo ** 2
        return df
