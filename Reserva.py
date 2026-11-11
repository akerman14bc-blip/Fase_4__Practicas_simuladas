
# ================================================================
# FASE 4 - COMPONENTE PRACTICO: PRACTICAS SIMULADAS
# Curso: Programacion
# Proyecto: Sistema Integral de Gestion de Clientes, Servicios y
# Reservas - Software FJ
# ================================================================

import logging
import math

from Clase_Base import Entidad_Base
from Clientes import Cliente
from Servicio import (
    Servicio,
    ServicioReservaSalas,
    ServicioAlquilerEquipos,
    Servicio_Asesoria_Especializada
)
from Excepciones import Reserva_Invalida_Error, Servicio_NoDisponible_Error


class Reserva(Entidad_Base):

    def __init__(self, id_reserva, cliente, servicio, duracion):

        # Validar el identificador de la reserva
        if id_reserva is None or str(id_reserva).strip() == "":
            raise Reserva_Invalida_Error(
                "El identificador de la reserva es obligatorio."
            )

        # Validar el cliente
        if not isinstance(cliente, Cliente):
            raise Reserva_Invalida_Error(
                "La reserva debe tener un cliente válido."
            )

        # Validar el servicio
        if not isinstance(servicio, Servicio):
            raise Reserva_Invalida_Error(
                "La reserva debe tener un servicio válido."
            )

        # Validar la duración
        try:
            if isinstance(duracion, bool):
                raise ValueError("La duración no puede ser un valor booleano.")

            duracion = float(duracion)

            if not math.isfinite(duracion) or duracion <= 0:
                raise ValueError("La duración debe ser mayor que cero.")

        except (ValueError, TypeError, OverflowError) as error:
            raise Reserva_Invalida_Error(
                "La duración de la reserva no es válida."
            ) from error

        # Guardar los datos de la reserva
        self.__id_reserva = str(id_reserva).strip()
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"
        self.__costo_total = 0

    # Propiedades para consultar los datos de la reserva

    @property
    def id_reserva(self):
        return self.__id_reserva

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    @property
    def costo_total(self):
        return self.__costo_total

    @property
    def id_cliente(self):
        return self.__cliente.id_cliente

    # Método para confirmar la reserva

    def confirmar(self):
        try:
            if self.__estado != "Pendiente":
                raise Reserva_Invalida_Error(
                    "Solamente se pueden confirmar reservas pendientes."
                )

            self.__estado = "Confirmada"

            logging.info(
                f"Reserva {self.__id_reserva} confirmada correctamente."
            )

            return True

        except Reserva_Invalida_Error as error:
            logging.error(
                f"Error al confirmar la reserva {self.__id_reserva}: {error}"
            )
            raise

    # Método para cancelar la reserva

    def cancelar(self):
        try:
            if self.__estado not in ["Pendiente", "Confirmada"]:
                raise Reserva_Invalida_Error(
                    "No se puede cancelar una reserva procesada o cancelada."
                )

            self.__estado = "Cancelada"

            logging.info(
                f"Reserva {self.__id_reserva} cancelada correctamente."
            )

            return True

        except Reserva_Invalida_Error as error:
            logging.error(
                f"Error al cancelar la reserva {self.__id_reserva}: {error}"
            )
            raise

    # Método interno para calcular el costo según el servicio

    def _calcular_costo_servicio(self):

        if isinstance(self.__servicio, ServicioReservaSalas):
            return self.__servicio.calcular_costo(
                self.__duracion,
                pagar_impuesto=False
            )

        elif isinstance(self.__servicio, ServicioAlquilerEquipos):
            return self.__servicio.calcular_costo(
                self.__duracion,
                seguro_daños=False
            )

        elif isinstance(self.__servicio, Servicio_Asesoria_Especializada):
            return self.__servicio.calcular_costo(
                self.__duracion,
                descuento_promo=False
            )

        else:
            raise Servicio_NoDisponible_Error(
                "El tipo de servicio no está reconocido por el sistema."
            )

    # Método para procesar la reserva

    def procesar(self):
        try:
            if self.__estado != "Confirmada":
                raise Reserva_Invalida_Error(
                    "Para procesar la reserva primero debe estar confirmada."
                )

            costo = self._calcular_costo_servicio()

        except Reserva_Invalida_Error as error:
            logging.error(
                f"Error al procesar la reserva {self.__id_reserva}: {error}"
            )
            raise

        except Servicio_NoDisponible_Error as error:
            logging.error(
                f"Error en el servicio de la reserva {self.__id_reserva}: {error}"
            )
            raise Reserva_Invalida_Error(
                "No fue posible procesar el servicio de la reserva."
            ) from error

        except Exception as error:
            logging.exception(
                f"Error inesperado en la reserva {self.__id_reserva}."
            )
            raise Reserva_Invalida_Error(
                "Ocurrió un error inesperado al procesar la reserva."
            ) from error

        else:
            self.__costo_total = costo
            self.__estado = "Procesada"

            logging.info(
                f"Reserva {self.__id_reserva} procesada. "
                f"Costo total: ${self.__costo_total}"
            )

            return self.__costo_total

        finally:
            logging.info(
                f"Finalizó el intento de procesamiento de la reserva "
                f"{self.__id_reserva}."
            )

    # Método heredado de Entidad_Base

    def mostrar_informacion(self):
        return (
            f"Reserva: {self.__id_reserva}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.get_nombre_servicio()}\n"
            f"Duración: {self.__duracion} días\n"
            f"Estado: {self.__estado}\n"
            f"Costo total: ${self.__costo_total}"
        )

    def __str__(self):
        return self.mostrar_informacion()
