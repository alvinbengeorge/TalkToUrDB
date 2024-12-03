from typing import Optional
from mysql.connector import MySQLConnection, Error

import mysql.connector

def connect_to_mysql(host: str, user: str, password: str) -> Optional[MySQLConnection]:
    connection: Optional[MySQLConnection] = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        if connection.is_connected():
            print("Successfully connected to the database")
    except Error as e:
        print(f"Error: '{e}'")
    return connection

def execute_query(connection: MySQLConnection, query) -> Optional[list]:
    """ Execute a single query """
    cursor = connection.cursor()
    cursor.execute(query, multi=True)
    return {
        "output": cursor.fetchall(),
        "columns": cursor.column_names,
        "command": query        
    }

def commit(connection: MySQLConnection):
    connection.commit()
    
def rollback(connection: MySQLConnection):
    connection.rollback()


    