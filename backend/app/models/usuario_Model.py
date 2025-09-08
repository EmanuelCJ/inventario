from app.db.conexionDB import get_connection

class UsuarioModel:
    __id_usuario: int
    __nombre: str
    __apellido: str
    __rol: str
    __contrasena: str

    def __init__(self, id_usuario: int, nombre: str, apellido: str, rol: str, contrasena: str):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__rol = rol
        self.__contrasena = contrasena

    def registrar_movimiento(tipo, cantidad, id_producto, id_usuario, id_lugar):
        conn = get_connection()
        cursor = conn.cursor()

        # 1) Insertar movimiento
        sql_mov = """
            INSERT INTO movimientos (tipo, fecha, cantidad, id_usuario)
            VALUES (%s, NOW(), %s, %s)
        """
        cursor.execute(sql_mov, (tipo, cantidad, id_usuario))
        id_movimiento = cursor.lastrowid

        # 2) Relacionar movimiento con producto
        sql_prod_mov = """
            UPDATE productos
            SET id_movimiento = %s
            WHERE id_producto = %s
        """
        cursor.execute(sql_prod_mov, (id_movimiento, id_producto))

        # 3) Actualizar stock en el lugar (producto_lugar)
        # si ya existe la fila, sumo cantidad; si no, la creo
        sql_check = """
        SELECT cantidad FROM producto_lugar
        WHERE id_producto = %s AND id_lugar = %s
        """
        cursor.execute(sql_check, (id_producto, id_lugar))
        row = cursor.fetchone()

        if row:
            # existe, actualizo
            nueva_cantidad = row[0] + cantidad if tipo == "entrada" else row[0] - cantidad
            sql_update = """
                UPDATE producto_lugar
                SET cantidad = %s
                WHERE id_producto = %s AND id_lugar = %s
                """
            cursor.execute(sql_update, (nueva_cantidad, id_producto, id_lugar))
        else:
            # no existe, inserto (solo si es entrada)
            if tipo == "entrada":
                sql_insert = """
                    INSERT INTO producto_lugar (id_producto, id_lugar, cantidad)
                    VALUES (%s, %s, %s)
                """
                cursor.execute(sql_insert, (id_producto, id_lugar, cantidad))

        conn.commit()
        cursor.close()
        conn.close()
        return id_movimiento