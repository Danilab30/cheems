import mysql.connector
from mysql.connector import Error

def get_db_connection():
    return mysql.connector.connect(
        host='162.241.2.39',
        user='itsonapp_244442',
        password='244442db#531R',
        database='itsonapp_244442'
    )
