class Libro:
    
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descripcion(self):
        return f'Libro: {self.titulo} autor: {self.autor}'
    
    def __str__(self):
        return f'libro: {self.titulo} autor: {self.autor} STR'
    
class LibroDigital(Libro):
    
    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self.formato = formato 
    
    def descripcion(self):
        return f'Libro: {self.titulo} autor: {self.autor} formato: {self.formato}'
    
    #opcional
    def __str__(self):
        return f'libro: {self.titulo} autor: {self.autor} STR'
    
libro1 = Libro("La peste","Alberto Campo")
librodigital1 = LibroDigital("El conde de Monte Cristo", "Alejandro Dumas", "PDF")

print(libro1.__str__())
print(libro1.descripcion())

print(librodigital1.__str__())
print(librodigital1.descripcion())
