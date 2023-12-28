from util.DatabaseConnector import DatabaseConnector
from Entity.Customers import Customers
from Entity.Products import Products
from Entity.Orders import Orders
from Entity.OrderDetails import OrderDetails
from Entity.Inventory import Inventory

db_connector = DatabaseConnector(host ="localhost", database ="TechShop", user ="root", password ="pradip")
db_connector.open_connection()


customer1= Customers(db_connector)

#customer1.create_customer("113","KL","Rahul", "klrahul@gmail.com", "1234587590","Patana")
#customer1.update_customer_Info("112", "kohali@gmail.com", "987654321", "Sambhajinagar")
#customer1.get_Customer_Details(1)
#customer1.calculate_Total_Orders(8)


product1=Products(db_connector)

#product1.get_product_details(105)
#product1.update_Product_Info("101","Dolby 5.2.0 atmos ",2500)
#product1.is_Product_InStock(109)


orders1=Orders(db_connector)

#orders1.get_Order_Details(207)
#orders1.Calculate_Total_Amount(203)
#orders1.place_order(211,399,5,107,9)


orderdetails1=OrderDetails(db_connector)
#orderdetails1.get_OrderDetail_Info(304)
#orderdetails1.update_Quantity(308,25)
#orderdetails1.Calculate_Subtotal(308)


inventory1=Inventory(db_connector)

#inventory1.Get_Product(403)
#inventory1.get_QuantityInStock(401)
#inventory1.add_To_Inventory(20,401)
#inventory1.remove_From_Inventory(20,401)
#inventory1.update_Stock_Quantity(100,404)
#inventory1.Is_Product_Available(20,404)
#inventory1.Get_InventoryValue()
#inventory1.List_LowStock_Products(30)
#inventory1.List_OutOf_StockProducts()
inventory1.List_All_Products()

db_connector.close_connection()