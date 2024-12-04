from persistence.db import get_db_connection
from mysql.connector import Error

class Rastreo:
    def __init__(self, locacion, estado, fecha, guia):
        self.locacion = locacion 
        self.estado = estado
        self.fecha = fecha
        self.guia = guia
        
    @classmethod
    def get_all(cls):
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM rastreo')
            #cursor.execute('SELECT * FROM rastreo WHERE guia = %s'), (rastreo.guia)
            return cursor.fetchall()
        except Error as e:
            return str(e)
        finally:
            cursor.close()
            connection.close()