from db.conexionDB import get_connection         

class productoModel:
    def __init__(self, id_producto: int, nombre: str, descripcion: str, precio: float, cantidad: int, id_categoria: int = None, id_movimiento: int = None):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__cantidad = cantidad
        #atributos de la relacion
        self.__id_categoria = id_categoria
        self.__id_movimiento = id_movimiento

    def serializar(self) -> dict:
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "id_categoria": self.id_categoria,
            "id_movimiento": self.id_movimiento
        }
    
    def deserializar(self, data: dict):
        return data(
            id_producto = data.get("id_producto"),
            nombre = data.get("nombre"),
            descripcion = data.get("descripcion"),
            precio = data.get("precio"),
            cantidad = data.get("cantidad"),
            id_categoria = data.get("id_categoria"),
            id_movimiento = data.get("id_movimiento")
        )
    
    def create(self, data):
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO productos (nombre, descripcion, stock) VALUES (%s, %s, %s)"
        cursor.execute(query, (data["nombre"], data["descripcion"], data["stock"]))
        conn.commit()
        cursor.close()
        conn.close()
    
    def read(self, producto_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM productos WHERE id=%s"
        cursor.execute(query, (producto_id,))
        producto = cursor.fetchone()
        cursor.close()
        conn.close()
        return producto
    
    def update(self, producto_id, data):
        conn = get_connection()
        cursor = conn.cursor()
        query = "UPDATE productos SET stock=%s WHERE id=%s"
        cursor.execute(query, (data["stock"], producto_id))
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self, producto_id):
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM productos WHERE id=%s"
        cursor.execute(query, (producto_id,))
        conn.commit()
        cursor.close()
        conn.close()
    