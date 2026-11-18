import logging
import os

# ====================== Configuración del archivo Logs ======================

def archivo_Logs():
    nombre_carpeta = "Logs"
    nombre_archivo = "errores y eventos_Softwrae_FJ_log.txt"
    ruta_archivo = os.path.join(nombre_carpeta, nombre_archivo)

    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)

    if not logging.getLogger().hasHandlers():
        logging.basicConfig(
            filename=ruta_archivo,
            level=logging.INFO,
            format="[%(asctime)s] [%(levelname)s]: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            encoding="utf-8"
        )
        
    logging.info("------------ Sistema de logs iniciado -------------")
