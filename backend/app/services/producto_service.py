# app/services/producto_service.py
from app.DAO.producto_DAO import ProductoDAO

class ProductoService:
    
    def __init__(self):
        self.producto_dao = ProductoDAO()

    def create_producto():
        pass

    def update_cantidad(self, producto_id: int, tipo: str, cantidad: int):
        producto = self.producto_dao.get_producto(producto_id)
        if not producto:
            raise ValueError("Producto no encontrado")

        if tipo == "salida" and producto["stock_actual"] < cantidad:
            raise ValueError("Stock insuficiente")

        nuevo_stock = producto["stock_actual"] + cantidad if tipo == "entrada" else producto["stock_actual"] - cantidad
        self.producto_dao.update_stock(producto_id, nuevo_stock)

    def read_producto():
        pass
    
    def delete_producto():
        pass