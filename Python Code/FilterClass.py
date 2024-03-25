class horizontalFilter:
    def __init__(self, length, height, width):
        self.len = length # horizontal length
        self.height = height # vertical hight of filter
        self.width = width # depth/width of filter
        # note: all dimensions are inner dimensions

        self.volume = self.len * self.height * self.width

        self.numCharges = 0
        self.numChargesEscape = 0
        self.totalCharge = 0
        self.volChargeDen = 0
        self.num10Part = 0
        self.num2dot5Part = 0
        self.num10PartOut = 0
        self.num2dot5PartOut = 0
        self.totalMass = 0
        

    def partIn(self, charge, diam, mass):
        self.totalCharge += charge
        if diam > 2.5 * 10 ** (-6):
            self.num10Part += 1
        else:
            self.num2dot5Part += 1
        self.numCharges += 1
        self.totalMass += mass

    def partOut(self, charge, diam):
        self.totalCharge -= charge
        if diam > 2.5 * 10 ** (-6):
            self.num10PartOut += 1
        else:
            self.num2dot5PartOut += 1
        self.numChargesEscape += 1

    def updateChargeDen(self):        
        self.volChargeDen = self.totalCharge / self.volume

    def getTotalMass(self):
        return self.totalMass

    def getTotalOut(self):
        return self.num10PartOut + self.num2dot5PartOut

    def getVCD(self):
        
        return self.volChargeDen

    def calcHowGood(self):
        out2dot5 = 100 * (1 - self.num2dot5PartOut / self.num2dot5Part)
        out10 = 100 * (1 - self.num10PartOut / self.num10Part)

        out2dot5 = round(out2dot5, 2)
        out10 = round(out10, 2)

        return out2dot5, out10

    def getHeight(self):
        # obselete function?
        return self.height
    
    def getDimensions(self):
        # access len w/ 0, height w/ 1, width w/ 2
        return [self.len, self.height, self.width]
        
        # if dim == 0:
        #     return self.len
        # elif dim == 1:
        #     return self.height
        # elif dim == 2:
        #     return self.width
        # else:
        #     return 0
