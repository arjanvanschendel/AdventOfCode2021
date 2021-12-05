class BinaryCounter:
    zerocount:int
    onecount:int

    def __init__(self):
        self.zerocount = 0
        self.onecount = 0
    
    def most(self):
        if(self.zerocount > self.onecount):
            return 0
        return 1

    def least(self):
        if(self.zerocount > self.onecount):
            return 1
        return 0