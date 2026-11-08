
import logging

# ====================== Configuración de Logs ======================

def archivo_Logs():
    logging.basicConfig(
        filename="errores y eventos_Softwrae_FJ_log.txt",
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
        encoding="utf-8"
    )

    logging.info("Sistema de logs iniciado.")
