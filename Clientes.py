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
logging.basicConfig(
    filename="sistema_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


class Cliente(Entidad_Base):
    """
    Clase que representa a un cliente dentro de la empresa Software FJ.
    Hereda de Entidad_Base y encapsula estrictamente los datos personales.
    """

    def __init__(self, id_cliente, nombre, correo, telefono):
        # Invocación al constructor de la clase base abstracta
        super().__init__()
        
        # Asignación a través de setters para activar validaciones desde la creación
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

   
    # GESTIÓN Y ENCAPSULACIÓN DEL ATRIBUTO: id_cliente
   
    @property
    def id_cliente(self):
        # Getter: Retorna el identificador privado del cliente
        return self.__id_cliente

    @id_cliente.setter
    def id_cliente(self, valor):
        # Validación: Verifica que el identificador no sea una cadena vacía ni espacios
        if not str(valor).strip():
            raise Cliente_Invalido_Error("El ID del cliente no puede estar vacío.")
        # Se almacena como atributo privado asegurando formato de texto limpio
        self.__id_cliente = str(valor).strip()

    # GESTIÓN Y ENCAPSULACIÓN DEL ATRIBUTO: nombre
   
    @property
    def nombre(self):
        # Getter: Retorna el nombre privado del cliente
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        # Validación de tipo: Verifica que el dato sea texto y no esté vacío
        if not isinstance(valor, str) or not valor.strip():
            raise Cliente_Invalido_Error("El nombre del cliente debe ser un texto no vacío.")
        # Validación de longitud: Exige al menos 3 caracteres alfabéticos
        if len(valor.strip()) < 3:
            raise Cliente_Invalido_Error("El nombre del cliente debe tener al menos 3 caracteres.")
        # Se asigna el valor depurado al atributo privado
        self.__nombre = valor.strip()

    # GESTIÓN Y ENCAPSULACIÓN DEL ATRIBUTO: correo
   
    @property
    def correo(self):
        # Getter: Retorna el correo electrónico privado
        return self.__correo

    @correo.setter
    def correo(self, valor):
        # Validación de formato: Comprueba que contenga '@' y '.' como estructura mínima
        if not isinstance(valor, str) or "@" not in valor or "." not in valor:
            raise Cliente_Invalido_Error(f"El correo electrónico '{valor}' no tiene un formato válido.")
        # Se guarda el correo electrónico sin espacios en los extremos
        self.__correo = valor.strip()

    # GESTIÓN Y ENCAPSULACIÓN DEL ATRIBUTO: telefono
 
    @property
    def telefono(self):
        # Getter: Retorna el número de teléfono privado
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        # Se convierte a cadena para procesar la entrada
        valor_str = str(valor).strip()
        # Validación numérica y de longitud mínima requerida (al menos 7 dígitos)
        if not valor_str.isdigit() or len(valor_str) < 7:
            raise Cliente_Invalido_Error("El teléfono debe contener únicamente números y al menos 7 dígitos.")
        # Se asigna al atributo privado
        self.__telefono = valor_str

  
    # MÉTODOS PÚBLICOS Y SOBRESCRITURA DE MÉTODOS ABSTRACTOS
    
    def mostrar_informacion(self):
        """
        Implementación concreta del método polimórfico heredado de Entidad_Base.
        Formatea y presenta la ficha descriptiva con los datos del cliente.
        """
        return (
            f"--- Información del Cliente ---\n"
            f"ID: {self.__id_cliente}\n"
            f"Nombre: {self.__nombre}\n"
            f"Correo: {self.__correo}\n"
            f"Teléfono: {self.__telefono}"
        )

    def __str__(self):
        # Representación textual legible de la instancia
        return f"Cliente({self.__id_cliente} - {self.__nombre})"

# BLOQUE DE PRUEBAS UNITARIAS Y CONTROL DE EXCEPCIONES

if __name__ == "__main__":
    print("=== INICIANDO PRUEBAS DE LA CLASE CLIENTE ===\n")

    # Caso 1: Instanciación correcta
    print("--- Caso 1: Creación de cliente válido ---")
    try:
        # Se intentan cargar datos que satisfacen todas las reglas de negocio
        c1 = Cliente("1001", "Alfonso Morales", "alfonso@email.com", "3101234567")
    except Cliente_Invalido_Error as e:
        # Se captura cualquier falla imprevista durante la prueba
        print(f"Error inesperado: {e}")
        logging.error(f"Error inesperado en Caso 1: {e}")
    else:
        # Cláusula else: Se ejecuta únicamente si el bloque try fue exitoso
        print("Caso 1 exitoso:")
        print(c1.mostrar_informacion())
        logging.info(f"Cliente registrado con éxito: {c1.id_cliente} - {c1.nombre}")
    finally:
        # Cláusula finally: Se ejecuta incondicionalmente al concluir la prueba
        print("Estado Caso 1: Verificación de ejecución concluida.\n")

    # Caso 2: Manejo de error por nombre menor a 3 caracteres
    print("--- Caso 2: Nombre con menos de 3 caracteres ---")
    try:
        # Se prueba el disparo intencional de la excepción por nombre corto
        c2 = Cliente("1002", "Al", "cliente@email.com", "3101234567")
    except Cliente_Invalido_Error as e:
        # Se reporta la captura exitosa del error y se persiste en el log
        print(f"Excepción capturada correctamente: {e}")
        logging.warning(f"Intento de registro fallido (nombre inválido): {e}")
    else:
        print("Error: El cliente no debió haberse creado.")
    finally:
        print("Estado Caso 2: Verificación de ejecución concluida.\n")

    # Caso 3: Manejo de error por formato de correo electrónico
    print("--- Caso 3: Correo electrónico sin formato ---")
    try:
        # Se prueba el rechazo de direcciones de correo sin estructura estándar
        c3 = Cliente("1003", "Carlos Perez", "correoinvalido.com", "3101234567")
    except Cliente_Invalido_Error as e:
        # Captura y asentamiento en el log
        print(f"Excepción capturada correctamente: {e}")
        logging.warning(f"Intento de registro fallido (correo inválido): {e}")
    else:
        print("Error: El cliente no debió haberse creado.")
    finally:
        print("Estado Caso 3: Verificación de ejecución concluida.\n")

    # Caso 4: Manejo de error por teléfono inválido o insuficiente
    print("--- Caso 4: Teléfono con longitud insuficiente ---")
    try:
        # Se prueba el rechazo de números de teléfono cortos o alfanuméricos
        c4 = Cliente("1004", "Maria Gomez", "maria@email.com", "12345")
    except Cliente_Invalido_Error as e:
        # Captura y asentamiento en el log
        print(f"Excepción capturada correctamente: {e}")
        logging.warning(f"Intento de registro fallido (teléfono inválido): {e}")
    else:
        print("Error: El cliente no debió haberse creado.")
    finally:
        print("Estado Caso 4: Verificación de ejecución concluida.\n")

    print("=== TODAS LAS VERIFICACIONES COMPLETADAS ===")
