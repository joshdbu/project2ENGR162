import math as m
from numpy import sign
import random

g = 9.81
timeStep = 0.001 #input("Enter desired timestep in seconds: ")

class AirParticles:
    
    def __init__(self, intX, intY, intXVel, intYVel):
        self.ppart = 1.229
        self.dpart = 3 * 10 ** (-10)
        self.pfluid = 1.229
        self.mewFluid = 18.18 * 10 ** (-6)
        self.Cd = 0.47
        self.pMass = (4/3) * m.pi * ((self.dpart / 2) ** 2) * self.ppart
        self.xPos, self.yPos = intX, intY
        self.xVel, self.yVel = intXVel, intYVel
        self.vapt = m.sqrt(self.xVel ** 2 + self.yVel ** 2)
        
    def euler(self):
        time = 0
        timeList = [0]
        xList = [self.xPos]
        yList = [self.yPos]
        
        angle = m.atan(self.yVel / self.xVel)
        # print(angle)
        randy = random.uniform(0.8, 1.2)
        n = 0
        while self.vapt > 0.5:
            fdmag = self.dragF(self.vapt)
            fdx = -1 * fdmag * m.cos(angle) 
            fdy = -1 * fdmag * m.sin(angle) * randy
            self.updatePos(fdx, fdy)
            time = time + timeStep
            timeList.append(time)
            xList.append(self.xPos)
            yList.append(self.yPos)
            #print(f"x: {self.xVel}   y: {self.yVel}   mag: {self.vapt}")
            #print(self.vapt)
            n += 1
        #print(n)
        
        return(timeList, xList, yList)
            
    def updatePos(self, fi, fk):
        oldXVel, oldYVel = self.xVel, self.yVel

        self.xVel = ((fi * timeStep) / self.pMass) + oldXVel
        self.yVel = ((fk * timeStep) / self.pMass) + oldYVel
        #print(f"x: {self.xVel}   y: {self.yVel}")
        self.vapt = m.sqrt(self.xVel ** 2 + self.yVel ** 2)

        avgXVel = (oldXVel + self.xVel) / 2
        avgYVel = (oldYVel + self.yVel) / 2
        
        deltaXPos = avgXVel * timeStep + 0.5 * (fi / self.pMass) * timeStep ** 2
        deltaYPos = avgYVel * timeStep + 0.5 * (fk / self.pMass) * timeStep ** 2

        self.xPos += deltaXPos
        self.yPos += deltaYPos

    def dragF(self, velo):
        df = (1/2) * self.pfluid * self.Cd * (m.pi / 4) * self.dpart ** 2 * velo ** 2
        return df
