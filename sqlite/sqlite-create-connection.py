import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()
 
if __name__ == '__main__':
    connection_path = "/home/manshi/docker-workspace/working-codehub-prod/codehub-dockerspawner-nbgrader/sqlite/sqlite.db"
    create_connection(connection_path)
