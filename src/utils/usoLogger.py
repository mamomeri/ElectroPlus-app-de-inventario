# Importar el logger
# from Utils.logger import get_logger
from logger import get_logger
# Crear un logger para este módulo
logger = get_logger(__name__)

def main():
    logger.info("Inicio del programa.")
    try:
        logger.debug("Realizando una operación.")
        # Simula una operación que puede fallar
        1 / 0
    except ZeroDivisionError:
        logger.error("Error: División por cero.", exc_info=True)
    logger.info("Fin del programa.")

if __name__ == "__main__":
    main()
