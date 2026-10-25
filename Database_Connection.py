import pymysql
 
Connection = pymysql.connect(user = "root" , password = "priyansh@907994" , host = "localhost" , database = "Inventory_DB")
print("Succesfully connected")
 
Cursor = Connection.cursor()
print("Cursor Created Successfully")