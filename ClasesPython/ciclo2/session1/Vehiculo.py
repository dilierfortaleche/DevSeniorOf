class Vehiculo:
    
    def __init__(self, tipo):
        self.topo = tipo
        
    def descripcion(self):
        return f'Este vehiculo es de tipo {self.tipo}'
    
class Moto(Vehiculo):
    
    def __init__(self,tipo, marca):
        super().__inoit__(tipo)
        self.marca = marca
        
moto1 = Moto('motocicleta', 'bucatti')
print (moto1.descripcion())