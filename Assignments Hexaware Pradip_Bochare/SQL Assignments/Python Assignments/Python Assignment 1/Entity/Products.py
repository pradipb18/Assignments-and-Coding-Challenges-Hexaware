from Exception.Exception import InvalidDataException
class Products:
    def __init__(self, ProductID, ProductName, Description, Price):
        self._ProductID=ProductID
        self._ProductName=ProductName
        self._Description=Description
        self._Price=Price

    def __init__(self, db_connector):
        self._db_connector = db_connector
    @property
    def ProductID(self):
        return self._ProductID

    @ProductID.setter
    def ProductID(self,new_ProductID):
        self._ProductID=new_ProductID
    @property
    def ProductName(self):
        return self.ProductName

    @ProductName.setter
    def ProductName(self,new_ProductName):
        self._ProductName=new_ProductName
    @property
    def Description(self):
        return self.Description

    @Description.setter
    def Description(self, new_Description):
        self._Description = new_Description
    @property
    def Price(self):
        return self.Price
    @Price.setter
    def Price(self,new_Price):
        if new_Price >= 0:
            self.Price = new_Price
        else:
            raise InvalidDataException("Price should be greater than 0")

    def get_product_details(self, ProductID):
        try:
            self._db_connector.open_connection()

            query = "SELECT * FROM products WHERE ProductID=%s"
            values = (ProductID,)

            self._db_connector.cursor.execute(query, values)

            product_details = self._db_connector.cursor.fetchone()

            if product_details:
                print("Product Details:")
                print(f"Product ID:{product_details[0]}")
                print(f"Product Name: {product_details[1]}")
                print(f"Description : {product_details[2]}")
                print(f"Price: {product_details[3]}")

            else:
                print("Product Id not found.")

        except Exception as e:
            print(f"Error getting Product details: {e}")

        finally:
            self._db_connector.close_connection()

    def update_Product_Info(self, ProductID, new_Description, new_Price):
        try:
            self._db_connector.open_connection()
            query = "UPDATE Products SET Description=%s,Price=%s WHERE ProductID=%s"
            values = (new_Description, new_Price, ProductID)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)
            self._db_connector.connection.commit()
            print("Product Details updated sucessfully")

        except Exception as e:
            print(f"Error updating Product Details :{e}")

        finally:
            self._db_connector.close_connection()

    def is_Product_InStock(self, ProductID):
        try:
            self._db_connector.open_connection()
            query = "SELECT QuantityInStock FROM Inventory WHERE ProductID = %s"
            values = (ProductID,)

            self._db_connector.cursor.execute(query, values)
            quantity_in_stock = self._db_connector.cursor.fetchone()

            if quantity_in_stock[0] > 0:
                print("Product is in stock and stockquantity is", quantity_in_stock[0])
            else:
                print("Product is not in stock")

        except Exception as e:
            print(f"Error checking product stock: {e}")
            return False
        finally:
            self._db_connector.close_connection()