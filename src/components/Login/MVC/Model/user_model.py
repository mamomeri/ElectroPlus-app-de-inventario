from db.orm.trabajador_model import TrabajadorModel

class UserModel:
    def __init__(self, db_path):
        self.trabajador_model = TrabajadorModel(db_path)

    def validate_user(self, username, password):
        """
        Valida las credenciales del usuario y retorna el rol si es válido.
        """
        user = self.trabajador_model.verify_trabajador(username, password)
        if user:
            return user[2]  # Retorna el rol del usuario
        return None
