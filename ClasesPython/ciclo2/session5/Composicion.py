class Vehiculo:
    def __call__(self, motor):
        self.motor = motor
    
    def encender(self):
        pass
    
class Motor:
    def __init__(self):
        pass
    def iniciar(self):
        pass

class MotorGasolina(Motor):
    def __init__(self):
        pass
    def iniciar(self):
        return f"Motor de gasolina iniciado"
    
class MotorElectrico(Motor):
    def __init__(self):
        pass
    def iniciar(self):
        return f"Motor electrico iniciado"
    
motor_gasolina = MotorGasolina()
motor_electrico = MotorElectrico()

auto_gasolina = Vehiculo(motor_gasolina)
auto_electrico = Vehiculo(motor_electrico)