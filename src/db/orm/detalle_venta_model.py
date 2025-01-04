from .base_model import BaseModel

class DetalleVentaModel(BaseModel):
    def __init__(self, db_path):
        super().__init__(db_path)

    def create_detalle_venta(self, id_venta, id_producto, cantidad, precio_unitario):
        query = """
        INSERT INTO DETALLE_VENTA (id_venta, id_producto, cantidad, precio_unitario)
        VALUES (?, ?, ?, ?)
        """
        self.execute_query(query, (id_venta, id_producto, cantidad, precio_unitario))

    def get_detalle_venta(self, venta_id):
        query = "SELECT * FROM DETALLE_VENTA WHERE id_venta = ?"
        return self.fetch_all(query, (venta_id,))
