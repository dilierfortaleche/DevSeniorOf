class Animall:
    
    cantidadAnimales = 0
    
    def __init__(self, name):
        self.name = name
        Animall.cantidadAnimales += 1
        
    @classmethod #decorador
    def totalAnimales(cls):
        return f'Tengo {cls.cantidadAnimales} animalitos'

animalito1 = Animall('Ron')
animalito2 =  Animall('Rayo')
animalito25 = Animall('Toby')

print(Animall.totalAnimales())