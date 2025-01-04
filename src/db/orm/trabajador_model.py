from .base_model import BaseModel

class TrabajadorModel(BaseModel):
    def __init__(self, db_path):
        super().__init__(db_path)

    def create_trabajador(self, nombre, tipo, contraseña):
        query = "INSERT INTO TRABAJADOR (nombre, tipo, contraseña) VALUES (?, ?, ?)"
        self.execute_query(query, (nombre, tipo, contraseña))

    def get_trabajadores(self):
        query = "SELECT * FROM TRABAJADOR"
        return self.fetch_all(query)

    def update_trabajador(self, trabajador_id, nombre, tipo, contraseña):
        query = "UPDATE TRABAJADOR SET nombre = ?, tipo = ?, contraseña = ? WHERE id = ?"
        self.execute_query(query, (nombre, tipo, contraseña, trabajador_id))

    def delete_trabajador(self, trabajador_id):
        query = "DELETE FROM TRABAJADOR WHERE id = ?"
        self.execute_query(query, (trabajador_id,))
        
    def verify_trabajador(self, nombre, contraseña):
        """
        Verifica si existe un trabajador con las credenciales dadas.
        """
        query = "SELECT * FROM TRABAJADOR WHERE nombre = ? AND contraseña = ?"
        return self.fetch_one(query, (nombre, contraseña))
    

