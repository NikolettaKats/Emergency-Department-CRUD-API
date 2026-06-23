import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        db = mysql.connector.connect(
        host="localhost",
        user="YOUR_USERNAME", # Placeholder
        password="YOUR_PASSWORD", # Placeholder
        database="istoriko_tep"
    )
        if db.is_connected():
            print("Connected to the database")
            return db
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None
   



