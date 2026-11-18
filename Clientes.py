# Alfonso Morales
# MÓDULO: Clientes.py
# se realizo la  Implementación de la entidad Cliente aplicando principios de POO:
# abstracción, herencia, encapsulación estricta y excepciones.

# Se  importa el módulo estándar logging para registrar eventos y errores en archivo

import logging

# Se importa la clase abstracta padre desde el archivo de arquitectura base
from Clase_Base import Entidad_Base

# Se importa la excepción personalizada específica para errores de clientes
from Excepciones import Cliente_Invalido_Error

# Configuración del archivo de logs para persistencia de fallos y auditoría
# Registra fecha, hora, nivel de severidad y descripción en 'sistema_fj.log'

from Logs import archivo_Logs

archivo_Logs()


# ====================== Clase Cliente ======================

class Cliente(Entidad_Base):

    def __init__(self, id_cliente, nombre, correo, telefono):
        super().__init__()

        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    # ====================== Validación ID Cliente ======================

    @property
    def id_cliente(self):
        return self.__id_cliente

    @id_cliente.setter
    def id_cliente(self, valor):

        # No permite valores vacíos, None, booleanos ni tipos diferentes
        # de texto o números enteros.
        if (
            valor is None
            or isinstance(valor, bool)
            or not isinstance(valor, (str, int))
            or not str(valor).strip()
        ):
            raise Cliente_Invalido_Error(
                "El ID del cliente no puede estar vacío o ser inválido."
            )

        self.__id_cliente = str(valor).strip()

    # ====================== Validación Nombre ======================

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):

        if not isinstance(valor, str) or not valor.strip():
            raise Cliente_Invalido_Error(
                "El nombre del cliente debe ser un texto válido."
            )

        if len(valor.strip()) < 3:
            raise Cliente_Invalido_Error(
                "El nombre del cliente debe tener mínimo 3 caracteres."
            )

        self.__nombre = valor.strip()

    # ====================== Validación Correo ======================

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):

        if not isinstance(valor, str):
            raise Cliente_Invalido_Error(
                "El correo electrónico debe ser un texto."
            )

        correo_limpio = valor.strip()

        # No permite espacios ni espacios al inicio o al final.
        if correo_limpio != valor or " " in correo_limpio:
            raise Cliente_Invalido_Error(
                "El correo electrónico no debe contener espacios."
            )

        # Debe contener exactamente un símbolo @.
        if correo_limpio.count("@") != 1:
            raise Cliente_Invalido_Error(
                "El correo electrónico debe contener un solo símbolo @."
            )

        parte_local, dominio = correo_limpio.split("@")

        # Comprueba que existan datos antes y después del @.
        if not parte_local or not dominio:
            raise Cliente_Invalido_Error(
                "El correo electrónico debe tener usuario y dominio."
            )

        # Comprueba que el dominio tenga un punto y una extensión válida.
        if (
            "." not in dominio
            or dominio.startswith(".")
            or dominio.endswith(".")
            or ".." in dominio
        ):
            raise Cliente_Invalido_Error(
                "El dominio del correo electrónico no es válido."
            )

        # Evita puntos consecutivos o al inicio y final del usuario.
        if (
            parte_local.startswith(".")
            or parte_local.endswith(".")
            or ".." in parte_local
        ):
            raise Cliente_Invalido_Error(
                "El usuario del correo electrónico no es válido."
            )

        self.__correo = correo_limpio

    # ====================== Validación Teléfono ======================

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):

        # Se conserva la validación original de mínimo 7 dígitos.
        telefono_limpio = str(valor)

        if not telefono_limpio.isdigit() or len(telefono_limpio) < 7:
            raise Cliente_Invalido_Error(
                "El teléfono debe contener mínimo 7 dígitos numéricos."
            )

        self.__telefono = telefono_limpio

    # ====================== Mostrar Información ======================

    def mostrar_informacion(self):

        return (
            f"ID cliente: {self.id_cliente} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo} | "
            f"Teléfono: {self.telefono}"
        )

    def __str__(self):
        return self.mostrar_informacion()


# ====================== Pruebas Unitarias ======================

if __name__ == "__main__":

    print("=== INICIANDO PRUEBAS DE LA CLASE CLIENTE ===")

    # Prueba 1: Cliente válido
    try:
        cliente1 = Cliente(
            "A001",
            "Alfonso Morales",
            "alfonso@gmail.com",
            "3132223344"
        )

        print("\nPrueba 1: Cliente válido")
        print(cliente1.mostrar_informacion())

    except Cliente_Invalido_Error as error:
        print("Error:", error)

    # Prueba 2: Nombre demasiado corto
    try:
        cliente2 = Cliente(
            "A002",
            "Al",
            "alfonso@gmail.com",
            "3132223344"
        )

    except Cliente_Invalido_Error as error:
        print("\nPrueba 2: Nombre inválido detectado correctamente")
        print(error)

    # Prueba 3: Correo sin símbolo @
    try:
        cliente3 = Cliente(
            "A003",
            "Carlos Morales",
            "correoinvalido.com",
            "3132223344"
        )

    except Cliente_Invalido_Error as error:
        print("\nPrueba 3: Correo inválido detectado correctamente")
        print(error)

    # Prueba 4: Teléfono demasiado corto
    try:
        cliente4 = Cliente(
            "A004",
            "Pedro Morales",
            "pedro@gmail.com",
            "12345"
        )

    except Cliente_Invalido_Error as error:
        print("\nPrueba 4: Teléfono inválido detectado correctamente")
        print(error)

    # Prueba 5: ID vacío
    try:
        cliente5 = Cliente(
            "",
            "Andres Morales",
            "andres@gmail.com",
            "3132223344"
        )

    except Cliente_Invalido_Error as error:
        print("\nPrueba 5: ID vacío detectado correctamente")
        print(error)

    # Prueba 6: ID None
    try:
        cliente6 = Cliente(
            None,
            "Andres Morales",
            "andres@gmail.com",
            "3132223344"
        )

    except Cliente_Invalido_Error as error:
        print("\nPrueba 6: ID None detectado correctamente")
        print(error)

    # Prueba 7: Correo con dos símbolos @
    try:
        cliente7 = Cliente(
            "A007",
            "Carlos Morales",
            "carlos@@gmail.com",
            "3132223344"
        )

    except Cliente_Invalido_Error as error:
        print("\nPrueba 7: Correo con dos @ detectado correctamente")
        print(error)

    # Prueba 8: Correo sin dominio válido
    try:
        cliente8 = Cliente(
            "A008",
            "Carlos Morales",
            "carlos@.com",
            "3132223344"
        )

    except Cliente_Invalido_Error as error:
        print("\nPrueba 8: Dominio inválido detectado correctamente")
        print(error)

    print("\n=== TODAS LAS VERIFICACIONES COMPLETADAS ===")
