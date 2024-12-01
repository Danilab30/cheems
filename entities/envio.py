from persistence.db import get_db_connection
from mysql.connector import Error

class Envio:
    def __init__(self, nombre, codigo):
        self.nombre = nombre 
        self.codigo = codigo
    
    @classmethod
    def get_all(cls):
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM ciudad')
            return cursor.fetchall()
        except Error as e:
            return str(e)
        finally:
            cursor.close()
            connection.close() 
            