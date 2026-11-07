import logging

import math

from abc import ABC, abstractmethod

from Clase_Base import Entidad_Base

from Excepciones import (Servicio_NoDisponible_Error)

# ====================== CLASE ABSTRACTA SERVICIO ======================

class Servicio(Entidad_Base, ABC):

    def __init__(self, nombre_servicio, tarifa_por_dia):

        if not isinstance (nombre_servicio, str) or len(nombre_servicio.strip()) <= 7:
                raise Servicio_NoDisponible_Error("El nombre del servicio no es valido")
        
        if not isinstance(tarifa_por_dia, (int, float)):
                raise Servicio_NoDisponible_Error("La tarifa debe ser numérica")
        
        if tarifa_por_dia <= 0:
                raise Servicio_NoDisponible_Error("La tarifa debe ser mayor que 0")
        
        self.__nombre_servicio = nombre_servicio
        self.__tarifa_por_dia = tarifa_por_dia


    def get_nombre_servicio(self):
        return self.__nombre_servicio
    
    def get_tarifa_por_dia(self):
        return self.__tarifa_por_dia


    @staticmethod
    def _validar_duracion(duracion):
       
        try:
            duracion = float(duracion)
        except (ValueError, TypeError, OverflowError) as error:
            raise Servicio_NoDisponible_Error("La duración debe ser un valor numérico.") from error

        if not math.isfinite(duracion) or duracion <= 0:
            raise Servicio_NoDisponible_Error("La duración debe ser mayor que cero.")
        return duracion
    
    @staticmethod
    def _validar_opcion(valor, nombre):
        if valor is None:
            raise Servicio_NoDisponible_Error("Debe ingresar el parametro opcional")
        if not isinstance(valor, bool):
            raise Servicio_NoDisponible_Error(f"{nombre}: debe ser True o False.")
        return valor
        

    @abstractmethod
    def mostrar_informacion(self):
        pass
    
    @abstractmethod
    def calcular_costo(self, duracion):
        pass

