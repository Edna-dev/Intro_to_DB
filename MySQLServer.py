import mysql.connector
from mysql.connector import Error

try:
    # establish a connection to the MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
    )

    if connection.is_connected():
        print("Connection to MySQL server established successfully")

    # create database alxbookstore
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE alxbookstore")
    print("Database alxbookstore created successfully")

except Error as e:
    # handle exceptions
    print(f"Error: {e}")
