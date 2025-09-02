from mysql.connector import connect, Error
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        connection = connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return connection
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None