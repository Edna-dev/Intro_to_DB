import pymysql

try:
    # Connect to MySQL server
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Edna-dev@2025"   # 👈 replace with your real MySQL password
    )

    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

except pymysql.MySQLError as e:
    print("Error while connecting to MySQL:", e)

finally:
    if conn:
        conn.close()
