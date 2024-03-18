from math import pi
g = 9.81


class Particles:
    def __init__(self, a, v):
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
        self.Dvert = 0 #distance above center of charges
        self.H = 0
        
    def calcCd(self):
        Re = (self.pfluid * self.dpart * abs(self.vapt))/ self.mewFluid
        Cd = 24 / Re
        return Cd
    
    def gravF(self):
        (pi / 6) * self.ppart * g * (self.dpart ^ 3)
    
    def bouyF(self):
        (pi / 6) * self.pfluid * g * (self.dpart ^ 3)

    def dragF(self):
        (1/2) * self.pfluid * self.calcCd() * (pi / 4) * self.dpart ^ 2 * self.vapt ^ 2
    

    
