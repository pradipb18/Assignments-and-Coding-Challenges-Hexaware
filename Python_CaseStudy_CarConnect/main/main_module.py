# main/main_module.py
from dao.customer_service import CustomerService
from dao.vehicle_service import VehicleService
from dao.reservation_service import ReservationService
from dao.admin_service import AdminService
from entity.admin import Admin
from entity.customer import Customer
from entity.reservation import Reservation
from entity.vehicle import Vehicle
from exception.exceptions import InvalidInputException, DatabaseConnectionException
from util.db_property_util import DBUtil


class MainModule:
    def __init__(self):


        # Initialize services with the constructed connection string
        self.customer_service = CustomerService()
        self.vehicle_service = VehicleService()
        self.reservation_service = ReservationService()
        self.admin_service = AdminService()


    def run_menu(self):
        while True:
            print("\n--- Car Connect System Menu ---")
            print("1. Customer Management")
            print("2. Vehicle Management")
            print("3. Reservation System")
            print("4. Admin Management")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.customer_management()
            elif choice == '2':
                self.vehicle_management()
            elif choice == '3':
                self.reservation_system()
            elif choice == '4':
                self.admin_management()
            elif choice == '5':
                print("Exiting Car Connect System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    def customer_management(self):
        while True:
            print("\n--- Customer Management ---")
            print("1. Get Customer by ID")
            print("2. Get Customer by Username")
            print("3. Register Customer")
            print("4. Update Customer")
            print("5. Delete Customer")
            print("6. Back to Main Menu")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.get_customer_by_id()
            elif choice == '2':
                self.get_customer_by_username()
            elif choice == '3':
                self.register_customer()
            elif choice == '4':
                self.update_customer()
            elif choice == '5':
                self.delete_customer()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")


    def vehicle_management(self):
        while True:
            print("\n--- Vehicle Management ---")
            print("1. Get Vehicle by ID")
            print("2. Get Available Vehicles")
            print("3. Add Vehicle")
            print("4. Update Vehicle")
            print("5. Remove Vehicle")
            print("6. Back to Main Menu")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.get_vehicle_by_id()
            elif choice == '2':
                self.view_available_vehicles()
            elif choice == '3':
                self.register_vehicle()
            elif choice == '4':
                self.update_vehicle()
            elif choice == '5':
                self.remove_vehicle()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

    def reservation_system(self):
        while True:
            print("\nReservation Management:")
            print("1. View Reservation Details")
            print("2. View Reservation Details by CustomerID")
            print("3. Create Reservation")
            print("4. Update Reservation Details")
            print("5. Cancel Reservation")
            print("6. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.get_reservation_by_id()
            elif choice == "2":
                self.get_reservations_by_customer_id()
            elif choice == "3":
                self.create_reservation()
            elif choice == "4":
                self.update_reservation()
            elif choice == "5":
                self.cancel_reservation()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")


    def admin_management(self):
        while True:
            print("\n--- Admin Management ---")
            print("1. Get Admin by ID")
            print("2. Get Admin by User name")
            print("3. Register Admin")
            print("4. Update Admin")
            print("5. Delete Admin")
            print("6. Back to Main Menu")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                self.get_admin_by_id()
            elif choice == '2':
                self.get_admin_by_username()
            elif choice == '3':
                self.register_admin()
            elif choice == '4':
                self.update_admin()
            elif choice == '5':
                self.delete_admin()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

    def get_customer_by_id(self):
        try:
            customer_id = input("Enter Customer ID: ")

            # Establish a connection and cursor
            connection = None
            cursor = None

            try:
                connection_params = {
                    "host": "localhost",
                    "user": "root",
                    "password": "pradip",
                    "database": "carconnect"
                }
                connection = DBUtil.getDBConn()
                cursor = connection.cursor()

                query = "SELECT * FROM Customer WHERE CustomerID = %s"
                cursor.execute(query, (customer_id,))
                result = cursor.fetchone()

                if result:
                    customer = Customer(*result)
                    # Display customer information
                    print("\nCustomer Information:")
                    print(f"Customer ID: {customer.customer_id}")
                    print(f"First Name: {customer.first_name}")
                    print(f"Last Name: {customer.last_name}")
                    # Display other customer properties as needed
                else:
                    print(f"Customer with ID {customer_id} not found.")

            except DatabaseConnectionException as e:
                print(f"Error connecting to the database: {str(e)}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

            finally:
                # Close the cursor and connection in the finally block to ensure they are closed even if an exception occurs
                if cursor:
                    cursor.close()
                if connection:
                    connection.close()
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def get_customer_by_username(self):
        username = input("Enter Customer Username: ")
        try:
            customer = self.customer_service.get_customer_by_username(username)
            print("Customer Details:")
            print("Customer ID : ",customer.customer_id)
            print("First Name : ", customer.first_name)
            print("Last Name : ",customer.last_name)
            print("Email ",customer.email)
            print("Phone Number : ",customer.phone_number)
            print("Address : ",customer.address)
            print("Username  : ",customer.username)
            print("Password : ",customer.password)
            print("Registration Date : ",customer.registration_date)

        except InvalidInputException as e:
            print(f"Error: {e}")

    def register_customer(self):
        # Get customer data from user input
        customer_id = input("Enter Customer ID: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email: ")
        phone_number = input("Enter Phone Number: ")
        address = input("Enter Address: ")
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        try:
            # Register the customer
            customer_data = {
                "customer_id":customer_id,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone_number": phone_number,
                "address": address,
                "username": username,
                "password": password
            }
            customer_id = self.customer_service.register_customer(customer_data)
            print(f"Customer registered successfully with ID: {customer_id}")
        except InvalidInputException as e:
            print(f"Error: {e}")

    def update_customer(self):
        try:
            # Get customer data from user input
            customer_id = int(input("Enter Customer ID to update: "))
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            email = input("Enter Email: ")
            phone_number = input("Enter Phone Number: ")
            address = input("Enter Address: ")

            # Update the customer
            customer_data = {
                "customer_id": customer_id,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone_number": phone_number,
                "address": address
            }
            self.customer_service.update_customer(customer_data)
            print("Customer updated successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid Customer ID.")
        except InvalidInputException as e:
            print(f"Error: {e}")

    def delete_customer(self):
        try:
            # Get customer ID from user input
            customer_id = int(input("Enter Customer ID to delete: "))
            self.customer_service.delete_customer(customer_id)
            print("Customer deleted successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid Customer ID.")
        except InvalidInputException as e:
            print(f"Error: {e}")


    def get_vehicle_by_id(self):
        try:
            vehicle_id = input("Enter Vehicle ID: ")

            # Establish a connection and cursor
            connection = None
            cursor = None

            try:
                connection_params = {
                    "host": "localhost",
                    "user": "root",
                    "password": "pradip",
                    "database": "carconnect"
                }
                connection = DBUtil.getDBConn()
                cursor = connection.cursor()

                query = "SELECT * FROM Vehicle WHERE VehicleID = %s"
                cursor.execute(query, (vehicle_id,))
                result = cursor.fetchone()

                if result:
                    vehicle = Vehicle(*result)
                    # Display customer information
                    print("\nVehicle Information:")
                    print(f"Vehicle ID: {vehicle.vehicle_id}")
                    print(f"Make: {vehicle.make}")
                    print(f"Model: {vehicle.model}")
                    print(f"Year: {vehicle.year}")
                    print(f"Color:{vehicle.color}")
                    # Display other customer properties as needed
                else:
                    print(f"Vehicle with ID {vehicle_id} not found.")

            except DatabaseConnectionException as e:
                print(f"Error connecting to the database: {str(e)}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

            finally:
                # Close the cursor and connection in the finally block to ensure they are closed even if an exception occurs
                if cursor:
                    cursor.close()
                if connection:
                    connection.close()
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def view_available_vehicles(self):
        try:
            available_vehicles = self.vehicle_service.get_available_vehicles()
            if available_vehicles:
                print("\nAvailable Vehicles:")
                for vehicle in available_vehicles:
                    print(f"Vehicle ID: {vehicle['VehicleID']}")
                    print(f"Model: {vehicle['Model']}")
                    print(f"Make: {vehicle['Make']}")
                    print(f"Year: {vehicle['Year']}")
                    print(f"Color: {vehicle['Color']}")
                    print(f"Registration Number: {vehicle['RegistrationNumber']}")
                    print(f"Daily Rate: {vehicle['DailyRate']}")
                    print("-------------------------")
            else:
                print("No available vehicles.")
        except DatabaseConnectionException as e:
            print(f"Error: {e}")

    def register_vehicle(self):
        # Get vehicle data from user input
        vehicle_id = input("Enter Vehicle ID: ")
        model = input("Enter Model Name: ")
        make = input("Enter Make Name: ")
        year = input("Enter Year: ")
        color = input("Enter Color: ")
        registration_number = input("Enter Registration Number: ")
        availability = input("Enter Availability: ")
        daily_rate = input("Enter DailyRate: ")

        try:
            # Register the vehicle
            vehicle_data = {
                "vehicle_id":vehicle_id ,
                "model": model,
                "make": make,
                "year": year,
                "color": color,
                "registration_number": registration_number,
                "availability":availability,
                "daily_rate": daily_rate
            }
            vehicle_id = self.vehicle_service.register_vehicle(vehicle_data)
            print(f"Vehicle registered successfully with ID: {vehicle_id}")
        except InvalidInputException as e:
            print(f"Error: {e}")

    def update_vehicle(self):
        try:
            # Get customer data from user input
            vehicle_id = int(input("Enter Vehicle ID to update: "))
            model = input("Enter Model: ")
            make = input("Enter Make: ")
            year = input("Enter Year: ")
            color = input("Enter Color: ")
            registration_number = input("Enter Registration Number: ")
            availability = input("Enter Availability: ")
            daily_rate = input("Enter Daily Rate: ")

            # Update the vehicle
            vehicle_data = {
                "vehicle_id": vehicle_id,
                "model": model,
                "make": make,
                "year": year,
                "color": color,
                "registration_number": registration_number,
                "availability": availability,
                "daily_rate": daily_rate
            }
            self.vehicle_service.update_vehicle(vehicle_data)
            print("Vehicle updated successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid Vehicle ID.")
        except InvalidInputException as e:
            print(f"Error: {e}")

    def remove_vehicle(self):
        try:
            # Get customer ID from user input
            vehicle_id = int(input("Enter Vehicle ID to delete: "))
            self.vehicle_service.remove_vehicle(vehicle_id)
            print("Vehicle deleted successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid Vehicle ID.")
        except InvalidInputException as e:
            print(f"Error: {e}")


    def get_reservation_by_id(self):
        try:
            reservation_id = input("Enter Reservation ID: ")

            # Establish a connection and cursor
            connection = None
            cursor = None

            try:
                connection_params = {
                    "host": "localhost",
                    "user": "root",
                    "password": "pradip",
                    "database": "carconnect"
                }
                connection = DBUtil.getDBConn()
                cursor = connection.cursor()

                query = "SELECT * FROM Reservation WHERE ReservationID = %s"
                cursor.execute(query, (reservation_id,))
                result = cursor.fetchone()

                if result:
                    reservation = Reservation(*result)
                    # Display customer information
                    print("\nCustomer Information:")
                    print(f"Reservation ID: {reservation.reservation_id}")
                    print(f"Customer ID: {reservation.customer_id}")
                    print(f"Vehicle ID: {reservation.vehicle_id}")
                    print(f"Start Date: {reservation.start_date}")
                    print(f"End Date: {reservation.end_date}")
                    print(f"Total Cost: {reservation.total_cost}")
                    # Display other customer properties as needed
                else:
                    print(f"Reservation with ID {reservation_id} not found.")

            except DatabaseConnectionException as e:
                print(f"Error connecting to the database: {str(e)}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

            finally:

                if cursor:
                    cursor.close()
                if connection:
                    connection.close()
        except Exception as e:
            print(f"An error occurred: {str(e)}")


    def get_reservations_by_customer_id(self):
        try:
            customer_id = input("Enter Customer ID: ")


            connection = None
            cursor = None

            try:
                connection_params = {
                    "host": "localhost",
                    "user": "root",
                    "password": "pradip",
                    "database": "carconnect"
                }
                connection = DBUtil.getDBConn()
                cursor = connection.cursor()

                query = "SELECT * FROM Reservation WHERE CustomerID = %s"
                cursor.execute(query, (customer_id,))
                result = cursor.fetchone()

                if result:
                    reservation = Reservation(*result)

                    print("\nCustomer Information:")
                    print(f"Reservation ID: {reservation.reservation_id}")
                    print(f"Customer ID: {reservation.customer_id}")
                    print(f"Vehicle ID: {reservation.vehicle_id}")
                    print(f"Start Date: {reservation.start_date}")
                    print(f"End Date: {reservation.end_date}")
                    print(f"Total Cost: {reservation.total_cost}")
                    # Display other customer properties as needed
                else:
                    print(f"Reservation with Customer ID {customer_id} not found.")

            except DatabaseConnectionException as e:
                print(f"Error connecting to the database: {str(e)}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

            finally:

                if cursor:
                    cursor.close()
                if connection:
                    connection.close()
        except Exception as e:
            print(f"An error occurred: {str(e)}")


    def create_reservation(self):
        # Get customer data from user input
        reservation_id = input("Enter Reservation ID: ")
        customer_id = input("Enter Customer ID: ")
        vehicle_id = input("Enter Vehicle ID: ")
        start_date = input("Enter Start Date: ")
        end_date = input("Enter End Date: ")
        total_cost = input("Enter Total Cost: ")
        status = input("Enter Status: ")


        try:

            reservation_data = {
                "reservation_id":reservation_id,
                "customer_id": customer_id,
                "vehicle_id": vehicle_id,
                "start_date": start_date,
                "end_date": end_date,
                "total_cost": total_cost,
                "status":status
            }
            reservation_id = self.reservation_service.create_reservation(reservation_data)
            print(f"Reservation Information registered successfully with ID: {reservation_id}")
        except InvalidInputException as e:
            print(f"Error: {e}")


    def update_reservation(self):
        try:

            reservation_id = int(input("Enter Reservation ID to update: "))
            customer_id = int(input("Enter Customer ID to update: "))
            vehicle_id = int(input("Enter Vehicle ID to update: "))
            start_date = input("Enter Start Date: ")
            end_date = input("Enter End Date: ")
            total_cost = input("Enter Total cost: ")
            status = input("Enter Status: ")



            reservation_data = {
                "reservation_id":reservation_id,
                "customer_id": customer_id,
                "vehicle_id": vehicle_id,
                "start_date": start_date,
                "end_date": end_date,
                "total_cost": total_cost,
                "status": status

            }
            self.reservation_service.update_reservation(reservation_data)
            print("Reservation updated successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid Reservation ID.")
        except InvalidInputException as e:
            print(f"Error: {e}")


    def cancel_reservation(self):
        try:
            # Get customer ID from user input
            reservation_id = int(input("Enter Reservation ID to cancel: "))
            self.reservation_service.cancel_reservation(reservation_id)
            print("Reservation canceled successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid Reservation ID.")
        except InvalidInputException as e:
            print(f"Error: {e}")


    def get_admin_by_id(self):
        try:
            admin_id = input("Enter Admin ID: ")


            connection = None
            cursor = None

            try:
                connection_params = {
                    "host": "localhost",
                    "user": "root",
                    "password": "pradip",
                    "database": "carconnect"
                }
                connection = DBUtil.getDBConn()
                cursor = connection.cursor()

                query = "SELECT * FROM Admin WHERE AdminID = %s"
                cursor.execute(query, (admin_id,))
                result = cursor.fetchone()

                if result:
                    admin = Admin(*result)
                    # Display customer information
                    print("\nCustomer Information:")
                    print(f"Admin ID: {admin.admin_id}")
                    print(f"First Name: {admin.first_name}")
                    print(f"Last Name: {admin.last_name}")
                    # Display other customer properties as needed
                else:
                    print(f"Customer with ID {admin_id} not found.")

            except DatabaseConnectionException as e:
                print(f"Error connecting to the database: {str(e)}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

            finally:
                # Close the cursor and connection in the finally block to ensure they are closed even if an exception occurs
                if cursor:
                    cursor.close()
                if connection:
                    connection.close()
        except Exception as e:
            print(f"An error occurred: {str(e)}")


    def get_admin_by_username(self):
        username = input("Enter Admin Username: ")
        try:
            admin = self.admin_service.get_admin_by_username(username)
            print("Admin Details:")
            print("Admin ID : ",admin.admin_id)
            print("First Name : ", admin.first_name)
            print("Last Name : ",admin.last_name)
            print("Email ",admin.email)
            print("Phone Number : ",admin.phone_number)
            print("Username  : ",admin.username)
            print("Password : ",admin.password)
            print("Role : ",admin.role)
            print("Join Date : ",admin.join_date)

        except InvalidInputException as e:
            print(f"Error: {e}")


    def register_admin(self):
        # Get customer data from user input
        admin_id = input("Enter Admin ID: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email: ")
        phone_number = input("Enter Phone Number: ")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        role = input("Enter Role: ")
        join_date=input("Enter Join Date:")

        try:

            admin_data = {
                "admin_id":admin_id,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone_number": phone_number,
                "username": username,
                "password": password,
                "role": role,
                "join_date":join_date

            }
            admin_id = self.admin_service.register_admin(admin_data)
            print(f"Admin registered successfully with ID: {admin_id}")
        except InvalidInputException as e:
            print(f"Error: {e}")


    def update_admin(self):
        try:
            # Get admin data from user input
            admin_id = int(input("Enter Admin ID to update: "))
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            email = input("Enter Email: ")
            phone_number = input("Enter Phone Number: ")
            role = input("Enter Role: ")

            # Update the admin
            admin_data = {
                "admin_id": admin_id,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone_number": phone_number,
                "role": role
            }
            self.admin_service.update_admin(admin_data)
            print("Admin updated successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid Admin ID.")
        except InvalidInputException as e:
            print(f"Error: {e}")


    def delete_admin(self):
        try:
            # Get admin ID from user input
            admin_id = int(input("Enter Admin ID to delete: "))
            self.admin_service.delete_admin(admin_id)
            print("Admin deleted successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid Customer ID.")
        except InvalidInputException as e:
            print(f"Error: {e}")




if __name__ == "__main__":
    car_connect_system = MainModule()
    car_connect_system.run_menu()
