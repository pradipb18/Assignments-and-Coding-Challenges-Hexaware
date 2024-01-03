# dao/admin_service.py
import mysql.connector
from entity.admin import Admin
from exception.exceptions import InvalidInputException, DatabaseConnectionException
from util.db_property_util import DBUtil


class AdminService:


    def get_admin_by_id(self, admin_id):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            query = "SELECT * FROM Admin WHERE AdminID = %s"
            cursor.execute(query, (admin_id,))

            admin_data = cursor.fetchone()

            if not admin_data:
                raise InvalidInputException(f"Admin with ID {admin_id} not found.")

            admin = Admin(**admin_data)
            return admin

        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        finally:
            cursor.close()
            connection.close()

    def get_admin_by_username(self, username):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            query = "SELECT * FROM Admin WHERE Username = %s"
            cursor.execute(query, (username,))

            admin_data = cursor.fetchone()

            if not admin_data:
                raise InvalidInputException(f"Admin with username {username} not found.")

            admin = Admin(*admin_data)
            return admin

        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        finally:
            cursor.close()
            connection.close()

    def register_admin(self, admin_data):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            query = "INSERT INTO Admin (AdminID,FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (
                admin_data['admin_id'],
                admin_data['first_name'],
                admin_data['last_name'],
                admin_data['email'],
                admin_data['phone_number'],
                admin_data['username'],
                admin_data['password'],
                admin_data['role'],
                admin_data['join_date']
            ))

            connection.commit()
            return admin_data['admin_id']

        except mysql.connector.Error as err:
            connection.rollback()
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        finally:
            cursor.close()
            connection.close()

    def update_admin(self, admin_data):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            query = "UPDATE Admin SET FirstName=%s, LastName=%s, Email=%s, PhoneNumber=%s, Role=%s WHERE AdminID=%s"
            cursor.execute(query, (admin_data['first_name'], admin_data['last_name'], admin_data['email'],
                                   admin_data['phone_number'], admin_data['role'], admin_data['admin_id']))

            connection.commit()

        except mysql.connector.Error as err:
            connection.rollback()
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        finally:
            cursor.close()
            connection.close()

    def delete_admin(self, admin_id):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            query = "DELETE FROM Admin WHERE AdminID=%s"
            cursor.execute(query, (admin_id,))

            connection.commit()

        except mysql.connector.Error as err:
            connection.rollback()
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        finally:
            cursor.close()
            connection.close()
