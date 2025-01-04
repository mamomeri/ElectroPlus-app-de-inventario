from .base_model import BaseModel

class VentaModel(BaseModel):
    def __init__(self, db_path):
        super().__init__(db_path)

    def create_venta(self, id_cliente, id_trabajador, fecha, metodo_pago, observaciones):
        query = """
        INSERT INTO VENTA (id_cliente, id_trabajador, fecha, metodo_pago, observaciones)
        VALUES (?, ?, ?, ?, ?)
        """
        self.execute_query(query, (id_cliente, id_trabajador, fecha, metodo_pago, observaciones))

    def get_ventas(self):
        query = "SELECT * FROM VENTA"
        return self.fetch_all(query)

    def update_venta(self, venta_id, id_cliente, id_trabajador, fecha, metodo_pago, observaciones):
        query = """
        UPDATE VENTA
        SET id_cliente = ?, id_trabajador = ?, fecha = ?, metodo_pago = ?, observaciones = ?
        WHERE id = ?
        """
        self.execute_query(query, (id_cliente, id_trabajador, fecha, metodo_pago, observaciones, venta_id))

    def delete_venta(self, venta_id):
        query = "DELETE FROM VENTA WHERE id = ?"
        self.execute_query(query, (venta_id,))
