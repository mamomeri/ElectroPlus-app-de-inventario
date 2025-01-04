from .base_model import BaseModel

class ClienteModel(BaseModel):
    def __init__(self, db_path):
        super().__init__(db_path)

    def create_cliente(self, nombre, contacto, direccion):
        query = "INSERT INTO CLIENTE (nombre, contacto, direccion) VALUES (?, ?, ?)"
        self.execute_query(query, (nombre, contacto, direccion))

    def get_clientes(self):
        query = "SELECT * FROM CLIENTE"
        return self.fetch_all(query)

    def update_cliente(self, cliente_id, nombre, contacto, direccion):
        query = "UPDATE CLIENTE SET nombre = ?, contacto = ?, direccion = ? WHERE id = ?"
        self.execute_query(query, (nombre, contacto, direccion, cliente_id))

    def delete_cliente(self, cliente_id):
        query = "DELETE FROM CLIENTE WHERE id = ?"
        self.execute_query(query, (cliente_id,))
