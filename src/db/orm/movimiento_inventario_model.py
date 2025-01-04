from .base_model import BaseModel

class MovimientoInventarioModel(BaseModel):
    def __init__(self, db_path):
        super().__init__(db_path)

    def create_movimiento(self, id_producto, id_trabajador, cantidad, fecha):
        query = """
        INSERT INTO MOVIMIENTO_INVENTARIO (id_producto, id_trabajador, cantidad, fecha)
        VALUES (?, ?, ?, ?)
        """
        self.execute_query(query, (id_producto, id_trabajador, cantidad, fecha))

    def get_movimientos(self):
        query = "SELECT * FROM MOVIMIENTO_INVENTARIO"
        return self.fetch_all(query)

    def update_movimiento(self, movimiento_id, id_producto, id_trabajador, cantidad, fecha):
        query = """
        UPDATE MOVIMIENTO_INVENTARIO
        SET id_producto = ?, id_trabajador = ?, cantidad = ?, fecha = ?
        WHERE id = ?
        """
        self.execute_query(query, (id_producto, id_trabajador, cantidad, fecha, movimiento_id))

    def delete_movimiento(self, movimiento_id):
        query = "DELETE FROM MOVIMIENTO_INVENTARIO WHERE id = ?"
        self.execute_query(query, (movimiento_id,))
