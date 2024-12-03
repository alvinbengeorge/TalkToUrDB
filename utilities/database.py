from typing import Optional
from mysql.connector import MySQLConnection, Error

import mysql.connector

def connect_to_mysql(host: str, user: str, password: str, database: str) -> Optional[MySQLConnection]:
    connection: Optional[MySQLConnection] = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print("Successfully connected to the database")
    except Error as e:
        print(f"Error: '{e}'")
    return connection

def execute_query(connection: MySQLConnection, query) -> Optional[list]:
    """ Execute a single query """
    cursor = connection.cursor()
    cursor.execute(query)
    return {
        "output": cursor.fetchall(),
        "columns": cursor.column_names,
        "command": query        
    }

def commit(connection: MySQLConnection):
    connection.commit()
    
def rollback(connection: MySQLConnection):
    connection.rollback()

if __name__ == "__main__":
    connection = connect_to_mysql(host="localhost", user="root", password="alvin", database="test")
    print(execute_query(connection, "SHOW TABLES"))