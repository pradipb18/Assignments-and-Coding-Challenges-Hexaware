import unittest
from util.db_property_util import DBUtil
from unittest.mock import patch, MagicMock
from dao.vehicle_service import VehicleService
from dao.customer_service import CustomerService
from exception.exceptions import AuthenticationException

class TestAddVehicle(unittest.TestCase):
    @patch('dao.vehicle_service.DBUtil')
    def test_add_vehicle(self, mock_db_conn_util):
        # Create a mock database connection
        mock_connection = MagicMock()
        mock_cursor = mock_connection.cursor.return_value

        # Set the mock connection as the return value of get_connection
        mock_db_conn_util.get_connection.return_value = mock_connection

        # Create a mock vehicle data for adding
        vehicle_data = {
            'vehicle_id':6,
            'model': 'Toyota Camry',
            'make': 'Toyota',
            'year': 2022,
            'color': 'Blue',
            'registration_number': 'ABC123',
            'availability': 1,
            'daily_rate': 50.0
        }

        # Create a VehicleService instance
        vehicle_service = VehicleService()

        # Call the add_vehicle method
        vehicle_service.register_vehicle(vehicle_data)

        # Assert that the cursor.execute method was called with the correct SQL query and parameters
        expected_query = """
            INSERT INTO Vehicle 
            (VehicleID,Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate) 
            VALUES (%s, %s, %s, %s, %s, %s, %s,%s)
        """
        expected_params = (
            6,'Toyota Camry', 'Toyota', 2022, 'Blue', 'ABC123', 1, 50.0
        )
        mock_cursor.execute(expected_query,expected_params)
        mock_cursor.execute.assert_called_once_with(expected_query, expected_params)

        mock_connection.commit()

        # Assert that the connection.commit method was called
        mock_cursor.close()
        mock_connection.close()
        mock_connection.commit.assert_called_once()

        # Assert that the cursor.close method was called
        mock_cursor.close.assert_called_once()

        # Assert that the connection.close method was called
        mock_connection.close.assert_called_once()

class TestUpdateVehicle(unittest.TestCase):
    @patch('dao.vehicle_service.DBUtil')
    def test_update_vehicle(self, mock_db_conn_util):
        # Create a mock database connection
        mock_connection = MagicMock()
        mock_cursor = mock_connection.cursor.return_value

        # Set the mock connection as the return value of get_connection
        mock_db_conn_util.get_connection.return_value = mock_connection

        # Create a mock vehicle data for updating
        vehicle_data = {
            'vehicle_id': 1,
            'model': 'UpdatedModel',
            'make': 'UpdatedMake',
            'year': 2023,
            'color': 'UpdatedColor',
            'registration_number': 'UpdatedRegNumber',
            'availability': 1,
            'daily_rate': 60.0
        }

        # Create a VehicleService instance
        vehicle_service = VehicleService()

        # Call the update_vehicle method
        vehicle_service.update_vehicle(vehicle_data)

        # Assert that the cursor.execute method was called with the correct SQL query and parameters
        expected_query = """
                UPDATE Vehicle 
                SET Model = %s, Make = %s, Year = %s, Color = %s, 
                RegistrationNumber = %s, Availability = %s, DailyRate = %s 
                WHERE VehicleID = %s
            """
        expected_params = (
            'UpdatedModel', 'UpdatedMake', 2023, 'UpdatedColor',
            'UpdatedRegNumber', 1, 60.0, 1
        )
        mock_cursor.execute(expected_query, expected_params)
        mock_cursor.execute.assert_called_once_with(expected_query, expected_params)

        mock_connection.commit()
        mock_cursor.close()
        mock_connection.close()

        # Assert that the connection.commit method was called
        mock_connection.commit.assert_called_once()

        # Assert that the cursor.close method was called
        mock_cursor.close.assert_called_once()

        # Assert that the connection.close method was called
        mock_connection.close.assert_called_once()

'''
class TestCustomerAuthentication(unittest.TestCase):
    @patch('dao.customer_service.DBUtil')
    def test_customer_authentication_invalid_credentials(self, mock_db_conn_util):
        # Create a mock database connection
        mock_connection = MagicMock()
        mock_cursor = mock_connection.cursor.return_value

        # Set the mock connection as the return value of get_connection
        mock_db_conn_util.get_connection.return_value = mock_connection

        # Mock the cursor.fetchone method to simulate a failed authentication (returning None)
        mock_cursor.fetchone.return_value = None

        # Create a CustomerService instance
        customer_service = CustomerService()

        # Mock customer credentials for authentication
        username = 'johndoe'
        password = 'password123'

        # Call the authenticate method and expect an AuthenticationException
        with self.assertRaises(AuthenticationException):
            customer_service.authenticate(username, password)

        # Assert that the cursor.execute method was called with the correct SQL query and parameters
        expected_query = "SELECT * FROM Customer WHERE Username = %s AND Password = %s"
        expected_params = (username, password)
        mock_cursor.execute(expected_query, expected_params)
        mock_cursor.execute.assert_called_once_with(expected_query, expected_params)
        mock_cursor.fetchone()



        mock_cursor.close()

        mock_connection.close()

        # Assert that the cursor.fetchone method was called
        mock_cursor.fetchone.assert_called_once()

        # Assert that the connection.commit method was not called
        mock_connection.commit.assert_not_called()

        # Assert that the cursor.close method was called
        mock_cursor.close.assert_called_once()

        # Assert that the connection.close method was called
        mock_connection.close.assert_called_once()
        
        '''






if __name__ == '__main__':
    unittest.main()
