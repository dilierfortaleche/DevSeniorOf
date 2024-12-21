class Empleado:
    
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self._salario = salario
        self.salarioMinimo = 1300000
        
    def mostrarInformacion(self):
        return f"nombre: {self.nombre}, salario{self._salario}"
    
    def obtenerSalario(self):
        return self._salario
    
    def establecerSalario(self, nuevoSalario):
        if nuevoSalario < 1300000:
            return f"salario no puerde ser menos al salario minimo"
        self._salario = nuevoSalario
        return f"el nuevo salario es {self._salario}"
        
    def asignacionesSalariales (self):
        pass
    
    def deduccionesSalariales(self):
        pass
    
Empleado1 = Empleado("Carlos", 1500000)

print(Empleado1.mostrarInformacion())
print(Empleado1.obtenerSalario())
print(Empleado1.establecerSalario(1200000))
print(Empleado1.establecerSalario(2500000))