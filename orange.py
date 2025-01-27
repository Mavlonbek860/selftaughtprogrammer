class Orange:
    
    def __init__(self, color, weight, mold):
    	self.color = color
    	self.weght = weight
    	self.mold = 0
    
    def rot(self, days, temp):
    	self.mold = days * temp * .1


orange = Orange('orange', 12, 0)



