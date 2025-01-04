import logging
import os

# Crear una función para configurar el logger
def get_logger(name):
    # Asegúrate de que la carpeta de logs exista
    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)
    
    # Ruta del archivo de log
    log_file = os.path.join(log_dir, "app.log")
    
    # Configurar logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Nivel del log
    
    # Formato del log
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger
