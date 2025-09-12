from app.db.conexionDB import ConectDB

class ProductoModel:
    def __init__(self, id_producto=None, nombre=None, descripcion=None, precio=None, id_categoria=None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.id_categoria = id_categoria

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "id_categoria": self.id_categoria
        }

    # CREATE
    def create(self):
        connection = ConectDB.get_connection()
        try:
            with connection.cursor() as cursor:
                query = """
                    INSERT INTO producto (nombre, descripcion, precio, id_categoria)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (self.nombre, self.descripcion, self.precio, self.id_categoria))
                connection.commit()
                self.id_producto = cursor.lastrowid
                return self
        except Exception as e:
            print(f"Error al crear producto: {e}")
            return None
        finally:
            connection.close()

    # READ ONE
    @staticmethod
    def read(id_producto):
        connection = ConectDB.get_connection()
        try:
            with connection.cursor() as cursor:
                query = "SELECT id_producto, nombre, descripcion, precio, id_categoria FROM producto WHERE id_producto = %s"
                cursor.execute(query, (id_producto,))
                result = cursor.fetchone()
                if result:
                    return ProductoModel(*result)
                return None
        except Exception as e:
            print(f"Error al leer producto: {e}")
            return None
        finally:
            connection.close()

    # READ ALL
    @staticmethod
    def read_all():
        connection = ConectDB.get_connection()
        try:
            with connection.cursor() as cursor:
                query = "SELECT id_producto, nombre, descripcion, precio, id_categoria FROM producto"
                cursor.execute(query)
                results = cursor.fetchall()
                return [ProductoModel(*row) for row in results]
        except Exception as e:
            print(f"Error al leer productos: {e}")
            return []
        finally:
            connection.close()

    # UPDATE
    def update(self):
        connection = ConectDB.get_connection()
        try:
            with connection.cursor() as cursor:
                query = """
                    UPDATE producto
                    SET nombre=%s, descripcion=%s, precio=%s, id_categoria=%s
                    WHERE id_producto=%s
                """
                cursor.execute(query, (self.nombre, self.descripcion, self.precio, self.id_categoria, self.id_producto))
                connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar producto: {e}")
            return False
        finally:
            connection.close()

    # DELETE
    @staticmethod
    def delete(id_producto):
        connection = ConectDB.get_connection()
        try:
            with connection.cursor() as cursor:
                query = "DELETE FROM producto WHERE id_producto = %s"
                cursor.execute(query, (id_producto,))
                connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar producto: {e}")
            return False
        finally:
            connection.close()
