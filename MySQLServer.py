import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("✅ MySQL Database connection successful")
    except Error as err:
        print(f"❌ Error: '{err}'")
    return connection


# Create database function
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("✅ Database created successfully")
    except Error as err:
        print(f"❌ Error: '{err}'")


if __name__ == "__main__":
    # Step 1: connect to MySQL server
    connection = create_server_connection("localhost", "root", "")

    # Step 2: create the 'alxbookstore' database
    create_database_query = "CREATE DATABASE alxbookstore"
    create_database(connection, create_database_query)
