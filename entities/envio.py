from persistence.db import get_db_connection
from mysql.connector import Error

class Envio:
    def __init__(self, id, origen, destino, fecha_envio, remitente, destinatario, guia):
        self.id = id 
        self.origen = origen
        self.destino = destino
        self.fecha_envio = fecha_envio
        self.remitente = remitente
        self.destinatario = destinatario
        self.guia = guia
    
    @classmethod
    def get_all(cls):
        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM envio')
            return cursor.fetchall()
        except Error as e:
            return str(e)
        finally:
            cursor.close()
            connection.close() 
            
    @classmethod
    def save(cls, envio):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute('INSERT INTO envio(origen, destino, fecha_envio, remitente, destinatario, guia) VALUES (%s, %s, %s, %s, %s, %s)', (envio.origen, envio.destino, envio.fecha_envio, envio.remitente, envio.destinatario, envio.guia))
            connection.commit()
            return cursor.lastrowid
        except Error as e:
            return str(e)
        finally:
            cursor.close()
            connection.close()  
            
    @classmethod
    def update(cls, id, envio):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute('UPDATE envio SET origen = %s, destino = %s, fecha_envio = %s, remitente = %s, destinatario = %s, guia = %s WHERE id = %s',
                           (envio.origen, envio.destino, envio.fecha_envio, envio.remitente, envio.destinatario, envio.guia, id))
            connection.commit()
            return cursor.rowcount
        except Error as e:
            return str(e)
        finally:
            cursor.close()
            connection.close()
            