import sqlite3
from sqlite3 import Error


def create_table(connection_path):
    """Create table in SQlite Database"""
    try:
        conn.execute("""CREATE TABLE mytable
                 (start, end, score)""")
    except:
        pass

def insert():
    try:
        conn.execute("""INSERT INTO mytable (start, end, score)
                      values(1, 99, 123)""")
    except:
        pass

def select(verbose=True):
    sql = "SELECT * FROM mytable"
    recs = conn.execute(sql)
    if verbose:
        for row in recs:
            print
            row

if __name__ == '__main__':
    connection_path = "/home/manshi/docker-workspace/working-codehub-prod/codehub-dockerspawner-nbgrader/sqlite/sqlite.db"
    conn = sqlite3.connect(connection_path)
    create_table(connection_path)
    insert()
    conn.commit() ## commit needed
    select()
    conn.close()