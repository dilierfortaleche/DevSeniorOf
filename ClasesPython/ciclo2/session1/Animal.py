class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def saludar (self):
        return f'Mi animalito se llama {self.name} y tiene {self.age} años'
    
animall = Animal("Ginebra", 3)

print (animall.name)
print(animall.age)
print(animall.saludar())

