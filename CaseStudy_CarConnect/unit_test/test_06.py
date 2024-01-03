import unittest
from unittest.mock import patch, MagicMock
from dao.customer_service import CustomerService
from exception.exceptions import AuthenticationException


class TestCustomerAuthentication(unittest.TestCase):

    @patch('dao.customer_service.DBUtil.getDBConn')
    def test_invalid_credentials(self, mock_get_conn):
        # Arrange
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        customer_service = CustomerService()

        # Set up a mock result for the authentication query
        mock_cursor.fetchone.return_value = None

        # Act and Assert
        with self.assertRaises(AuthenticationException):
            customer_service.authenticate('invalid_username', 'invalid_password')

        # Assert that the cursor's execute method was called with the expected query
        expected_query = "SELECT * FROM Customer WHERE Username = %s AND Password = %s"
        expected_params = ('invalid_username', 'invalid_password')
        mock_cursor.execute.assert_called_once_with(expected_query, expected_params)

        # Clean up
        mock_cursor.close.assert_called_once()
        mock_conn.close.assert_called_once()


if __name__ == '__main__':
    unittest.main()
