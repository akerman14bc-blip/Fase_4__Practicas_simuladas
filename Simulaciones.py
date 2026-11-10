
import logging

from Excepciones import Error_SoftwareFJ

from Crear_Registros import *

from Logs import archivo_Logs
archivo_Logs()

# ====================== Simulación de Operaciones ======================

def ejecutar_simulacion():

    print("\n" + "=" * 75)
    print("                Iniciando Simulación de Software FJ")

    operaciones = [

        ("Operación 1 Registrar Nuevo Cliente: Exitosa",
         
            lambda: registrar_cliente(
                id_cliente="A001", nombre="Omar Perez", correo="abop12@hot.com", telefono=3132223344)),



        ("Operación 2 Crear Nueva Reserva: Fallida (Los días deben ser una entrada numérica)",
         
            lambda: nueva_reserva(
            ### Faltan atributos  id_cliente="A001", servicio=sala_mediana, dias="dos", pagar_impuesto=False)),


                
        ("Operación 3 Registrar Nuevo Cliente: Fallida (El cliente ya se había registrado)",
         
            lambda: registrar_cliente(
                id_cliente="A002", nombre="Omar Perez", correo="abop12@hot.com", telefono=3012213456)),   



        ("Operación 4 Crear Nueva Reserva: Exitoso",
         
            lambda: nueva_reserva(
            ### Faltan atributos



        ("Operación 5 Registrar Nuevo Cliente: Fallida (No seleccionó ID de registro)",
         
            lambda: registrar_cliente(
                id_cliente="", nombre="Igór Jesús", correo="def@hot.com", telefono=3012213456)),



        ("Operación 6 Crear Nueva Reserva: Fallida (ID de cliente inexistente)",
         
            lambda: nueva_reserva(
          ### Faltan atributos  id_cliente="A002", servicio=alquiler_laptop, dias=2, seguro_daños=True)),



        ("Operación 7 Registrar Nuevo Cliente: Exitoso",
         
            lambda: registrar_cliente(
                id_cliente="A002", nombre="Daniel Torres", correo="fgh12qa@hot.com", telefono=316543344)),


        
        ("Operación 8 Crear Nuevo Servicio: Exitoso",
         
            lambda: crear_servicio_asesoria(
                nombre_servicio="Asesoría Jurídica", tarifa_dia=220000, especialidad="Derecho")),

        
        
        ("Operación 9 Crear Nuevo Servicio: Fallido (Faltó la tarifa por día)",
         
            lambda: crear_servicio_alquiler(
                nombre_servicio="Alquiler TV", equipo="Sony Smart 50'")), 



        ("operación 10 Crear Nuevo Servicio: Fallido (Capacidad insuficiente de la nueva sala)",
         
            lambda: crear_servicio_reserva(
                nombre_servicio="Sala Pequeña", tarifa_dia=40000, capacidad=19))
        
    ]


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

    print("="*75 + "\n\n\n" + "="*75)
    sistema.mostrar_resumen_listas()

    print("\n ============   Simulación Finalizada con Éxito   ==================\n")
