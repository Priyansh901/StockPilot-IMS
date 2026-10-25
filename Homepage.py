from Products import *
from Supplier import *

class Homepage(Products, Supplier):
    
    def Menu(self):
        while True:
            choose = input(
                "Choose:\n1. Products Info\n2. Suppliers Info\n3. Customer Info\n4. Purchase Info\n5. Exit\nEnter your choice: "
            ).title()

            if choose in ["1", "Products Info"]:
                self.Product_Menu()

            elif choose in ["2", "Suppliers Info"]:
                self.Supplier_Menu()

            elif choose in ["3", "Customer Info"]:
                print("Customer Info module is under development.")

            elif choose in ["4", "Purchase Info"]:
                print("Purchase Info module is under development.")

            elif choose in ["5", "Exit"]:
                print("Thank you for using Inventory Management System. Goodbye!")
                break

            else:
                print("Invalid Choice, Please try again.")
                continue