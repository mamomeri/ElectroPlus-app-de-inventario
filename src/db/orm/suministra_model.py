from .base_model import BaseModel

class SuministraModel(BaseModel):
    def __init__(self, db_path):
        super().__init__(db_path)

    def create_suministro(self, id_proveedor, id_producto, cantidad, fecha, precio_al_por_mayor):
        query = """
        INSERT INTO SUMINISTRA (id_proveedor, id_producto, cantidad, fecha, precio_al_por_mayor)
        VALUES (?, ?, ?, ?, ?)
        """
        self.execute_query(query, (id_proveedor, id_producto, cantidad, fecha, precio_al_por_mayor))

    def get_suministros(self):
        query = "SELECT * FROM SUMINISTRA"
        return self.fetch_all(query)

    def update_suministro(self, suministro_id, id_proveedor, id_producto, cantidad, fecha, precio_al_por_mayor):
        query = """
        UPDATE SUMINISTRA
        SET id_proveedor = ?, id_producto = ?, cantidad = ?, fecha = ?, precio_al_por_mayor = ?
        WHERE id = ?
        """
        self.execute_query(query, (id_proveedor, id_producto, cantidad, fecha, precio_al_por_mayor, suministro_id))

    def delete_suministro(self, suministro_id):
        query = "DELETE FROM SUMINISTRA WHERE id = ?"
        self.execute_query(query, (suministro_id,))
