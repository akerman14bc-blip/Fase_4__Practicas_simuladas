
from Excepciones import Cliente_Invalido_Error, Reserva_Invalida_Error, Servicio_NoDisponible_Error

# ====================== Gestión de Listas Internas ======================

class Gestion_Listas:
    def __init__(self):
        self.clientes_registrados = []
        self.servicios_disponibles = []
        self.reservas_realizadas = []

    def registrar_cliente(self, cliente):
        if any(c.nombre == cliente.nombre for c in self.clientes_registrados):
            raise Cliente_Invalido_Error(f"El cliente {cliente.nombre} ya se encuentra registrado.")
        self.clientes_registrados.append(cliente)

    def registrar_servicio(self, servicio):
        if any(c.get_nombre_servicio() == servicio.get_nombre_servicio() for c in self.servicios_disponibles):
            raise Servicio_NoDisponible_Error(f"El servicio {servicio.get_nombre_servicio()} ya se encuentra registrado.")
        self.servicios_disponibles.append(servicio)

    def registrar_reserva(self, reserva):
        if any(c.id_reserva == reserva.id_reserva for c in self.reservas_realizadas):
            raise Reserva_Invalida_Error(f"Ya existe una reserva registrada con el ID {reserva.id_reserva}.")
        self.reservas_realizadas.append(reserva)

    def buscar_cliente(self, id_cliente):
        for cliente in self.clientes_registrados:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None

    def mostrar_resumen_listas(self):
        print(f"\nClientes registrados: {len(self.clientes_registrados)}")
        print(f"Servicios disponibles: {len(self.servicios_disponibles)}")
        print(f"Reservas realizadas: {len(self.reservas_realizadas)}")
