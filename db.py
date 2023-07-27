import mysql.connector
from mysql.connector import Error

try:
    db_conn = mysql.connector.connect(
        host = 'localhost',
        password = '',
        user = 'root'
    )
    cursor = db_conn.cursor()
    if(db_conn.is_connected):
        cursor.execute("SHOW DATABASES")
        db_info = db_conn.get_server_info()
        for db in cursor:
           print(db)
        print("connected", db_info)
except Error as e:
    print(e)