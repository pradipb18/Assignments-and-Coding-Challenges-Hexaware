import unittest
from unittest.mock import patch
from dao.vehicle_service import VehicleService
from exception.exceptions import DatabaseConnectionException


class TestVehicleService(unittest.TestCase):

    def setUp(self):
        self.vehicle_service = VehicleService()

    @patch('dao.vehicle_service.DBUtil.getDBConn')
    def test_get_all_vehicles(self, mock_get_conn):
        # Mocking the database connection and cursor
        mock_cursor = mock_get_conn.return_value.cursor.return_value

        # Mocking the execute method to fetch all vehicles
        mock_cursor.fetchall.return_value = [
            {'VehicleID': 1, 'Model': 'Sedan', 'Make': 'Toyota', 'Year': 2022, 'Color': 'Blue',
             'RegistrationNumber': 'ABC123', 'Availability': 1, 'DailyRate': 50.00},
            {'VehicleID': 2, 'Model': 'SUV', 'Make': 'Honda', 'Year': 2023, 'Color': 'Red',
             'RegistrationNumber': 'XYZ456', 'Availability': 1, 'DailyRate': 60.00},
        ]

        # Call the method to get all vehicles
        all_vehicles = self.vehicle_service.get_all_vehicles()

        # Check if the execute method was called with the expected query
        expected_query = "SELECT * FROM Vehicle"
        mock_cursor.execute.assert_called_once_with(expected_query)

        # Ensure that the method returned the expected list of all vehicles
        expected_result = [
            {'VehicleID': 1, 'Model': 'Sedan', 'Make': 'Toyota', 'Year': 2022, 'Color': 'Blue',
             'RegistrationNumber': 'ABC123', 'Availability': 1, 'DailyRate': 50.00},
            {'VehicleID': 2, 'Model': 'SUV', 'Make': 'Honda', 'Year': 2023, 'Color': 'Red',
             'RegistrationNumber': 'XYZ456', 'Availability': 1, 'DailyRate': 60.00},
        ]
        self.assertEqual(all_vehicles, expected_result)

    @patch('dao.vehicle_service.DBUtil.getDBConn')
    def test_get_all_vehicles_database_error(self, mock_get_conn):
        # Mocking the database connection and cursor
        mock_cursor = mock_get_conn.return_value.cursor.return_value

        # Mocking the execute method to raise a DatabaseConnectionException
        mock_cursor.execute.side_effect = DatabaseConnectionException("Error fetching all vehicles")

        # Call the method and expect a DatabaseConnectionException to be raised
        with self.assertRaises(DatabaseConnectionException):
            self.vehicle_service.get_all_vehicles()


if __name__ == '__main__':
    unittest.main()
