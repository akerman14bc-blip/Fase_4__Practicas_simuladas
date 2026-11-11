
from abc import ABC, abstractmethod  # Importa herramientas para crear Clases Abstractas y métodos obligatorios

import math          # Importa la librería matemática para utilizar funciones como validación de números finitos

from Clase_Base import Entidad_Base  # Importa la clase base general

from Excepciones import (Servicio_NoDisponible_Error) # Importa excepción para manejar errores en los servicios



# ====================== Clase Abstracta Servicio ======================


class Servicio(Entidad_Base, ABC):

    def __init__(self, nombre_servicio, tarifa_por_dia):

        if not isinstance(nombre_servicio, str):
            raise Servicio_NoDisponible_Error(
                "El nombre del servicio no debe ser un valor numérico"
            )

        if len(nombre_servicio.strip()) <= 9:
            raise Servicio_NoDisponible_Error(
                "El nombre del servicio debe contener al menos 10 caracteres"
            )

        if not isinstance(tarifa_por_dia, (int, float)) or isinstance(tarifa_por_dia, bool):
            raise Servicio_NoDisponible_Error(
                "La tarifa diaria debe ser un valor numérico"
            )

        if not math.isfinite(tarifa_por_dia) or tarifa_por_dia <= 0:
            raise Servicio_NoDisponible_Error(
                "La tarifa diaria debe ser mayor de $ 9.500"
            )

        self.__nombre_servicio = nombre_servicio
        self.__tarifa_por_dia = tarifa_por_dia

    def get_nombre_servicio(self):
        return self.__nombre_servicio

    def get_tarifa_por_dia(self):
        return self.__tarifa_por_dia

    @staticmethod
    def _validar_duracion(duracion):

        try:
            if isinstance(duracion, bool):
                raise ValueError("La duración no puede ser un valor booleano")

            duracion = float(duracion)

        except (ValueError, TypeError, OverflowError) as error:
            raise Servicio_NoDisponible_Error(
                "Los días de reserva deben ser un valor numérico válido"
            ) from error

        if not math.isfinite(duracion) or duracion <= 0:
            raise Servicio_NoDisponible_Error(
                "Los días de reserva deben ser mayor que cero."
            )

        return duracion

    @staticmethod
    def _validar_opcion(valor, nombre):

        if valor is None:
            raise Servicio_NoDisponible_Error(
                "Debe ingresar el parámetro opcional"
            )

        if not isinstance(valor, bool):
            raise Servicio_NoDisponible_Error(
                f"{nombre} debe ser 'True' o 'False'."
            )

        return valor

    @abstractmethod
    def mostrar_informacion(self):
        pass

    @abstractmethod
    def calcular_costo(self, duracion):
        pass


# ====================== Servicio de Reserva de Salas ======================

class ServicioReservaSalas(Servicio):

    def __init__(self, nombre_servicio, tarifa_por_dia, capacidad_personas):

        super().__init__(nombre_servicio, tarifa_por_dia)

        if not isinstance(capacidad_personas, (int, float)) or isinstance(capacidad_personas, bool):
            raise Servicio_NoDisponible_Error(
                "La capacidad de la sala debe ser un valor numérico"
            )

        if not math.isfinite(capacidad_personas) or capacidad_personas <= 19:
            raise Servicio_NoDisponible_Error(
                "La capacidad de la sala debe ser de mínimo 20 personas"
            )

        self.__capacidad_personas = capacidad_personas

        # Inicializa el impuesto desde la creación del servicio
        self.impuesto = 0

    def get_capacidad_personas(self):
        return self.__capacidad_personas

    def get_impuesto(self):
        return self.impuesto

    def mostrar_informacion(self):

        return (
            f"Servicio: {self.get_nombre_servicio()} | "
            f"Capacidad: {self.__capacidad_personas} personas | "
            f"Tarifa diaria: ${self.get_tarifa_por_dia():.0f} | "
            f"Impuestos del 8% : + {self.get_impuesto():.0f} adicional"
        )

    def calcular_costo(self, dias, pagar_impuesto=None):

        try:
            dias = self._validar_duracion(dias)

            self._validar_opcion(
                pagar_impuesto, "Aplicar impuestos"
            )

            costo = self.get_tarifa_por_dia() * dias

            self.impuesto = 0

            if pagar_impuesto:
                self.impuesto = costo * 0.08

            return costo + self.impuesto

        except Servicio_NoDisponible_Error as error:
            raise Servicio_NoDisponible_Error(
                f"Error calculando reserva de salas: {error}"
            ) from error


# ====================== Servicio de Alquiler de Equipos ======================

class ServicioAlquilerEquipos(Servicio):

    def __init__(self, nombre_servicio, tarifa_por_dia, equipo):

        super().__init__(nombre_servicio, tarifa_por_dia)

        if not isinstance(equipo, str):
            raise Servicio_NoDisponible_Error(
                "El tipo de equipo no debe ser un valor numérico"
            )

        if len(equipo.strip()) <= 3:
            raise Servicio_NoDisponible_Error(
                "El tipo de equipo debe tener al menos 4 caracteres"
            )

        self.__equipo = equipo

        # Inicializa el seguro desde la creación del servicio
        self.seguro = 0

    def get_equipo(self):
        return self.__equipo

    def get_seguro(self):
        return self.seguro

    def mostrar_informacion(self):

        return (
            f"Servicio: {self.get_nombre_servicio()} | "
            f"Equipo: {self.__equipo} | "
            f"Tarifa diaria: ${self.get_tarifa_por_dia():.0f} | "
            f"Seguro contra daños: + $ {self.get_seguro():.0f} adicional"
        )

    def calcular_costo(self, dias, seguro_daños=None):

        try:
            dias = self._validar_duracion(dias)

            self._validar_opcion(
                seguro_daños, "Seguro contra daños"
            )

            costo = self.get_tarifa_por_dia() * dias

            self.seguro = 0

            if seguro_daños:
                self.seguro = 50000

            return costo + self.seguro

        except Servicio_NoDisponible_Error as error:
            raise Servicio_NoDisponible_Error(
                f"Error calculando alquiler de equipos: {error}"
            ) from error


# ====================== Servicio de Asesoría Especializada ======================

class Servicio_Asesoria_Especializada(Servicio):

    def __init__(self, nombre_servicio, tarifa_por_dia, area_especialidad):

        super().__init__(nombre_servicio, tarifa_por_dia)

        if not isinstance(area_especialidad, str):
            raise Servicio_NoDisponible_Error(
                "El nombre del área de especialidad no debe ser un valor numérico"
            )

        if len(area_especialidad.strip()) <= 4:
            raise Servicio_NoDisponible_Error(
                "El nombre del área de especialidad debe contener al menos 5 caracteres"
            )

        self.__area_especialidad = area_especialidad

        # Inicializa la promoción desde la creación del servicio
        self.promo = 0

    def get_area_especialidad(self):
        return self.__area_especialidad

    def get_promo(self):
        return self.promo

    def mostrar_informacion(self):

        return (
            f"Servicio: {self.get_nombre_servicio()} | "
            f"Área: {self.__area_especialidad} | "
            f"Tarifa por día: ${self.get_tarifa_por_dia():.0f} | "
            f"Descuento promocional del 10%: -${self.get_promo():.0f}"
        )

    def calcular_costo(self, dias, descuento_promo=None):

        try:
            dias = self._validar_duracion(dias)

            self._validar_opcion(
                descuento_promo, "Descuento promocional"
            )

            costo = self.get_tarifa_por_dia() * dias

            self.promo = 0

            if descuento_promo:
                self.promo = costo * 0.10

            return costo - self.promo

        except Servicio_NoDisponible_Error as error:
            raise Servicio_NoDisponible_Error(
                f"Error calculando asesoría especializada: {error}"
            ) from error

