from datetime import datetime
datetime.now()
from Exception.Exception import InvalidDataException


class Orders:
    def __init__(self, OrderID, CustomerID, OrderDate):
        self._OrderID = OrderID
        self._CustomerID = CustomerID
        self._OrderDate = OrderDate
        self._TotalAmount = 0

    def __init__(self, db_connector):
        self._db_connector = db_connector
    @property
    def OrderID(self):
        return self._OrderID
    @OrderID.setter
    def OrderID(self,new_OrderID):
        self._OrderID=new_OrderID

    @property
    def CustomerID(self):
        return self._CustomerID
    @CustomerID.setter
    def Customer(self,new_CustomerID):
        self._CustomerID=new_CustomerID
    @property
    def OrderDate(self):
        return self.OrderDate
    @OrderDate.setter
    def OrderDate(self,new_OrderDate):
        self._OrderDate=new_OrderDate
    @property
    def TotalAmount(self):
        return self.TotalAmount
    @TotalAmount.setter
    def TotalAmount(self, new_Totalamount):

        if isinstance( new_Totalamount, (int, float)) and  new_Totalamount >= 0:
            self.TotalAmount =  new_Totalamount
        else:
            raise InvalidDataException("Invalid total amount value.")

    def Calculate_Total_Amount(self, OrderID):
        try:
            self._db_connector.open_connection()

            query_check_order = "SELECT * FROM Orders WHERE OrderID = %s"
            values = (OrderID,)

            with self._db_connector.connection.cursor() as cursor_check_order:
                cursor_check_order.execute(query_check_order, values)
                order_exists = cursor_check_order.fetchone()

            if not order_exists:
                print("Order ID not found.")
                return

            calculate_total_amount = """
                SELECT SUM(Products.Price * OrderDetails.Quantity)
                FROM OrderDetails
                JOIN Products ON OrderDetails.ProductID = Products.ProductID
                WHERE OrderDetails.OrderID = %s
            """
            values1 = (OrderID,)

            with self._db_connector.connection.cursor() as cursor_calculate_total_amount:
                cursor_calculate_total_amount.execute(calculate_total_amount, values1)
                total_amount = cursor_calculate_total_amount.fetchone()[0]

            print(f"Total amount for OrderID {OrderID}: {total_amount:.2f}")

        except Exception as e:
            print(f"Error calculating total amount: {e}")

        finally:
            self._db_connector.close_connection()

    def get_Order_Details(self, OrderID):
        try:
            self._db_connector.open_connection()

            query = "SELECT * FROM orders WHERE OrderID=%s"
            values = (OrderID,)

            self._db_connector.cursor.execute(query, values)

            order_details = self._db_connector.cursor.fetchone()

            if order_details:
                print("Order Details:")
                print(f"Order ID:{order_details[0]}")
                print(f"Customer ID:{order_details[1]}")
                print(f"Order Date: {order_details[2]}")
                print(f"Total Amount: {order_details[3]}")

            else:
                print("Order Id not found.")

        except Exception as e:
            print(f"Error getting Order details: {e}")

        finally:
            self._db_connector.close_connection()

    def place_order(self, OrderID, OrderDetailID, CustomerID, ProductID, Quantity):
        try:
            self._db_connector.open_connection()
            query = "INSERT INTO Orders (OrderID,CustomerID, OrderDate) VALUES (%s, %s,%s)"
            values = (OrderID, CustomerID, datetime.now())

            with self._db_connector.connection.cursor() as cursor1:
                cursor1.execute(query, values)

            query_details = "INSERT INTO OrderDetails (OrderdetailID,OrderID, ProductID, Quantity) VALUES (%s, %s, %s,%s)"
            values_details = (OrderDetailID, OrderID, ProductID, Quantity)

            with self._db_connector.connection.cursor() as cursor2:
                cursor2.execute(query_details, values_details)

            query_update_inventory = "UPDATE Inventory SET QuantityInStock = QuantityInStock - %s WHERE ProductID = %s"
            values_update_inventory = (Quantity, ProductID)
            with self._db_connector.connection.cursor() as cursor3:
                cursor3.execute(query_update_inventory, values_update_inventory)

            query_total_amount = """
                       SELECT SUM(Products.Price * OrderDetails.Quantity)
                       FROM OrderDetails
                       JOIN Products ON OrderDetails.ProductID = Products.ProductID
                       WHERE OrderDetails.OrderID = %s
                   """
            with self._db_connector.connection.cursor() as cursor4:
                cursor4.execute(query_total_amount, (OrderID,))
                total_amount = cursor4.fetchone()[0]

            query_update_total_amount = "UPDATE Orders SET TotalAmount = %s WHERE OrderID = %s"
            values_update_total_amount = (total_amount, OrderID)
            with self._db_connector.connection.cursor() as cursor5:
                cursor5.execute(query_update_total_amount, values_update_total_amount)
            self._db_connector.connection.commit()
            print(
                f"Order placed successfully. OrderID: {OrderID} OrderTotal :{total_amount} and inventory updated with avaialble stock")
        except Exception as e:
            print(f"Error placing order: {e}")
        finally:
            self._db_connector.close_connection()

    def updateOrderStatus(self):
        # no status table in database schema
        pass

    def cancelOrder(self):
        # no status table in database schema
        pass