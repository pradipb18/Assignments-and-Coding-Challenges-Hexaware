
import mysql.connector
from mysql.connector import Error

class DatabaseConnector:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor=None
    def open_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            self.cursor=self.connection.cursor()
            print("Connected to MySQL database")
        except Error as e:
            print(f"Error: {e}")

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            self.cursor.close()
            print("Connection closed")