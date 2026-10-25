from Database_Connection import Connection, Cursor
from Homepage import *

class Login(Homepage):
 
    def login(self):
        while True:
            try: 
                Username = input("Enter Username : ")
                Password = input("Enter Password : ")
                Query = "Select Username, Password from User where Username = %s and Password = %s"
                Cursor.execute(Query, (Username, Password))
                result = Cursor.fetchone()

            except Exception as E:
                print(E)

            else:
                if result:
                    print("Login successfully")
                    print("Welcome to Inventory Management System")
                    self.Menu()
                    break  # Exits the loop once login is successful
                else:
                    print("Invalid Username or Password, Please Type Correct Username and Password")