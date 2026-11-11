
import logging

from Excepciones import Error_SoftwareFJ

from Crear_Registros import *

from Logs import archivo_Logs
archivo_Logs()


# ====================== Simulación de Operaciones ======================


# ====================== Funciones de apoyo para las reservas ======================

# Esta función permite crear, confirmar y procesar una reserva.
# Integra los métodos desarrollados en la clase Reserva.

def crear_y_procesar_reserva(id_reserva, id_cliente, servicio, duracion):

    reserva = nueva_reserva(
        id_reserva=id_reserva,
        id_cliente=id_cliente,
        servicio=servicio,
        duracion=duracion
    )

    reserva.confirmar()
    reserva.procesar()

    print(f"\nReserva procesada correctamente. Costo total: ${reserva.costo_total}")

    return reserva


# Esta función permite crear, confirmar y cancelar una reserva.
# Se utiliza para comprobar el funcionamiento del método cancelar() de Reserva.

def crear_y_cancelar_reserva(id_reserva, id_cliente, servicio, duracion):

    reserva = nueva_reserva(
        id_reserva=id_reserva,
        id_cliente=id_cliente,
        servicio=servicio,
        duracion=duracion
    )

    reserva.confirmar()
    reserva.cancelar()

    print(f"\nReserva {reserva.id_reserva} cancelada correctamente.")

    return reserva


# ====================== Ejecución de la Simulación de Operaciones ======================

def ejecutar_simulacion():

    print("\n" + "=" * 75)
    print("                Iniciando Simulación de Software FJ")

    operaciones = [

        # Operación 1: Registro exitoso de un nuevo cliente.
        ("Operación 1 Registrar Nuevo Cliente: Exitosa",

            lambda: registrar_cliente(
                id_cliente="A001", nombre="Omar Perez", correo="abop12@hot.com", telefono=3132223344)),


        # Operación 2: Prueba de manejo de excepciones por duración incorrecta.
        ("Operación 2 Crear Nueva Reserva: Fallida (Los días deben ser una entrada numérica)",

            lambda: nueva_reserva(
                id_reserva="R001", id_cliente="A001", servicio=sala_mediana, duracion="dos")),


        # Operación 3: Prueba de validación para evitar clientes duplicados.
        ("Operación 3 Registrar Nuevo Cliente: Fallida (El cliente ya se había registrado)",

            lambda: registrar_cliente(
                id_cliente="A002", nombre="Omar Perez", correo="abop12@hot.com", telefono=3012213456)),


        # Operación 4: Creación, confirmación y procesamiento de una reserva.
        # Integra la clase Reserva desarrollada para el proyecto.

        ("Operación 4 Crear Nueva Reserva: Exitoso",

            lambda: crear_y_procesar_reserva(
                id_reserva="R002", id_cliente="A001", servicio=sala_mediana, duracion=2)),


        # Operación 5: Prueba de validación cuando no se proporciona el ID del cliente.
        ("Operación 5 Registrar Nuevo Cliente: Fallida (No seleccionó ID de registro)",

            lambda: registrar_cliente(
                id_cliente="", nombre="Igór Jesús", correo="def@hot.com", telefono=3012213456)),


        # Operación 6: Prueba de validación cuando el ID del cliente no existe.
        ("Operación 6 Crear Nueva Reserva: Fallida (ID de cliente inexistente)",

            lambda: nueva_reserva(
                id_reserva="R003", id_cliente="A002", servicio=alquiler_laptop, duracion=2)),


        # Operación 7: Registro exitoso de un segundo cliente.
        ("Operación 7 Registrar Nuevo Cliente: Exitoso",

            lambda: registrar_cliente(
                id_cliente="A002", nombre="Daniel Torres", correo="fgh12qa@hot.com", telefono=316543344)),


        # Operación 8: Creación exitosa de un nuevo servicio de asesoría.
        ("Operación 8 Crear Nuevo Servicio: Exitoso",

            lambda: crear_servicio_asesoria(
                nombre_servicio="Asesoría Jurídica", tarifa_dia=220000, especialidad="Derecho")),


        # Operación 9: Prueba de manejo de excepciones por falta de tarifa diaria.
        ("Operación 9 Crear Nuevo Servicio: Fallida (Faltó la tarifa por día)",

            lambda: crear_servicio_alquiler(
                nombre_servicio="Alquiler TV", equipo="Sony Smart 50'")),


        # Operación 10: Prueba de validación por capacidad insuficiente de una sala.
        ("operación 10 Crear Nuevo Servicio: Fallido (Capacidad insuficiente de la nueva sala)",

            lambda: crear_servicio_reserva(
                nombre_servicio="Sala Pequeña", tarifa_dia=40000, capacidad=19)),


        # Operación 11: Prueba de confirmación y cancelación de una reserva.
        # Integra los métodos confirmar() y cancelar() de la clase Reserva.

        ("Operación 11 Crear Nueva Reserva: Exitoso (Confirmación y cancelación de reserva)",

            lambda: crear_y_cancelar_reserva(
                id_reserva="R004", id_cliente="A002", servicio=alquiler_laptop, duracion=2))

    ]


    # ====================== Procesamiento de las Operaciones ======================

    for numero, (desc, acc) in enumerate(operaciones, start=1):
        print("="*75 + "\n\n\n" + "=" * 75)
        print(f"{desc}")

        try:
            acc()
            print(f"\nOperación # {numero} procesada correctamente.")

        except Error_SoftwareFJ as error:
            logging.error(f"{error}")
            print(f"\nError controlado {error}")
            print(f"\nError en operación # {numero} controlado correctamente.")

        except Exception as error:
            logging.critical(f"Error inesperado: {error}")
            print(f"\n¡¡Error inesperado!!: {error}\n")
            print(f"Error inesperado en operación # {numero}.")


    # ====================== Resumen Final de la Simulación ======================

    print("="*75 + "\n\n\n" + "="*75)
    sistema.mostrar_resumen_listas()

    print("\n ============   Simulación Finalizada con Éxito   ==================\n")


# ====================== Ejecución del Programa ======================

if __name__ == "__main__":
    ejecutar_simulacion()
