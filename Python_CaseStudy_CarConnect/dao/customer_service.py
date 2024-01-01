# dao/customer_service.py
import mysql.connector
from entity.customer import Customer
from exception.exceptions import AuthenticationException, InvalidInputException, DatabaseConnectionException,CustomerNotFoundException
from util.db_property_util import DBUtil


class CustomerService:

    def authenticate(self, username, password):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            query = "SELECT * FROM Customer WHERE Username = %s AND Password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result :
                print("customer found",[*result])
                customer = Customer(*result)
                return customer
            else:
                print("customer not found")
                raise AuthenticationException("Invalid username or password.")

        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()






    def get_customer_by_id(self, customer_id):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            query = "SELECT * FROM Customer WHERE CustomerID = %s"
            cursor.execute(query, (customer_id,))

            customer_data = cursor.fetchone()

            if not customer_data:
                raise InvalidInputException(f"Customer with ID {customer_id} not found.")

            customer = Customer(**customer_data)
            return customer

        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        finally:
            cursor.close()
            connection.close()

    def get_customer_by_username(self, username):

            try:
                connection = DBUtil.getDBConn()
                cursor = connection.cursor()

                query = "SELECT * FROM Customer WHERE Username = %s"
                cursor.execute(query, (username,))
                result = cursor.fetchone()

                if result:
                    customer = Customer(*result)
                    return customer
                else:
                    raise CustomerNotFoundException(f"Customer with ID {username} not found.")

            except Exception as e:
                raise DatabaseConnectionException(f"Error connecting to the database: {str(e)}")

            finally:
                if cursor:
                    cursor.close()
                if connection:
                    connection.close()

    def register_customer(self, customer_data):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            query = """
                INSERT INTO Customer 
                (CustomerID,FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate) 
                VALUES (%s,%s, %s, %s, %s, %s, %s, %s, NOW())
            """
            cursor.execute(query, (
                customer_data['customer_id'],
                customer_data['first_name'],
                customer_data['last_name'],
                customer_data['email'],
                customer_data['phone_number'],
                customer_data['address'],
                customer_data['username'],
                customer_data['password']
            ))

            connection.commit()
            return  customer_data['customer_id'] # return the ID of the newly inserted customer

        except mysql.connector.Error as err:
            connection.rollback()
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        except Exception as e:
            connection.rollback()
            raise InvalidInputException(f"Error registering customer: {e}")

        finally:
            cursor.close()
            connection.close()
    def update_customer(self, customer_data):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            query = "UPDATE Customer SET FirstName=%s, LastName=%s, Email=%s, PhoneNumber=%s, Address=%s WHERE CustomerID=%s"
            cursor.execute(query, (customer_data['first_name'], customer_data['last_name'], customer_data['email'],
                                   customer_data['phone_number'], customer_data['address'],
                                   customer_data['customer_id']))

            connection.commit()

        except mysql.connector.Error as err:
            connection.rollback()
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        finally:
            cursor.close()
            connection.close()

    def delete_customer(self, customer_id):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            query = "DELETE FROM Customer WHERE CustomerID=%s"
            cursor.execute(query, (customer_id,))

            connection.commit()

        except mysql.connector.Error as err:
            connection.rollback()
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        finally:
            cursor.close()
            connection.close()





