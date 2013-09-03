import numpy as np

class Intervalo(object):
    def __init__(self, min, max=None): 
        
        if max is None:
            max = min
        elif min > max:
            min, max = max, min
        
        self.min = min
        self.max = max
    
    def __repr__(self):
        return "Intervalo({},{})".format(self.min,self.max) #otra manera de hacerlo
        
    def __str__(self):
        return "[{},{}]".format(self.min, self.max)
    
    def _repr_html_(self):
        return "[{},{}]".format(self.min, self.max)
    
    def __add__(self, otro):
        if not isinstance(otro,Intervalo):
            otro = Intervalo(otro)
        return Intervalo(self.min + otro.min, self.max + otro.max)
        
    def __radd__(self, otro):
        return self + otro
    
    def __sub__(self, otro):
        if not isinstance(otro,Intervalo):
            otro = Intervalo(otro)
        return Intervalo(self.min - otro.max, self.max - otro.min)
    
    def __rsub__(self, otro):
        return self - otro
    
    def __mul__(self, otro):
        if not isinstance(otro,Intervalo):
            otro = Intervalo(otro)
        a = np.min([self.min*otro.min, self.min*otro.max, self.max*otro.min, self.max*otro.max])
        b = np.max([self.min*otro.min, self.min*otro.max, self.max*otro.min, self.max*otro.max])
        return Intervalo(a,b)
    
    def __rmul__(self, otro):
        return self * otro
    
    #Funcion inversa para calcular mas facil la division    
    def inverse(self):
        if self.min <= 0 <= self.max:
            return "Error, el intervalo del denominador contiene el cero"
        else:
            return Intervalo(1./self.max,1./self.min)
    
    def __div__(self, otro):
        if not isinstance(otro,Intervalo):
            otro = Intervalo(otro)
        if otro.min <= 0 & otro.max >= 0:
            return "Error, el intervalo del denominador contiene el cero"
        else:
            return self * otro.inverse()
    
    __truediv__ = __div__
    
    def __rdiv__(self, otro):
        return self.inverse() * otro
        
    __rtruediv__ = __rdiv__
    
    def __neg__(self):
        return Intervalo(-self.max, -self.min)
    
    # Intersection
    def __and__(self, otro):
        if not isinstance(otro,Intervalo):
            otro = Intervalo(otro)
        if (self.min > otro.max) | (self.max < otro.min):
            return None
        else:
            a = np.max([self.min, otro.min])
            b = np.min([self.max, otro.max])
            return Intervalo(a,b)
    
    def __rand__(self, otro):
        return self & otro
    
    def __or__(self, otro):
        if not isinstance(otro,Intervalo):
            otro = Intervalo(otro)
        if (self.min > otro.max) | (self.max < otro.min):
            return [self, otro]
        else:
            a = np.min([self.min, otro.min]) 
            b = np.max([self.max, otro.max])
            return Intervalo(a,b)
    
    def __ror__(self, otro):
        return self | otro
    
    def hull(self, otro):
        if not isinstance(otro,Intervalo):
            otro = Intervalo(otro)
        a = np.min([self.min,otro.min])
        b = np.max([self.max,otro.max])
        return Intervalo(a,b)
    
    def width(self):
        return self.max - self.min
    
    def mean(self):
        return 1./2.*(self.min + self.max)
    
    def radius(self):
        return 1./2.*self.width()
    