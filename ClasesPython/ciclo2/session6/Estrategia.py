from abc import ABC, abstractmethod

class EstrategiaDescuentos(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def calcular(self, monto):
        pass
    
class SinDescuento(EstrategiaDescuentos):
    
    def calcular (self, monto):
        return monto
    
class DescuentoPorcentaje(EstrategiaDescuentos):
    
    def __init__(self, porcentaje):
        self.porcentaje = porcentaje
        
    def calcular(self, monto):
        return  monto - (monto * self.porcentaje / 100)
    
class DescuentoFijo(EstrategiaDescuentos):
    
    def __init__(self, montoDescuento):
        self.montoDescuento = montoDescuento
        
    def calcular (self, monto):
        return monto - self.montoDescuento
    
class Pedido:
    
    def