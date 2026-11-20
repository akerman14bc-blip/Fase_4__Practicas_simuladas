

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

    # Constructor: recibe los datos y las opciones adicionales
    def __init__(
        self, id_reserva, cliente, servicio, duracion,
        pagar_impuesto=False,
        seguro_daños=False,
        descuento_promo=False
    ):

        # Validar el identificador
        if isinstance(id_reserva, bool) or not isinstance(id_reserva, (str, int)):
            raise Reserva_Invalida_Error(
                "El identificador debe ser texto o un numero entero."
            )

        if str(id_reserva).strip() == "":
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
                raise ValueError("La duración no puede ser booleana.")

            duracion = float(duracion)

            if not math.isfinite(duracion):
                raise ValueError("La duración debe ser finita.")

            if duracion <= 0 or duracion > 182:
                raise ValueError("La duración está fuera del rango permitido.")

        except (ValueError, TypeError, OverflowError) as error:
            raise Reserva_Invalida_Error(
                "Duración inválida: debe ser numérica, mayor que 0 y máximo 182 días."
            ) from error

        # Validar las opciones adicionales
        if not isinstance(pagar_impuesto, bool):
            raise Reserva_Invalida_Error(
                "La opción de impuesto debe ser True o False."
            )

        if not isinstance(seguro_daños, bool):
            raise Reserva_Invalida_Error(
                "La opción de seguro contra daños debe ser True o False."
            )

        if not isinstance(descuento_promo, bool):
            raise Reserva_Invalida_Error(
                "La opción de descuento promocional debe ser True o False."
            )

        # Guardar los datos de la reserva
        self.__id_reserva = str(id_reserva).strip()
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion

        # Guardar las opciones adicionales
        self.__pagar_impuesto = pagar_impuesto
        self.__seguro_daños = seguro_daños
        self.__descuento_promo = descuento_promo

        # Inicializar el estado y los valores del costo
        self.__estado = "Pendiente"
        self.__costo_total = 0
        self.__costo_base = 0
        self.__valor_ajuste = 0
        self.__concepto_ajuste = ""
        self.__signo_ajuste = "+"

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
                pagar_impuesto=self.__pagar_impuesto
            )

        elif isinstance(self.__servicio, ServicioAlquilerEquipos):
            return self.__servicio.calcular_costo(
                self.__duracion,
                seguro_daños=self.__seguro_daños
            )

        elif isinstance(self.__servicio, Servicio_Asesoria_Especializada):
            return self.__servicio.calcular_costo(
                self.__duracion,
                descuento_promo=self.__descuento_promo
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

            # Calcular el costo del servicio
            costo = self._calcular_costo_servicio()

            # Validar el costo calculado
            if isinstance(costo, bool):
                raise ValueError("El costo no puede ser booleano.")

            costo = float(costo)

            if not math.isfinite(costo) or costo < 0:
                raise ValueError("El costo debe ser finito y no negativo.")

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

        except (ValueError, TypeError, OverflowError) as error:
            logging.error(
                f"Error en el costo de la reserva {self.__id_reserva}: {error}"
            )
            raise Reserva_Invalida_Error(
                "El costo calculado para la reserva no es válido."
            ) from error

        except Exception as error:
            logging.exception(
                f"Error inesperado en la reserva {self.__id_reserva}."
            )
            raise Reserva_Invalida_Error(
                "Ocurrió un error inesperado al procesar la reserva."
            ) from error

        else:
            # Calcular y guardar el detalle del costo
            self.__costo_base = (
                self.__servicio.get_tarifa_por_dia() * self.__duracion
            )

            if isinstance(self.__servicio, ServicioReservaSalas):
                self.__concepto_ajuste = "Impuesto (8%)"
                self.__valor_ajuste = (
                    self.__servicio.get_impuesto()
                    if self.__pagar_impuesto else 0
                )
                self.__signo_ajuste = "+"

            elif isinstance(self.__servicio, ServicioAlquilerEquipos):
                self.__concepto_ajuste = "Seguro contra daños"
                self.__valor_ajuste = (
                    self.__servicio.get_seguro()
                    if self.__seguro_daños else 0
                )
                self.__signo_ajuste = "+"

            elif isinstance(self.__servicio, Servicio_Asesoria_Especializada):
                self.__concepto_ajuste = "Descuento promocional (10%)"
                self.__valor_ajuste = (
                    self.__servicio.get_promo()
                    if self.__descuento_promo else 0
                )
                self.__signo_ajuste = "-"

            # Actualizar el costo y el estado
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

    # Método heredado de Entidad_Base para mostrar información

    def mostrar_informacion(self):
        informacion = (
            f"Reserva: {self.__id_reserva}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.get_nombre_servicio()}\n"
            f"Duración: {self.__duracion} días\n"
            f"Estado: {self.__estado}\n"
        )

        if self.__estado == "Procesada":
            informacion += (
                f"Costo base: ${self.__costo_base:.0f}\n"
                f"{self.__concepto_ajuste}: "
                f"{self.__signo_ajuste}${self.__valor_ajuste:.0f}\n"
            )

        informacion += f"Costo total: ${self.__costo_total:.0f}"

        return informacion

    # Representar la reserva como texto

    def __str__(self):
        return self.mostrar_informacion()
        
