class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saludar(self):
        return f'hola mi nombre es {self.nombre} y tengo {self.edad} años'
    