from Exception.Exception import InvalidDataException

class OrderDetails:
    def __init__(self, OrderDetailID, OrderID, ProductID, Quantity):
        self._OrderDetailID = OrderDetailID
        self._OrderID = OrderID
        self._ProductID = ProductID
        self._Quantity = Quantity

    def __init__(self, db_connector):
        self._db_connector = db_connector
    @property
    def OrderDetailID(self):
        return self._OrderDetailId
    @OrderDetailID.setter
    def OrderDetailID(self,new_OrderDetailID):
        self._OrderDetailID=new_OrderDetailID
    @property
    def OrderID(self):
        return self._OrderID
    @OrderID.setter
    def OrderID(self,new_OrderID):
        self._OrderID=new_OrderID

    @property
    def ProductID(self):
        return self._ProductID
    @ProductID.setter
    def ProductID(self,new_ProductID):
        self._ProductID=new_ProductID

    @property
    def Quantity(self):
        return self.Quantity

    @Quantity.setter
    def Quantity(self, new_Quantity):
        if isinstance(new_Quantity, int) and new_Quantity > 0:
            self.Quantity = new_Quantity
        else:
            raise InvalidDataException("Quantity must be a positive integer")

    def Calculate_Subtotal(self, OrderDetailID):
        try:
            self._db_connector.open_connection()
            query = "SELECT OD.Quantity, P.Price FROM Orderdetails OD INNER JOIN Products P ON OD.ProductID = P.ProductID WHERE OD.OrderDetailID = %s"
            values = (OrderDetailID,)

            with self._db_connector.cursor as cursor:
                cursor.execute(query, values)
                order_data = cursor.fetchone()

            if order_data:
                quantity, price = order_data
                subtotal = quantity * price
                print(f"Subtotal for OrderDetailID {OrderDetailID}: {subtotal}")
            else:
                print("Order detail not found.")
        except Exception as e:
            print(f"Error calculating subtotal: {e}")
        finally:
            self._db_connector.close_connection()

    def get_OrderDetail_Info(self, OrderDetailID):
        try:
            self._db_connector.open_connection()

            query = "SELECT * FROM orderdetails WHERE OrderDetailID=%s"
            values = (OrderDetailID,)

            self._db_connector.cursor.execute(query, values)

            orderdetails_details = self._db_connector.cursor.fetchone()

            if orderdetails_details:
                print("OrderDetails Details:")
                print(f"OrderDetailID:{orderdetails_details[0]}")
                print(f"OrderID:{orderdetails_details[1]}")
                print(f"ProductID: {orderdetails_details[2]}")
                print(f"Quantity: {orderdetails_details[3]}")

            else:
                print("OrderDetails Id not found.")

        except Exception as e:
            print(f"Error getting Orderdetails: {e}")

        finally:
            self._db_connector.close_connection()

    def update_Quantity(self, OrderDetailID, new_Quantity):
        try:
            self._db_connector.open_connection()
            query = "UPDATE OrderDetails SET Quantity=%s where OrderDetailID=%s"
            values = (new_Quantity, OrderDetailID)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)
            self._db_connector.connection.commit()
            print("Quantity updated sucessfully")

        except Exception as e:
            print(f"Error updating Quantity :{e}")

        finally:
            self._db_connector.close_connection()

    def AddDiscount(self, discount_amount):
        try:
            if discount_amount < 0:
                raise InvalidDataException("Invalid discount amount")
        except InvalidDataException as e:
            print(f"Discount not applied: {str(e)}")