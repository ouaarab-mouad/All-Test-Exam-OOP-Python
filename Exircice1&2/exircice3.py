class circle :
    def __init__(self , R=0):
        self .R=R
    def getArea(self):
        return pi*self.R**2
    def getPrimeter(self):
        return 2*pi*self.R
    
C1=circle(5)
print(C1.getArea())
print(C1.getPrimeter())