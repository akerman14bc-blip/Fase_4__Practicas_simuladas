
from abc import ABC, abstractmethod  # Importa herramientas para crear Clases Abstractas y métodos obligatorios

import math          # Importa la librería matemática para utilizar funciones como validación de números finitos

from Clase_Base import Entidad_Base  # Importa la clase base general

from Excepciones import (Servicio_NoDisponible_Error) # Importa excepción para manejar errores en los servicios



# ====================== Clase Abstracta Servicio ======================

# Clase abstracta principal que define la estructura genérica y validaciones de cualquier servicio
class Servicio(Entidad_Base, ABC):

    # Constructor que inicializa y valida nombre y tarifa base
    def __init__(self, nombre_servicio, tarifa_por_dia):

        if not isinstance(nombre_servicio, str): # Valida que el nombre sea texto
            raise Servicio_NoDisponible_Error(
                "El nombre del servicio No debe ser un valor numérico")

        if len(nombre_servicio.strip()) <= 9:  # Valida que el nombre tenga al menos 10 caracteres
            raise Servicio_NoDisponible_Error(
                "El nombre del servicio debe contener al menos 10 caracteres")

        # Valida que la tarifa sea numérica y no sea un valor booleano
        if not isinstance(tarifa_por_dia, (int, float)) or isinstance(tarifa_por_dia, bool):
            raise Servicio_NoDisponible_Error(
                "La tarifa diaria debe ser un valor numérico")

        # Valida que la tarifa sea finita y esté dentro del rango permitido
        if not math.isfinite(tarifa_por_dia):
            raise Servicio_NoDisponible_Error(
                "La tarifa diaria debe ser un valor numérico finito")

        if tarifa_por_dia <= 9400:
            raise Servicio_NoDisponible_Error(
                "La tarifa diaria debe ser superior a $9.400")

        if tarifa_por_dia > 800000:
            raise Servicio_NoDisponible_Error(
                "La tarifa diaria no debe ser mayor de $800.000")

        self.__nombre_servicio = nombre_servicio # Asigna los valores validados a atributos privados
        self.__tarifa_por_dia = tarifa_por_dia

    # Getter para obtener el nombre del servicio
    def get_nombre_servicio(self):
        return self.__nombre_servicio

    # Getter para consultar la tarifa diaria
    def get_tarifa_por_dia(self):
        return self.__tarifa_por_dia

    @staticmethod # Método estático para validar que los días ingresados sean numéricos y válidos
    def _validar_duracion(duracion):

        try:
            # Evita que True o False sean aceptados como números
            if isinstance(duracion, bool):
                raise ValueError("La duración no puede ser un valor booleano")

            duracion = float(duracion) # Intenta convertir la duración a número decimal

        except (ValueError, TypeError, OverflowError) as error:
            raise Servicio_NoDisponible_Error(
                "Los días de reserva deben ser un valor numérico válido"
            ) from error

        if not math.isfinite(duracion) or duracion <= 0:
            raise Servicio_NoDisponible_Error(
                "Los días de reserva deben ser mayores que cero")

        if duracion > 182:
            raise Servicio_NoDisponible_Error(
                "La reserva no puede superar los 6 meses")

        return duracion

    @staticmethod # Método estático para validar que los parámetros booleanos opcionales no sean nulos
    def _validar_opcion(valor, nombre):

        if valor is None:   # Valida que se ingrese un parámetro
            raise Servicio_NoDisponible_Error(
                "Debe ingresar el parámetro opcional")

        if not isinstance(valor, bool):  # Valida que se elija la opción True o False
            raise Servicio_NoDisponible_Error(
                f"{nombre} debe ser 'True' o 'False'.")

        return valor

    @abstractmethod  # Método obligatorio que implementarán las clases hijas para mostrar su información
    def mostrar_informacion(self):
        pass

    @abstractmethod # Método obligatorio para calcular el costo total adaptado a cada tipo de servicio
    def calcular_costo(self, duracion):
        pass




# Clase que hereda de Servicio para gestionar la reserva específica de salas
class ServicioReservaSalas(Servicio):

    # Constructor que inicializa los datos de la sala y valida su capacidad mínima
    def __init__(self, nombre_servicio, tarifa_por_dia, capacidad_personas):
        super().__init__(nombre_servicio, tarifa_por_dia)

        # Valida que la capacidad sea un número entero y no un valor booleano
        if not isinstance(capacidad_personas, int) or isinstance(capacidad_personas, bool):
            raise Servicio_NoDisponible_Error(
                "La capacidad de la sala debe ser un número entero")

        if capacidad_personas <= 19:   # Exige que la capacidad sea de al menos 20
            raise Servicio_NoDisponible_Error(
                "La capacidad de la sala debe ser de mínimo 20 personas")

        if capacidad_personas > 100:
            raise Servicio_NoDisponible_Error(
                "La capacidad de la sala no debe superar las 100 personas")

        self.__capacidad_personas = capacidad_personas   # Asigna la capacidad de forma privada

        # Inicializa el impuesto desde la creación del servicio
        self.impuesto = 0

    # Getter para obtener la capacidad de la sala
    def get_capacidad_personas(self):
        return self.__capacidad_personas

    # Devuelve el valor del impuesto aplicado
    def get_impuesto(self):
        return self.impuesto

    # Retorna un texto detallado con las características y costos de la sala
    def mostrar_informacion(self):
        return (
            f"Servicio: {self.get_nombre_servicio()} | "
            f"Capacidad: {self.__capacidad_personas} personas | "
            f"Tarifa diaria: ${self.get_tarifa_por_dia():.0f} | "
            f"Impuestos del 8% : + {self.get_impuesto():.0f} adicional"
        )

    # Calcula el costo total de la reserva aplicando un impuesto opcional del 8%
    def calcular_costo(self, dias, pagar_impuesto=None):

        try:
            dias = self._validar_duracion(dias)   # Valida la cantidad de días

            self._validar_opcion(
                pagar_impuesto, "Aplicar impuestos"
            )   # Valida el parámetro de impuestos

            costo = self.get_tarifa_por_dia() * dias
            self.impuesto = 0

            if pagar_impuesto:
                self.impuesto = costo * 0.08

            return costo + self.impuesto

        except Servicio_NoDisponible_Error as error:
            raise Servicio_NoDisponible_Error(
                f"Error calculando reserva de salas: {error}"
            ) from error



# Clase que hereda de Servicio para gestionar el alquiler de equipos tecnológicos
class ServicioAlquilerEquipos(Servicio):

    # Constructor que inicializa el servicio de alquiler y valida el tipo de equipo
    def __init__(self, nombre_servicio, tarifa_por_dia, equipo):
        super().__init__(nombre_servicio, tarifa_por_dia)

        if not isinstance(equipo, str): # Valida que el equipo especificado sea texto válido
            raise Servicio_NoDisponible_Error(
                "El tipo de equipo no debe ser un valor numérico")

        if len(equipo.strip()) <= 3:   # Valida que el texto tenga al menos 4 caracteres
            raise Servicio_NoDisponible_Error(
                "El tipo de equipo debe tener al menos 4 caracteres")

        if len(equipo.strip()) > 18:
            raise Servicio_NoDisponible_Error(
                "El tipo de equipo debe tener máximo 18 caracteres")

        self.__equipo = equipo

        # Inicializa el seguro desde la creación del servicio
        self.seguro = 0

    # Devuelve el tipo de equipo alquilado
    def get_equipo(self):
        return self.__equipo

    # Devuelve el costo adicional aplicado por seguro
    def get_seguro(self):
        return self.seguro

    # Retorna un texto detallado con la información del equipo y seguro contra daños
    def mostrar_informacion(self):
        return (
            f"Servicio: {self.get_nombre_servicio()} | "
            f"Equipo: {self.__equipo} | "
            f"Tarifa diaria: ${self.get_tarifa_por_dia():.0f} | "
            f"Seguro contra daños: + $ {self.get_seguro():.0f} adicional"
        )

    # Calcula el costo del alquiler de equipos sumando un seguro opcional fijo de $50.000
    def calcular_costo(self, dias, seguro_daños=None):

        try:
            dias = self._validar_duracion(dias)   # Valida la duración en días

            self._validar_opcion(
                seguro_daños, "Seguro contra daños"
            )  # Valida el parámetro del seguro

            costo = self.get_tarifa_por_dia() * dias
            self.seguro = 0

            if seguro_daños:
                self.seguro = 50000

            return costo + self.seguro

        except Servicio_NoDisponible_Error as error:
            raise Servicio_NoDisponible_Error(
                f"Error calculando alquiler de equipos: {error}"
            ) from error



# Clase que hereda de Servicio para gestionar asesorías especializadas
class Servicio_Asesoria_Especializada(Servicio):

    # Constructor que inicializa la asesoría y valida el tipo de área
    def __init__(self, nombre_servicio, tarifa_por_dia, area_especialidad):
        super().__init__(nombre_servicio, tarifa_por_dia)

        if not isinstance(area_especialidad, str):   # Valida que el área de especialidad sea un texto válido
            raise Servicio_NoDisponible_Error(
                "El nombre del área de especialidad no debe ser un valor numérico")

        if len(area_especialidad.strip()) <= 4: # Valida que el área de especialidad tenga al menos 5 caracteres
            raise Servicio_NoDisponible_Error(
                "El nombre del área de especialidad debe contener al menos 5 caracteres")

        if len(area_especialidad.strip()) > 15:
            raise Servicio_NoDisponible_Error(
                "El nombre del área de especialidad puede tener máximo 15 caracteres")

        self.__area_especialidad = area_especialidad

        # Inicializa la promoción desde la creación del servicio
        self.promo = 0

    # Devuelve el área de especialidad de la asesoría
    def get_area_especialidad(self):
        return self.__area_especialidad

    # Devuelve el valor total del descuento promocional
    def get_promo(self):
        return self.promo

    # Retorna un texto detallado con la información de la asesoría y los impuestos aplicados
    def mostrar_informacion(self):
        return (
            f"Servicio: {self.get_nombre_servicio()} | "
            f"Área: {self.__area_especialidad} | "
            f"Tarifa por día: ${self.get_tarifa_por_dia():.0f} | "
            f"Descuento promocional del 10% : -${self.get_promo():.0f}"
        )

    # Calcula el costo total de la reserva de asesoría aplicando opcionalmente un descuento del 10%
    def calcular_costo(self, dias, descuento_promo=None):

        try:
            dias = self._validar_duracion(dias)  # Valida los días mediante el método estático

            self._validar_opcion(
                descuento_promo, "Descuento promocional"
            ) # Valida el parámetro de descuento

            costo = self.get_tarifa_por_dia() * dias
            self.promo = 0

            if descuento_promo:
                self.promo = costo * 0.10

            return costo - self.promo

        except Servicio_NoDisponible_Error as error:
            raise Servicio_NoDisponible_Error(
                f"Error calculando asesoría especializada: {error}"
            ) from error


