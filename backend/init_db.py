import mysql.connector
from mysql.connector import Error, errorcode

import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")

DB_CONFIG = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'port': os.getenv("DB_PORT"),
    'raise_on_warnings': True,
}

print(DB_CONFIG) # Debugging line to check DB_CONFIG

TABLES = {}
SEEDS = {}
TABLES = {}

TABLES['usuarios'] = (
    "CREATE TABLE `usuarios` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `nombre` varchar(50) NOT NULL,"
    "  `apellido` varchar(50) NOT NULL,"
    "  `user_name` varchar(50) NOT NULL,"
    "  `rol` ENUM('admin','editor','visor') DEFAULT 'visor',"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB"
)

TABLES['movimientos'] = (
    "CREATE TABLE `movimientos` ("
    "  `id_movimientos` int(11) NOT NULL AUTO_INCREMENT,"
    "  `tipo` ENUM('create','update','delete','read','salida','entrada'),"
    "  `fecha_creacion` DATETIME DEFAULT CURRENT_TIMESTAMP,"
    "  `fecha_modificacion` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,"
    "  `cantidad` int(11) NOT NULL,"
    "  `id_usuario` int NOT NULL,"
    "  PRIMARY KEY (`id_movimientos`),"
    "  FOREIGN KEY (`id_usuario`) REFERENCES `usuarios`(`id`)"
    ") ENGINE=InnoDB"
)

TABLES['categoria'] = (
    "CREATE TABLE `categoria` ("
    "  `id_categoria` int(11) NOT NULL AUTO_INCREMENT,"
    "  `nombre` varchar(50) NOT NULL,"
    "  `descripcion` varchar(100) NOT NULL,"
    "  PRIMARY KEY (`id_categoria`)"
    ") ENGINE=InnoDB"
)

TABLES['lugar'] = (
    "CREATE TABLE `lugar` ("
    "  `id_lugar` int(11) NOT NULL AUTO_INCREMENT,"
    "  `nombre` varchar(50) NOT NULL,"
    "  `descripcion` varchar(100) NOT NULL,"
    "  PRIMARY KEY (`id_lugar`)"
    ") ENGINE=InnoDB"
)

TABLES['productos'] = (
    "CREATE TABLE `productos` ("
    "  `id_productos` int(11) NOT NULL AUTO_INCREMENT,"
    "  `nombre` varchar(50) NOT NULL,"
    "  `condicion` ENUM('nuevo','usado'),"
    "  `descripcion` varchar(100) NOT NULL,"
    "  `stock_actual` int(11),"
    "  `id_categoria` int(11),"
    "   `id_movimientos` int(11),"
    "  PRIMARY KEY (`id_productos`),"
    "  FOREIGN KEY (`id_categoria`) REFERENCES `categoria`(`id_categoria`),"
    "  FOREIGN KEY (`id_movimientos`)  REFERENCES `movimientos`(`id_movimientos`)" 
    ") ENGINE=InnoDB"
)
TABLES["productos_lugar"] = (
    "CREATE TABLE `productos_lugar` ("
    "  `id_productos` int(11) NOT NULL,"
    "  `id_lugar` int(11) NOT NULL,"
    "  `cantidad` int(11) NOT NULL,"
    "  PRIMARY KEY (`id_productos`,`id_lugar`),"
    "  FOREIGN KEY (`id_productos`) REFERENCES `productos`(`id_productos`),"
    "  FOREIGN KEY (`id_lugar`) REFERENCES `lugar`(`id_lugar`)"
    ") ENGINE=InnoDB"
)


def create_database(cursor):
    try:
        cursor.execute(
            f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'", )
    except Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database already exists")
        else:
            print(err)
    else:
        print(f"Database {DB_NAME} created successfully.")


def create_tables(tables, cursor):

    for table_name in tables:
        table_description = tables[table_name]
        try:
            print(f"Creating table {table_name}: ", end="")
            cursor.execute(table_description)
        except Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    """
    Esta funcion rellena la base de datos pero todavia no tengo el csv con los datos
    """
# def seeds_tables(seed, cursor):
#     for table_name in seed:
#         seed_description = seed[table_name]
#         try:
#             print(f"Seeding table {table_name}: ", end="")
#             cursor.executemany(seed_description[0], seed_description[1])
#         except Error as err:
#             if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#                 print("already exists.")
#             else:
#                 print(err.msg)
#         else:
#             print("OK")

"""
    crea la base de datos
"""
cxn = mysql.connector.connect(**DB_CONFIG)
cursor = cxn.cursor()
create_database(cursor)
CONF_DB = DB_CONFIG.copy()
CONF_DB['database'] = DB_NAME
cursor.close()
cxn.close()

"""
    crea las tablas
    """
cxn = mysql.connector.connect(**CONF_DB)
cursor = cxn.cursor()
create_tables(TABLES, cursor)
# seeds_tables(SEEDS, cursor) #esta linea llama a cargar los datos
cxn.commit()
cursor.close()
cxn.close()
