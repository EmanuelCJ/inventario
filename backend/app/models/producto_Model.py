from backend.app.db.conexion_DB import get_connection         

class productoModel:
    def __init__(self, id_producto: int, nombre: str, descripcion: str, cantidad: int, id_categoria: int = None, id_movimiento: int = None):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__cantidad = cantidad
        #atributos de la relacion
        self.__id_categoria = id_categoria
        self.__id_movimiento = id_movimiento


    # Getters and Setters
    def get_id_producto(self) -> int:
        return self.__id_producto
        
    def get_nombre(self) -> str:
        return self.__nombre
    
    def set_nombre(self, nombre: str):
        #validar que sea admin para modificar
        self.__nombre = nombre
        
    def get_descripcion(self) -> str:
        return self.__descripcion
    
    def set_descripcion(self, descripcion: str):
        #validar que sea admin para modificar
        self.__descripcion = descripcion
        
    def get_cantidad(self) -> int:
        return self.__cantidad
    
    def set_cantidad(self, cantidad: int):
        #validar que sea admin para modificar
        self.__cantidad = cantidad
        
    def get_id_categoria(self) -> int:
        return self.__id_categoria
    
    def set_id_categoria(self, id_categoria: int):
        #validar que sea admin para modificar
        self.__id_categoria = id_categoria
        
    def get_id_movimiento(self) -> int:
        return self.__id_movimiento
    
    
    def serializar(self) -> dict:
        return {
            "id_producto": self.get_id_producto(),
            "nombre": self.get_nombre(),
            "descripcion": self.get_descripcion(),
            "cantidad": self.get_cantidad(),
            "id_categoria": self.get_id_categoria(),
            "id_movimiento": self.get_id_movimiento()
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
        
    @staticmethod
    def create(self, data):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "INSERT INTO productos (nombre, descripcion, stock) VALUES (%s, %s, %s)"
            cursor.execute(query, (data["nombre"], data["descripcion"], data["stock"]))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Error al crear producto: {e}")
        return False
        
    @staticmethod
    def read(self, producto_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM productos WHERE id=%s"
        cursor.execute(query, (producto_id,))
        producto = cursor.fetchone()
        cursor.close()
        conn.close()
        return producto
    
    @staticmethod
    def update(self, producto_id, data):
        conn = get_connection()
        cursor = conn.cursor()
        query = "UPDATE productos SET stock=%s WHERE id=%s"
        cursor.execute(query, (data["stock"], producto_id))
        conn.commit()
        cursor.close()
        conn.close()
        
    @staticmethod
    def delete(self, producto_id):
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM productos WHERE id=%s"
        cursor.execute(query, (producto_id,))
        conn.commit()
        cursor.close()
        conn.close()
    