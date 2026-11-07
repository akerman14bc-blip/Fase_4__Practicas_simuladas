# ====================== EXCEPCIONES PERSONALIZADAS ======================

class Error_SoftwareFJ(Exception):   # Excepción base del sistema Software FJ.
    pass

class Cliente_Invalido_Error(Error_SoftwareFJ):  # Se produce cuando los datos de un cliente no son válidos.
    pass

class Servicio_NoDisponible_Error(Error_SoftwareFJ):  # Se produce cuando un servicio tiene datos u operaciones inválidas.
    pass

class Reserva_Invalida_Error(Error_SoftwareFJ):  # Se produce cuando una reserva no puede procesarse.
    pass
