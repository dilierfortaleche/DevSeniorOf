class Vehiculos:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def descripcion(self):
        return f"El vehiculo es de marca {self.marca}, modelo {self.modelo}"
        
class Auto(Vehiculos):
    
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
        
    def descripcion(self):
        return f"El vehiculo es de marca {self.marca}, modelo {self.modelo} y tiene {self.puertas} puertas"
    
mi_auto = Auto("chevrolet", "Sedan", 4)
print(mi_auto.descripcion())