
from Exception.Exception import InvalidDataException


class Customers:
    def __init__(self,CustomerId,FirstName,LastName,Email,Phone,Address):
        self._CustomerId=CustomerId
        self._FirstName=FirstName
        self._LastName=LastName
        self._Email=Email
        self._Phone=Phone
        self._Address=Address

    def __init__(self,db_connector):
        self._db_connector = db_connector
    @property
    def CustomerId(self):
        return self._CustomerId
    @CustomerId.setter
    def CustomerId(self, new_customer_id):
        self._CustomerId = new_customer_id
    @property
    def FirstName(self):
        return self._FirstName
    @FirstName.setter
    def FirstName(self,new_FirstName):
        self._FirstName=new_FirstName
    @property
    def LastName(self):
        return self._LastName

    @LastName.setter
    def LastName(self, new_LastName):
        self._LastName = new_LastName
    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self,new_Email):
        if "@" in new_Email and "." in new_Email:
            self._Email =new_Email
        else:
            raise InvalidDataException("Invalid email format.")

    @property
    def Phone(self):
        return self._Phone
    @Phone.setter
    def Phone(self, new_Phone):
        if len(new_Phone) == 10 and new_Phone.isdigit():
            self._Phone = new_Phone
        else:
            raise InvalidDataException("Invalid phone number format.")

    @property
    def Address(self):
        return self._Address
    @Address.setter
    def Address(self, new_Address):
        if isinstance(new_Address, str):
            self._Address = new_Address
        else:
            raise InvalidDataException("Invalid address format")

    def create_customer(self, CustomerId, FirstName, LastName, Email, Phone, Address):
        try:
            self._db_connector.open_connection()
            cursor = self._db_connector.connection.cursor()

            cursor.execute("SELECT * FROM customers WHERE Email = %s", (Email,))
            existing_customer = cursor.fetchone()

            if existing_customer:
                print("Error: Email address is already in use.")
            else:
                cursor.execute(
                    "INSERT INTO customers (CustomerId,FirstName,LastName, Email, Phone,Address) VALUES (%s, %s, %s,%s,%s,%s)",
                    (CustomerId, FirstName, LastName, Email, Phone, Address))
                self._db_connector.connection.commit()
                print("Customer created successfully")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            if cursor:
                cursor.close()
            self._db_connector.close_connection()

    def calculate_Total_Orders(self, Customerid):
        try:
            self._db_connector.open_connection()
            query = """ SELECT COUNT(OrderID) AS TotalOrders FROM Orders
                        WHERE Customerid = %s"""
            values = (Customerid,)
            self._db_connector.cursor.execute(query, values)
            result = self._db_connector.cursor.fetchone()

            if result:
                total_orders = result[0]
                print(f"Total Orders for Customer {Customerid}: {total_orders}")
            else:
                print("No orders found for this customer")

        except Exception as e:
            print(f"Error calculating total orders: {e}")
        finally:
            self._db_connector.close_connection()

    def get_Customer_Details(self, Customerid):
        try:
            self._db_connector.open_connection()

            query = "SELECT * FROM customers WHERE CustomerId=%s"
            values = (Customerid,)

            self._db_connector.cursor.execute(query, values)

            customer_details = self._db_connector.cursor.fetchone()

            if customer_details:
                print("Customer Details:")
                print(f"Customer ID:{customer_details[0]}")
                print(f"First Name: {customer_details[1]}")
                print(f"Last Name: {customer_details[2]}")
                print(f"Email: {customer_details[3]}")
                print(f"Phone: {customer_details[4]}")
                print(f"Address: {customer_details[5]}")
            else:
                print("Customer not found.")

        except Exception as e:
            print(f"Error getting customer details: {e}")

        finally:
            self._db_connector.close_connection()

    def update_customer_Info(self, Customerid, new_Email, new_Phone, new_Address):
        try:
            self._db_connector.open_connection()

            query = "UPDATE customers SET Email=%s,Phone=%s, Address=%s WHERE Customerid=%s"
            values = (new_Email, new_Phone, new_Address, Customerid)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)
            self._db_connector.connection.commit()
            print("Customer account updated sucessfully")
        except Exception as e:
            print(f"Error updating customer account :{e}")
        finally:
            self._db_connector.close_connection()