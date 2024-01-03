import unittest
from unittest.mock import patch
from dao.vehicle_service import VehicleService
from exception.exceptions import DatabaseConnectionException


class TestVehicleService(unittest.TestCase):

    def setUp(self):
        self.vehicle_service = VehicleService()

    @patch('dao.vehicle_service.DBUtil.getDBConn')
    def test_update_vehicle(self, mock_get_conn):
        # Mocking the database connection and cursor
        mock_cursor = mock_get_conn.return_value.cursor.return_value

        # Mocking the execute method for a successful update
        mock_cursor.execute.return_value = None

        # Sample vehicle data for update
        vehicle_data = {
            'vehicle_id': 1,
            'model': 'UpdatedModel',
            'make': 'UpdatedMake',
            'year': 2024,
            'color': 'Red',
            'registration_number': 'XYZ456',
            'availability': 1,
            'daily_rate': 60.00
        }

        # Call the method to update the vehicle details
        self.vehicle_service.update_vehicle(vehicle_data)

        # Check if the execute method was called with the expected query and parameters
        expected_query = "UPDATE Vehicle SET Model=%s, Make=%s, Year=%s, Color=%s, RegistrationNumber=%s, Availability=%s, DailyRate=%s WHERE VehicleID=%s"
        expected_params = (
            'UpdatedModel', 'UpdatedMake', 2024, 'Red', 'XYZ456', 1, 60.00, 1
        )
        mock_cursor.execute.assert_called_once_with(expected_query, expected_params)

        # Ensure commit method is called after successful execution
        mock_get_conn.return_value.commit.assert_called_once()

    @patch('dao.vehicle_service.DBUtil.getDBConn')
    def test_update_vehicle_database_error(self, mock_get_conn):
        # Mocking the database connection and cursor
        mock_cursor = mock_get_conn.return_value.cursor.return_value

        # Mocking the execute method to raise a DatabaseConnectionException
        mock_cursor.execute.side_effect = DatabaseConnectionException("Error updating vehicle details in the database")

        # Sample vehicle data for update
        vehicle_data = {
            'vehicle_id': 1,
            'model': 'UpdatedModel',
            'make': 'UpdatedMake',
            'year': 2024,
            'color': 'Red',
            'registration_number': 'XYZ456',
            'availability': 1,
            'daily_rate': 60.00
        }

        # Call the method and expect a DatabaseConnectionException to be raised
        with self.assertRaises(DatabaseConnectionException):
            self.vehicle_service.update_vehicle(vehicle_data)


if __name__ == '__main__':
    unittest.main()
