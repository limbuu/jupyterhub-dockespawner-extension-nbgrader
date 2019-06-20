import mysql.connector
connection = mysql.connector.connect(user='root', password='123',
                              host='127.0.0.1',
                              database='jupyterhub_test')

try:
   cursor = connection.cursor()
   cursor.execute("CREATE TABLE teacher (id INT, name VARCHAR(255))")
   # Get database table'
   cursor.execute("SHOW TABLES")
   for table in cursor:
       print(table)
finally:
    connection.close()