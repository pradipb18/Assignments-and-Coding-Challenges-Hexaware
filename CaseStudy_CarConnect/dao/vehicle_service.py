
import mysql.connector
from entity.vehicle import Vehicle
from exception.exceptions import InvalidInputException, DatabaseConnectionException
from util.db_property_util import DBUtil


class VehicleService:



    def get_vehicle_by_id(self, vehicle_id):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            query = "SELECT * FROM Vehicle WHERE VehicleID = %s"
            cursor.execute(query, (vehicle_id,))

            vehicle_data = cursor.fetchone()

            if not vehicle_data:
                raise InvalidInputException(f"Vehicle with ID {vehicle_id} not found.")

            vehicle = Vehicle(**vehicle_data)
            return vehicle

        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        finally:
            cursor.close()
            connection.close()

    def get_available_vehicles(self):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor(dictionary=True)

            query = "SELECT * FROM Vehicle WHERE Availability = 1"
            cursor.execute(query)

            vehicles_data = cursor.fetchall()

            if not vehicles_data:
                raise InvalidInputException("No available vehicles found.")

            return vehicles_data

        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        finally:
            cursor.close()
            connection.close()

    def register_vehicle(self, vehicle_data):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            query = "INSERT INTO Vehicle (VehicleID,Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (
                vehicle_data['vehicle_id'],
                vehicle_data['model'],
                vehicle_data['make'],
                vehicle_data['year'],
                vehicle_data['color'],
                vehicle_data['registration_number'],
                vehicle_data['availability'],
                vehicle_data['daily_rate']
            ))

            connection.commit()
            return vehicle_data['vehicle_id']

        except mysql.connector.Error as err:
            connection.rollback()
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")
        except Exception as e:
            connection.rollback()
            raise DatabaseConnectionException(f"Error adding a new vehicle to the database: {e}")
        finally:
            cursor.close()
            connection.close()

    def update_vehicle(self, vehicle_data):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            query = "UPDATE Vehicle SET Model=%s, Make=%s, Year=%s, Color=%s, RegistrationNumber=%s, Availability=%s, DailyRate=%s WHERE VehicleID=%s"
            cursor.execute(query, (vehicle_data['model'], vehicle_data['make'], vehicle_data['year'],
                                   vehicle_data['color'], vehicle_data['registration_number'],
                                   vehicle_data['availability'],
                                   vehicle_data['daily_rate'], vehicle_data['vehicle_id']))

            connection.commit()

        except mysql.connector.Error as err:
            connection.rollback()
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        finally:
            cursor.close()
            connection.close()

    def remove_vehicle(self, vehicle_id):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor()

            query = "DELETE FROM Vehicle WHERE VehicleID=%s"
            cursor.execute(query, (vehicle_id,))

            connection.commit()

        except mysql.connector.Error as err:
            connection.rollback()
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        finally:
            cursor.close()
            connection.close()

    def get_all_vehicles(self):
        try:
            connection = DBUtil.getDBConn()
            cursor = connection.cursor(dictionary=True)

            query = "SELECT * FROM Vehicle"
            cursor.execute(query)

            vehicles_data = cursor.fetchall()

            if not vehicles_data:
                raise InvalidInputException("No vehicles found.")

            return vehicles_data

        except mysql.connector.Error as err:
            raise DatabaseConnectionException(f"Error connecting to the database: {err}")

        finally:
            cursor.close()
            connection.close()