# ====================== EXCEPCIONES PERSONALIZADAS ======================

class Error_SoftwareFJ(Exception):
    """Excepción base del sistema Software FJ."""


class Cliente_Invalido_Error(Error_SoftwareFJ):
    """Se produce cuando los datos de un cliente no son válidos."""


class Servicio_NoDisponible_Error(Error_SoftwareFJ):
    """Se produce cuando un servicio tiene datos u operaciones inválidas."""


class Reserva_Invalida_Error(Error_SoftwareFJ):
    """Se produce cuando una reserva no puede procesarse."""
