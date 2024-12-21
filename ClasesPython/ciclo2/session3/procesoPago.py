#interfaces en python
from abc import ABC, abstractmethod

class ProcesoPago(ABC):
    
    @abstractmethod
    def procesoPago(self, cantidad: float) -> None:
        pass
    
    @abstractmethod
    def reembolsoPago(self, cantidada: float) -> None:
        pass
    
class Paypal(ProcesoPago):
    
    def procesoPago(self, cantidad: float) -> None:
        print(f'proceso de pago de ${cantidad} por Paypal')
        
    def reembolsoPago(self, transacionId: str) -> None:
        print(f'reembolsando Id transaccion numero: {transacionId} por Paypal')
        
class Stripe(ProcesoPago):
    
    def procesoPago(self, cantidad: float) -> None:
        print(f'proceso de pago de ${cantidad} por Stripe')
        
    def reembolsoPago(self, transacionId: str) -> None:
        print(f'reembolsando Id transaccion numero: {transacionId} por Stripe')
        
        
if __name__ == '__main__':
    ProcesoPaypal = Paypal()
    ProcesoStripe = Stripe()
    
    ProcesoPaypal.procesoPago(500.00)
    ProcesoPaypal.reembolsoPago('123456789')
    
    ProcesoStripe.procesoPago(500.00)
    ProcesoStripe.reembolsoPago('123456789')