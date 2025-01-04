from .base_model import BaseModel

class ProductoModel(BaseModel):
    def __init__(self, db_path):
        super().__init__(db_path)

    def create_producto(self, nombre, categoria, descripcion, modelo, precio_al_por_menor, stock, detalles_tecnicos):
        query = """
        INSERT INTO PRODUCTO (nombre, categoria, descripcion, modelo, precio_al_por_menor, stock, detalles_tecnicos)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        self.execute_query(query, (nombre, categoria, descripcion, modelo, precio_al_por_menor, stock, detalles_tecnicos))

    def get_productos(self):
        query = "SELECT * FROM PRODUCTO"
        return self.fetch_all(query)

    def update_producto(self, producto_id, nombre, categoria, descripcion, modelo, precio_al_por_menor, stock, detalles_tecnicos):
        query = """
        UPDATE PRODUCTO
        SET nombre = ?, categoria = ?, descripcion = ?, modelo = ?, precio_al_por_menor = ?, stock = ?, detalles_tecnicos = ?
        WHERE id = ?
        """
        self.execute_query(query, (nombre, categoria, descripcion, modelo, precio_al_por_menor, stock, detalles_tecnicos, producto_id))

    def delete_producto(self, producto_id):
        query = "DELETE FROM PRODUCTO WHERE id = ?"
        self.execute_query(query, (producto_id,))
