
from Exception.Exception import DatabaseConnectionException


class DatabaseHandler:
    def execute_query(self, query):
        try:
            raise DatabaseConnectionException("Database is offline.")
        except DatabaseConnectionException as e:
            print(f"Database Error: {e}")