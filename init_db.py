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

TABLES['usuarios'] = {
    "CREATE TABLE `usuarios`("
    "`id` int(11) NOT NULL AUTO_INCREMENT,"
    "`nombre` varchar(50) NOT NULL,"
    "`apellido` varchar(50) NOT NULL,"
    "`user_name` varchar(50) NOT NULL,"
    "`rol` ENUM(`admin`,`editor`,`visor`) DEFAULT visor,"
    "PRIMARY KEY (`id`)"
    ") "
}
TABLES['movimientos'] = {
    "`id_movimientos` int(11) NOT NULL AUTO_INCREMENT,"
    "`tipo` ENUM(`create`,`update`,`delete`,`read`,`salida`,`entrada`),"
    "`fecha` DATETIME "
}