class horizontalFilter:
    def __init__(self, length, height, width):
        self.len = length # horizontal length
        self.height = height # vertical hight of filter
        self.width = width # depth/width of filter
        # note: all dimensions are inner dimensions

        self.volume = self.len * self.height * self.width

        self.totalCharge = 0
        self.volChargeDen = 0
    def partIn(self, charge):
        self.totalCharge += charge

    def partOut(self, charge):
        self.totalCharge -= charge

    def updateChargeDen(self):
        self.volChargeDen = self.totalCharge / self.volume

    def getVCD(self):
        
        return self.volChargeDen

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
