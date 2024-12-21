class Banco:
    
    TASA_INTERES = 0.05
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    @classmethod
    def cantidadaTaza(cls, nuevaTasa):
        cls.tasaInteres = nuevaTasa
        
    @staticmethod
    def conversionDolaresAEuros(dolares):
        return dolares * 0.05