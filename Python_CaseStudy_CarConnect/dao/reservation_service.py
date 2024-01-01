# dao/reservation_service.py
import mysql.connector
from datetime import datetime
from entity.reservation import Reservation
from exception.exceptions import InvalidInputException, DatabaseConnectionException
from util.db_property_util import DBUtil


class ReservationService:


    def get_reservation_by_id(self, reservation_id):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            query = "SELECT * FROM Reservation WHERE ReservationID = %s"
            cursor.execute(query, (reservation_id,))

            reservation_data = cursor.fetchone()

            if not reservation_data:
                raise InvalidInputException(f"Reservation with ID {reservation_id} not found.")

            reservation = Reservation(**reservation_data)
            return reservation

        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        finally:
            cursor.close()
            connection.close()

    def get_reservations_by_customer_id(self, customer_id):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            query = "SELECT * FROM Reservation WHERE CustomerID = %s"
            cursor.execute(query, (customer_id,))

            reservations_data = cursor.fetchall()

            if not reservations_data:
                raise InvalidInputException(f"No reservations found for customer with ID {customer_id}.")

            reservations = [Reservation(**data) for data in reservations_data]
            return reservations

        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        finally:
            cursor.close()
            connection.close()

    def create_reservation(self, reservation_data):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            query = "INSERT INTO Reservation (ReservationID,CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status) VALUES (%s, %s, %s, %s, %s, %s,%s)"
            cursor.execute(query, (reservation_data['reservation_id'],reservation_data['customer_id'], reservation_data['vehicle_id'],
                                   reservation_data['start_date'], reservation_data['end_date'],
                                   reservation_data['total_cost'], reservation_data['status']))

            connection.commit()
            return reservation_data['reservation_id']  # return the ID of the newly inserted reservation

        except mysql.connector.Error as err:
            connection.rollback()
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        finally:
            cursor.close()
            connection.close()

    def update_reservation(self, reservation_data):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()
            query = "UPDATE Reservation SET CustomerID=%s, VehicleID=%s, StartDate=%s, EndDate=%s, TotalCost=%s, Status=%s WHERE ReservationID=%s"
            cursor.execute(query, (reservation_data['customer_id'], reservation_data['vehicle_id'], reservation_data['start_date'],reservation_data['end_date'], reservation_data['total_cost'],reservation_data['status'], reservation_data['reservation_id']))
            connection.commit()


        except mysql.connector.Error as err:
            connection.rollback()
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        finally:
            cursor.close()
            connection.close()

    def cancel_reservation(self, reservation_id):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            query = "UPDATE Reservation SET Status='Canceled' WHERE ReservationID=%s"
            cursor.execute(query, (reservation_id,))

            connection.commit()

        except mysql.connector.Error as err:
            connection.rollback()
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        finally:
            cursor.close()
            connection.close()
