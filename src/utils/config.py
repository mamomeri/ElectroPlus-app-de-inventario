
# src/utils/config.py

import os

# Obtén la ruta absoluta del directorio base del proyecto
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Configura la ruta absoluta para la base de datos
DATABASE_PATH = os.path.join(BASE_DIR, "db", "Data", "ElectroPlusDB.db")

# Configura la ruta absoluta para los logs
LOG_FILE_PATH = os.path.join(BASE_DIR, "utils", "logs", "app.log")
