import unittest
from unittest.mock import patch, MagicMock
from dao.vehicle_service import VehicleService
from exception.exceptions import DatabaseConnectionException, InvalidInputException


class TestVehicleService(unittest.TestCase):

    def setUp(self):
        self.vehicle_service = VehicleService()

    @patch('dao.vehicle_service.DBUtil.getDBConn')
    def test_get_available_vehicles(self, mock_get_conn):
        # Mocking the database connection and cursor
        mock_cursor = mock_get_conn.return_value.cursor.return_value

        # Mocking the execute method to fetch available vehicles
        mock_cursor.fetchall.return_value = [
            {'VehicleID': 1, 'Model': 'Sedan', 'Make': 'Toyota', 'Year': 2022, 'Color': 'Blue',
             'RegistrationNumber': 'ABC123', 'Availability': 1, 'DailyRate': 50.00},
            {'VehicleID': 2, 'Model': 'SUV', 'Make': 'Honda', 'Year': 2023, 'Color': 'Red',
             'RegistrationNumber': 'XYZ456', 'Availability': 1, 'DailyRate': 60.00},
        ]

        # Call the method to get available vehicles
        available_vehicles = self.vehicle_service.get_available_vehicles()

        # Check if the execute method was called with the expected query
        expected_query = "SELECT * FROM Vehicle WHERE Availability = 1"
        mock_cursor.execute.assert_called_once_with(expected_query)

        # Ensure that the method returned the expected list of available vehicles
        expected_result = [
            {'VehicleID': 1, 'Model': 'Sedan', 'Make': 'Toyota', 'Year': 2022, 'Color': 'Blue',
             'RegistrationNumber': 'ABC123', 'Availability': 1, 'DailyRate': 50.00},
            {'VehicleID': 2, 'Model': 'SUV', 'Make': 'Honda', 'Year': 2023, 'Color': 'Red',
             'RegistrationNumber': 'XYZ456', 'Availability': 1, 'DailyRate': 60.00},
        ]
        self.assertEqual(available_vehicles, expected_result)

    @patch('dao.vehicle_service.DBUtil.getDBConn')
    def test_get_available_vehicles_database_error(self, mock_get_conn):
        # Mocking the database connection and cursor
        mock_cursor = mock_get_conn.return_value.cursor.return_value

        # Mocking the execute method to raise a DatabaseConnectionException
        mock_cursor.execute.side_effect = DatabaseConnectionException("Error fetching available vehicles")

        # Call the method and expect a DatabaseConnectionException to be raised
        with self.assertRaises(DatabaseConnectionException):
            self.vehicle_service.get_available_vehicles()


if __name__ == '__main__':
    unittest.main()
