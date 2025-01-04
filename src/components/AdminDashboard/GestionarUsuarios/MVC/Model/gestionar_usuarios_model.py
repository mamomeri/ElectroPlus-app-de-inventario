from db.orm.trabajador_model import TrabajadorModel
from utils.config import DATABASE_PATH

class GestionarUsuariosModel:
    def __init__(self):
        self.trabajador_model = TrabajadorModel(DATABASE_PATH)

    def fetch_users(self):
        """Obtiene todos los trabajadores usando el ORM."""
        return self.trabajador_model.get_trabajadores()

    def add_user(self, nombre, tipo, contraseña):
        """Agrega un nuevo trabajador."""
        self.trabajador_model.create_trabajador(nombre, tipo, contraseña)

    def update_user(self, user_id, nombre, tipo, contraseña):
        """Actualiza un trabajador existente."""
        self.trabajador_model.update_trabajador(user_id, nombre, tipo, contraseña)

    def delete_user(self, user_id):
        """Elimina un trabajador."""
        self.trabajador_model.delete_trabajador(user_id)
