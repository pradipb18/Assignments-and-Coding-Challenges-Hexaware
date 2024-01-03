import unittest
from unittest.mock import patch
from dao.customer_service import CustomerService
from exception.exceptions import DatabaseConnectionException


class TestCustomerService(unittest.TestCase):

    def setUp(self):
        self.customer_service = CustomerService()

    @patch('dao.customer_service.DBUtil.getDBConn')
    def test_update_customer(self, mock_get_conn):
        # Mocking the database connection and cursor
        mock_cursor = mock_get_conn.return_value.cursor.return_value

        # Mocking the execute method for a successful update
        mock_cursor.execute.return_value = None

        # Sample customer data for update
        customer_data = {
            'customer_id': 1,
            'first_name': 'UpdatedFirstName',
            'last_name': 'UpdatedLastName',
            'email': 'updated.email@example.com',
            'phone_number': '987654321',
            'address': '456 Updated St',
            'username': 'updated_username',
            'password': 'updated_password'
        }

        # Call the method to update the customer
        self.customer_service.update_customer(customer_data)

        # Check if the execute method was called with the expected query and parameters
        expected_query = "UPDATE Customer SET FirstName=%s, LastName=%s, Email=%s, PhoneNumber=%s, Address=%s WHERE CustomerID=%s"
        expected_params = (
            'UpdatedFirstName', 'UpdatedLastName', 'updated.email@example.com', '987654321', '456 Updated St', 1
        )
        mock_cursor.execute.assert_called_once_with(expected_query, expected_params)

        # Ensure commit method is called after successful execution
        mock_get_conn.return_value.commit.assert_called_once()


if __name__ == '__main__':
    unittest.main()
