
from datetime import datetime

from Exception.Exception import InvalidDataException,InsufficientStockException


class Inventory:
    def __init__(self, InventoryID, ProductID, QuantityInStock, LastStockUpdate):
        self._InventoryID = InventoryID
        self._ProductID = ProductID
        self._QuantityInStock = QuantityInStock
        self._LastStockUpdate = LastStockUpdate

    def __init__(self,db_connector):
        self._db_connector = db_connector

    @property
    def InventoryID(self):
        return self._InventoryID
    @InventoryID.setter
    def InventoryID(self,new_InventoryID):
        self._InventoryID=new_InventoryID
    @property
    def ProductID(self):
        return self._ProductID
    @ProductID.setter
    def ProductID(self,new_ProductID):
        self._ProductID=new_ProductID
    @property
    def QuantityInStock(self):
        return self._QuantityInStock
    @QuantityInStock.setter
    def QuantityInStock(self,new_QuantityInStock):
        if new_QuantityInStock >= 0:
            self._QuantityInStock = new_QuantityInStock
        else:
            raise InvalidDataException("Quantity in stock must be non-negative")
    @property
    def LastStockUpdate(self):
        return self._LastStockUpdate
    @LastStockUpdate.setter
    def LastStockUpdate(self,new_LastStockUpdate):
        self._LastStockUpdate=new_LastStockUpdate

    def Get_Product(self, InventoryID):
        try:
            self._db_connector.open_connection()
            query = ("SELECT P.ProductID, P.ProductName, P.Description, P.Price FROM Products P"
                     " INNER JOIN Inventory I ON P.ProductID = I.ProductID WHERE I.InventoryID = %s")
            values = (InventoryID,)

            with self._db_connector.cursor as cursor:
                cursor.execute(query, values)
                product_data = cursor.fetchone()

            if product_data:
                product_id, product_name, description, price = product_data
                print(
                    f"Product ID: {product_id}, Product Name: {product_name}, Description: {description}, Price: rs{price}")
            else:
                print("Product not found in the inventory.")

        except Exception as e:
            print(f"Error getting product: {e}")

        finally:
            self._db_connector.close_connection()

    def get_QuantityInStock(self, InventoryID):
        try:
            self._db_connector.open_connection()
            query = "SELECT QuantityInStock FROM Inventory WHERE InventoryID = %s"
            values = (InventoryID,)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)
                quantity_in_stock = cursor.fetchone()

            if quantity_in_stock is not None:
                return quantity_in_stock[0]
            else:
                return 0

        except Exception as e:
            print(f"Error getting quantity in stock: {e}")
            return 0

    def add_To_Inventory(self, quantity_to_add, InventoryID):
        try:
            self._db_connector.open_connection()
            current_quantity = self.get_QuantityInStock(InventoryID)
            new_Quantity = current_quantity + quantity_to_add
            query = "UPDATE Inventory SET QuantityInStock=%s, LastStockUpdate=%s WHERE InventoryID=%s"
            values = (new_Quantity, datetime.now(), InventoryID)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)

            self._db_connector.connection.commit()
            print(f"{quantity_to_add} units added to inventory successfully.")

        except Exception as e:
            print(f"Error adding to inventory: {e}")

        finally:
            self._db_connector.close_connection()

    def remove_From_Inventory(self, quantity_to_remove, InventoryID):
        try:
            self._db_connector.open_connection()
            current_quantity = self.get_QuantityInStock(InventoryID)
            if (current_quantity >= quantity_to_remove):
                new_Quantity = current_quantity - quantity_to_remove
                query = "UPDATE Inventory SET QuantityInStock=%s, LastStockUpdate=%s WHERE InventoryID=%s"
                values = (new_Quantity, datetime.now(), InventoryID)

                with self._db_connector.connection.cursor() as cursor:
                    cursor.execute(query, values)

                self._db_connector.connection.commit()
                print(f"{quantity_to_remove} units removed from inventory successfully.")
            else:
                raise InsufficientStockException("Insufficient stock for the specified quantity.")

        except Exception as e:
            print(f"Error removing to inventory: {e}")

        finally:
            self._db_connector.close_connection()

    def update_Stock_Quantity(self, new_Quantity, InventoryID):
        try:
            self._db_connector.open_connection()

            query = "UPDATE Inventory SET QuantityInStock=%s, LastStockUpdate=%s WHERE InventoryID=%s"
            values = (new_Quantity, datetime.now(), InventoryID)

            with self._db_connector.cursor as cursor:
                cursor.execute(query, values)

            self._db_connector.connection.commit()
            print(f"Stock quantity updated to {new_Quantity} successfully.")

        except Exception as e:
            print(f"Error updating stock quantity: {e}")

        finally:
            self._db_connector.close_connection()

    def Is_Product_Available(self, quantity_to_check, InventoryID):
        try:
            self._db_connector.open_connection()
            query = "SELECT QuantityInStock FROM Inventory WHERE InventoryID = %s"
            values = (InventoryID,)
            with self._db_connector.cursor as cursor:
                cursor.execute(query, values)
                current_quantity = cursor.fetchone()
            if current_quantity is not None and current_quantity[0] >= quantity_to_check:
                print(f"Product is available in sufficient quantity: {current_quantity[0]} units.")
                return True
            else:
                print("Product is not available in sufficient quantity.")
                return False
        except Exception as e:
            print(f"Error checking product availability: {e}")
            return False

        finally:
            self._db_connector.close_connection()

    def Get_InventoryValue(self):
        try:
            self._db_connector.open_connection()
            query = "SELECT P.ProductID, P.Price, I.QuantityInStock FROM Products P INNER JOIN Inventory I ON P.ProductID = I.ProductID"
            with self._db_connector.cursor as cursor:
                cursor.execute(query)
                products_data = cursor.fetchall()
            if products_data:
                total_value = 0
                for product in products_data:
                    product_id, price, quantity = product
                    total_value += price * quantity
                print(f"Total value of the inventory: rs{total_value}")
            else:
                print("No products found in the inventory.")
        except Exception as e:
            print(f"Error calculating inventory value: {e}")
        finally:
            self._db_connector.close_connection()

    def List_LowStock_Products(self, threshold):
        try:
            self._db_connector.open_connection()
            query = "SELECT ProductID, QuantityInStock FROM Inventory WHERE QuantityInStock < %s"
            values = (threshold,)
            with self._db_connector.cursor as cursor:
                cursor.execute(query, values)
                low_stock_products = cursor.fetchall()
            if low_stock_products:
                print("Low stock products:")
                for product in low_stock_products:
                    print(f"ProductID: {product[0]}, QuantityInStock: {product[1]}")
            else:
                print("No products with quantities below the specified threshold.")

        except Exception as e:
            print(f"Error listing low stock products: {e}")

        finally:
            self._db_connector.close_connection()

    def List_OutOf_StockProducts(self):
        try:
            self._db_connector.open_connection()
            query = "SELECT ProductID FROM Inventory WHERE QuantityInStock <= 0"
            with self._db_connector.cursor as cursor:
                cursor.execute(query)
                out_of_stock_products = cursor.fetchall()

            if out_of_stock_products:
                print("Out of stock products:")
                for product_id in out_of_stock_products:
                    print(f"ProductID: {product_id[0]}")
            else:
                print("No products are currently out of stock.")

        except Exception as e:
            print(f"Error listing out of stock products: {e}")

        finally:
            self._db_connector.close_connection()

    def List_All_Products(self):
        try:
            self._db_connector.open_connection()
            query = "SELECT ProductID, QuantityInStock FROM Inventory"
            with self._db_connector.cursor as cursor:
                cursor.execute(query)
                all_products = cursor.fetchall()
            if all_products:
                print("All products in the inventory:")
                for product in all_products:
                    print(f"ProductID: {product[0]}, QuantityInStock: {product[1]}")
            else:
                print("No products found in the inventory.")
        except Exception as e:
            print(f"Error listing all products: {e}")
        finally:
            self._db_connector.close_connection()