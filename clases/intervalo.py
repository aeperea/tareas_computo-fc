class Intervalo(object):
    def __init__(self, min, max=None): 
        
        if max is None:
            max = min
        if min > max:
            dummy = min
            min = max
            max = dummy
        
        self.min = min
        self.max = max
    
    def __repr__(self):
        return "Intervalo({},{})".format(self.min,self.max) #otra manera de hacerlo
        
    def __str__(self):
        return "[{},{}]".format(self.min, self.max)
    
    def _repr_html_(self):
        return "[{},{}]".format(self.min, self.max)
    
    def __add__(self, otro):
        return Intervalo(self.min + otro.min, self.max + otro.max)
    
    def __sub__(self, otro):
        return Intervalo(self.min - otro.max, self.max - otro.min)