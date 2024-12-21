class Animal:
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        return "todo animal habla de alguna forma"
    
    def __str__(self):
        return f"el nombre del animal es {self.nombre}"
    
class Perro(Animal):
    
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
        pass
    
    def hablar(self):
        return "guau guauuu"
    
    def __str__(self):
        return f"el  mombre del perro es  {self.nombre} y su raza es {self.raza}"

animal1 = Animal("whisky")
perro1 = Perro("tequila", "doberman")

print(animal1.hablar())
print(animal1.__str__())

print(perro1.hablar())
print(perro1.__str__())