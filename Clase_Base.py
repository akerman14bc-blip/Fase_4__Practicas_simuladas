from abc import ABC, abstractmethod

# =====================   Clase Abstracta Base   ======================

class Entidad_Base(ABC):               # clase abstracta que represente entidades generales del sistema
   
    @abstractmethod
    def mostrar_informacion(self):     # Metodo que se debe implementar en todas las clases que hereden de Entidad_Base
        pass
