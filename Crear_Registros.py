
from Servicio import (ServicioReservaSalas, ServicioAlquilerEquipos, Servicio_Asesoria_Especializada)

from Cliente import Cliente

from Reserva import Reserva

from Excepciones import *

from Listas import Gestion_Listas

import logging


sistema = Gestion_Listas()



def registrar_cliente(id_cliente=None, nombre=None, correo=None, telefono=None):

    try:
        logging.info(f"[Registro]: Iniciando Registro de Nuevo Cliente: {nombre}")

        if id_cliente is None or nombre is None or correo is None or telefono is None:
            raise Cliente_Invalido_Error(
                "Debe agregar todos los parametros: 'ID Cliente' | 'Nombre' | 'Correo' | 'Telefono'")
        
        cliente = Cliente(id_cliente, nombre, correo, telefono)
        sistema.registrar_cliente(cliente)
        logging.info(f"[Registro]: Cliente registrado con éxito: {cliente}")
    
    except Error_SoftwareFJ as error:
        logging.warning(f"No se pudo registrar al cliente {nombre}")
        raise Cliente_Invalido_Error(f"al registrar nuevo cliente: {error}")

    print("")
    print("Registro de nuevo cliente creado con éxito\n")
    print(f"ID cliente: {id_cliente} | Nombre: {nombre} | Correo: {correo} | Teleforno: {telefono}")


def nueva_reserva#( ??? , id_cliente=None, servicio=None, dias/duracion =None, **kwargs):  Faltan atributos 

    try:
        logging.info(f"[Registro]: Iniciando Registro de Nueva Reserva: ID")

# Faltan excepciones
        
        cliente = sistema.buscar_cliente(id_cliente)
        if cliente is None:
            raise Reserva_Invalida_Error(f"No existe un cliente registrado con ID {id_cliente}")
        
###     reserva = Reserva(id_reserva, cliente, servicio, dias, **kwargs)     !! Faltan Atributos
        sistema. registrar_reserva(reserva)
        logging.info(f"[Reserva]: Éxito al crear la reserva: ID")

    except Error_SoftwareFJ as error:
        logging.warning(f"No se pudo registrar la reserva : ID")
        raise Reserva_Invalida_Error(f"al registrar la reserva ID: {error}")
            

    print("")
    print("Nueva Reserva creada con éxito\n")
    print(f"ID Reserva:  | ID Cliente: {id_cliente} \n")
    print(servicio.mostrar_informacion())
    print("")
    print(reserva.mostrar_informacion())

    


def crear_servicio_alquiler(nombre_servicio=None, tarifa_dia=None, equipo=None):

    try:
        logging.info(f"[Servicios]: Iniciando Creación de un Nuevo servicio de Alquiler: {nombre_servicio}")

        if equipo is None or tarifa_dia is None or nombre_servicio is None:
            raise Servicio_NoDisponible_Error(
                "Debe agregar todos los parametros: 'Nombre del servicio' | 'Tarifa por día' | 'Tipo de equipo'")  
        
        servicio = ServicioAlquilerEquipos(nombre_servicio, tarifa_dia, equipo)
        sistema.registrar_servicio(servicio)
        sistema.registrar_servicio(servicio)
        logging.info(f"[Servicio]: Nuevo Servicio de Alquiler creado:{servicio}")
    
    except Error_SoftwareFJ as error:
        logging.warning(f"No se puedo crear el servicio de Alquiler: {nombre_servicio}")
        raise Servicio_NoDisponible_Error(f"al crear nuevo servicio de Alquiler: {error}")
    
    print("")
    print("Servicio de Alquiler de Equipos creado con éxito\n")
    print(f"Nombre: {nombre_servicio} | Tarifa diaria: {tarifa_dia} | Equipo: {equipo}")


def crear_servicio_reserva(nombre_servicio=None, tarifa_dia=None, capacidad=None):

    try:
        logging.info(
            f"[Servicios]: Iniciando Creación de un Nuevo servicio de Reserva de Salas: {nombre_servicio}")

        if capacidad is None or tarifa_dia is None or nombre_servicio is None:
            raise Servicio_NoDisponible_Error(
                "Debe agregar todos los parametros: 'Nombre del servicio' | 'Tarifa por día' | 'Capacidad de Sala'")
        
        servicio = ServicioReservaSalas(nombre_servicio, tarifa_dia, capacidad)
        sistema.registrar_servicio(servicio)
        sistema.registrar_servicio(servicio)
        logging.info(f"[Servicio]: Nuevo Servicio de Reserva de Salas creado:{servicio}")

    except Error_SoftwareFJ as error:
        logging.warning(f"No se puedo crear el servicio de Reserva de Salas: {nombre_servicio}")
        raise Servicio_NoDisponible_Error(f"al crear nuevo servicio de Reserva de Salas: {error}")

    print("")
    print("Servicio de Reserva de Salas creado con éxito\n")
    print(f"Nombre: {nombre_servicio} | Tarifa diaria: {tarifa_dia} | Capacidad: {capacidad}")


def crear_servicio_asesoria(nombre_servicio=None, tarifa_dia=None, especialidad=None):

    try:
        logging.info(f"[Servicios]: Iniciando Creación de un Nuevo servicio de Asesoría: {nombre_servicio}")
        
        if especialidad is None or tarifa_dia is None or nombre_servicio is None:
            raise Servicio_NoDisponible_Error(
                "Debe agregar todos los parametros: 'Nombre del servicio' | 'Tarifa por día' | 'Especialidad'")
        
        servicio = Servicio_Asesoria_Especializada(nombre_servicio, tarifa_dia, especialidad)
        sistema.registrar_servicio(servicio)
        logging.info(f"[Servicio]: Nuevo servicio de Asesoría creado:{servicio}")

    except Error_SoftwareFJ as error:
        logging.warning(f"No se puedo crear el servicio de Asesoría: {nombre_servicio}")
        raise Servicio_NoDisponible_Error(f"al crear nuevo servicio de Asesoría: {error}")
                               
    print("")
    print("Servicio de Asesoría Especilizada creado con éxito\n")
    print(f"Nombre: {nombre_servicio} | Tarifa diaria: {tarifa_dia} | Área: {especialidad}")

sala_mediana = ServicioReservaSalas("Reserva de sala Mediana", 80000, 50)
alquiler_laptop = ServicioAlquilerEquipos("Alquiler de Laptop", 30000, "Laptop Core i5 HP")
asesoria_ti = Servicio_Asesoria_Especializada("Asesoría en Programación", 90000, "Desarrollo")
