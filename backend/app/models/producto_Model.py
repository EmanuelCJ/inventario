from db.conexionDB import get_connection         

class productoModel:
    def __init__(self, id_producto: int, nombre: str, descripcion: str, precio: float, cantidad: int, id_categoria: int = None, id_movimiento: int = None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad
        #atributos de la relacion
        self.id_categoria = id_categoria
        self.id_movimiento = id_movimiento

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

    #crear un nuevo producto nuevo
    def create_producto(self):
        connection = get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO producto (nombre, descripcion, precio, cantidad, id_categoria) VALUES (%s, %s, %s, %s, %s)"
        values = (self.nombre, self.descripcion, self.precio, self.cantidad, self.id_categoria)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
        return cursor.lastrowid

    @staticmethod
    def get_all_productos():
        connection = get_connection()
        
        #diccionario para obtener los nombres de las columnas
        with connection.cursor(dictionary=True) as cursor:
            try:
                #ejecutar la consulta SQL para obtener todos los productos
                cursor.execute("SELECT * FROM producto")
                
                #guardar los resultados en una variable
                rows = cursor.fetchall()

                #lista para almacenar los productos
                productos = []
                for row in rows:
                    productos.append(row)
                    
                return productos
            except Exception as e:
                print(f"Error al ejecutar la consulta: {e}")
                return []