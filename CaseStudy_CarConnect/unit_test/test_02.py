import unittest
from unittest.mock import patch
from dao.vehicle_service import VehicleService
from exception.exceptions import DatabaseConnectionException, InvalidInputException


class TestVehicleService(unittest.TestCase):

    def setUp(self):
        self.vehicle_service = VehicleService()

    @patch('dao.vehicle_service.DBUtil.getDBConn')
    def test_add_new_vehicle(self, mock_get_conn):
        # Mocking the database connection and cursor
        mock_cursor = mock_get_conn.return_value.cursor.return_value

        # Mocking the execute method for a successful insertion
        mock_cursor.execute.return_value = None

        # Sample vehicle data for insertion
        vehicle_data = {
            'vehicle_id': 1,
            'model': 'NewModel',
            'make': 'NewMake',
            'year': 2023,
            'color': 'Blue',
            'registration_number': 'ABC123',
            'availability': 1,
            'daily_rate': 50.00
        }

        # Call the method to add a new vehicle
        new_vehicle_id = self.vehicle_service.register_vehicle(vehicle_data)

        # Check if the execute method was called with the expected query and parameters
        expected_query = "INSERT INTO Vehicle (VehicleID,Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        expected_params = (
            1, 'NewModel', 'NewMake', 2023, 'Blue', 'ABC123', 1, 50.00
        )
        mock_cursor.execute.assert_called_once_with(expected_query, expected_params)

        # Ensure commit method is called after successful execution
        mock_get_conn.return_value.commit.assert_called_once()

        # Ensure the method returns the correct vehicle ID
        self.assertEqual(new_vehicle_id, 1)

    @patch('dao.vehicle_service.DBUtil.getDBConn')
    def test_add_new_vehicle_database_error(self, mock_get_conn):
        # Mocking the database connection and cursor
        mock_cursor = mock_get_conn.return_value.cursor.return_value

        # Mocking the execute method to raise a DatabaseConnectionException
        mock_cursor.execute.side_effect = Exception("Error adding a new vehicle to the database")

        # Sample vehicle data for insertion
        vehicle_data = {
            'vehicle_id': 1,
            'model': 'NewModel',
            'make': 'NewMake',
            'year': 2023,
            'color': 'Blue',
            'registration_number': 'ABC123',
            'availability': 1,
            'daily_rate': 50.00
        }

        # Call the method and expect a DatabaseConnectionException to be raised
        with self.assertRaises(DatabaseConnectionException):
            self.vehicle_service.register_vehicle(vehicle_data)


if __name__ == '__main__':
    unittest.main()
