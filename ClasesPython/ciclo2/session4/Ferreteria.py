#import threading as th
from abc import ABC, abstractmethod

# Patron Singleton
class SistemaFacturacion:
    
    _instancia = None
    #_lock = th.Lock()
    
    def _new_(cls, *args, **kwargs):
        
        if not cls._instancia:
            cls._instancia = super(SistemaFacturacion, cls).__new__(cls)
            cls._instancia._inicializacionHistorico()
        return cls._instancia
    
    #opcional
        """
        with cls._lock:
            if cls._instancia is None:
                cls._instancia = super(SistemaFacturacion, cls).__new__(cls)
                cls._instancia._inicializacionHistorico()
                return cls._instancia
                """
                
    def _inicializacionHistorico(self):
        self.historial = []
        print("sistema de facturacion iniciado")
        
    def registrarOperacion(self, operacion):
        self.historial.append(operacion)
        print(f"la operacion fue registrada: {operacion}")
        
#Clase abstracta = Superclase
class ProcesoNegocio(ABC):
    
    @abstractmethod
    def ejecutar(self):
        pass
    

class ProsesarPedido(ProcesoNegocio):
    
    def ejecutar(self):
        print("procesando pedido...")
        return "pedido procesado"
    
class ProcesarFactura(ProcesoNegocio):
    
    def ejecutar(self):
        print("procesando factura...")
        return "factura procesada"
    
#crear la fabrica ( patron de diseño  Factory)
class FabricaProcesosNegocio:
    
    @staticmethod
    def crearProcesoNegocio(tipoProceso):
        if tipoProceso == "pedido":
            return ProsesarPedido()
        elif tipoProceso == "factura":
            return ProcesarFactura()
        else:
            raise ValueError(f"el proceso {tipoProceso} no existe")

if __name__ == "__name__":
    
    Sistema_Facturacion = SistemaFacturacion()
    
    proceso1 =FabricaProcesosNegocio.crearProcesoNegocio("pedido")
    proceso2 = FabricaProcesosNegocio.crearProcesoNegocio("factura")
    
    resultadoPedido1 = proceso1.ejecutar()
    Sistema_Facturacion.registrarOperacion(resultadoPedido1)
    
    resultadoPedido2 = proceso2.ejecutar()
    Sistema_Facturacion.registrarOperacion(resultadoPedido2)
    
    print("\n Historico de procesos de negocios")
    for operacion in Sistema_Facturacion.historial:
        print(f"Tranzacion: {operacion}")