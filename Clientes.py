from Clase_Base import Entidad_Base
from Excepciones import Cliente_Invalido_Error


class Cliente(Entidad_Base):
    """
    Clase que representa a un cliente dentro del sistema Software FJ.
    Aplica encapsulación rigurosa y validaciones con Cliente_Invalido_Error.
    """

    def __init__(self, id_cliente, nombre, correo, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def id_cliente(self):
        return self.__id_cliente

    @id_cliente.setter
    def id_cliente(self, valor):
        if not str(valor).strip():
            raise Cliente_Invalido_Error("El ID del cliente no puede estar vacío.")
        self.__id_cliente = str(valor).strip()

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise Cliente_Invalido_Error("El nombre del cliente debe ser un texto no vacío.")
        if len(valor.strip()) < 3:
            raise Cliente_Invalido_Error("El nombre del cliente debe tener al menos 3 caracteres.")
        self.__nombre = valor.strip()

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or "@" not in valor or "." not in valor:
            raise Cliente_Invalido_Error(f"El correo electrónico '{valor}' no tiene un formato válido.")
        self.__correo = valor.strip()

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        valor_str = str(valor).strip()
        if not valor_str.isdigit() or len(valor_str) < 7:
            raise Cliente_Invalido_Error("El teléfono debe contener únicamente números y al menos 7 dígitos.")
        self.__telefono = valor_str

    def mostrar_informacion(self):
        """
        Implementación del método abstracto de Entidad_Base.
        """
        return (
            f"--- Información del Cliente ---\n"
            f"ID: {self.__id_cliente}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"
        )

    def __str__(self):
        return f"Cliente({self.__id_cliente} - {self.__nombre})"


# ============================================================
# BLOQUE DE VERIFICACIÓN LOCAL
# ============================================================
if __name__ == "__main__":
    print("=== INICIANDO PRUEBAS DE LA CLASE CLIENTE ===\n")

    # Caso 1: Válido
    try:
        c1 = Cliente("1001", "Alfonso Morales", "alfonso@email.com", "3101234567")
        print("Caso 1 (Éxito):")
        print(c1.mostrar_informacion())
        print("\n" + "=" * 45 + "\n")
    except Cliente_Invalido_Error as e:
        print(f"Error inesperado: {e}")

    # Caso 2: Nombre corto
    try:
        print("Caso 2 (Debe fallar por nombre corto):")
        c2 = Cliente("1002", "Al", "cliente@email.com", "3101234567")
    except Cliente_Invalido_Error as e:
        print(f"Capturado correctamente: {e}\n")

    # Caso 3: Correo sin @
    try:
        print("Caso 3 (Debe fallar por correo sin formato):")
        c3 = Cliente("1003", "Carlos Perez", "correoinvalido.com", "3101234567")
    except Cliente_Invalido_Error as e:
        print(f"Capturado correctamente: {e}\n")

    # Caso 4: Teléfono con letras o corto
    try:
        print("Caso 4 (Debe fallar por teléfono inválido):")
        c4 = Cliente("1004", "Maria Gomez", "maria@email.com", "12345")
    except Cliente_Invalido_Error as e:
        print(f"Capturado correctamente: {e}\n")

    print("=== TODAS LAS VERIFICACIONES COMPLETADAS ===")
