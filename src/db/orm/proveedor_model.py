from .base_model import BaseModel

class ProveedorModel(BaseModel):
    def __init__(self, db_path):
        super().__init__(db_path)

    def create_proveedor(self, nombre, contacto):
        query = "INSERT INTO PROVEEDOR (nombre, contacto) VALUES (?, ?)"
        self.execute_query(query, (nombre, contacto))

    def get_proveedores(self):
        query = "SELECT * FROM PROVEEDOR"
        return self.fetch_all(query)

    def update_proveedor(self, proveedor_id, nombre, contacto):
        query = "UPDATE PROVEEDOR SET nombre = ?, contacto = ? WHERE id = ?"
        self.execute_query(query, (nombre, contacto, proveedor_id))

    def delete_proveedor(self, proveedor_id):
        query = "DELETE FROM PROVEEDOR WHERE id = ?"
        self.execute_query(query, (proveedor_id,))
