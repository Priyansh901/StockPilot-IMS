from Database_Connection import Connection, Cursor

class Products:

    def add_product(self):
        while True:
            try:
                Product_Name = input("Enter Product name - ").strip()
                Category = input("Enter Category - ").strip()
                Purchase_Price = float(input("Enter Purchase Price - "))
                Selling_Price = float(input("Enter Selling Price - "))
                Stock = int(input("Enter Stock - "))

                Query = "INSERT INTO Products (Product_Name, Category, Purchase_Price, Selling_Price, Stock) VALUES (%s, %s, %s, %s, %s)"
                Cursor.execute(Query, (Product_Name, Category, Purchase_Price, Selling_Price, Stock))
                Connection.commit()
                print("Added Successfully")

            except Exception as E:
                print(E)
            else:
                while True:
                    choose = input("Choose:\n1. Add Another Product\n2. Done\nEnter Your Choice: ").title()

                    if choose in ["1", "Add Another Product"]:
                        break
                    elif choose in ["2", "Done"]:
                        return
                    else:
                        print("Invalid Choice")
                        continue

    def Del_Product(self):
        while True:
            try:
                Product_Name = input("Enter Product Name: ").strip()

                Query = "SELECT * FROM Products WHERE Product_Name = %s"
                Cursor.execute(Query, (Product_Name,))
                Info = Cursor.fetchall()

                if len(Info) == 0:
                    print("Product Not Found, Please Enter Correct Product Name")
                    continue
                else:
                    Line_1 = "Here is Your Related Search"
                    print(Line_1.center(20, "-"))

                    for info in Info:
                        print(info)

                    Product_ID = int(input("Enter Product Id which you want to Delete: "))

                    Query = "DELETE FROM Products WHERE Product_ID = %s"
                    Cursor.execute(Query, (Product_ID,))
                    Connection.commit()

                    if Cursor.rowcount == 0:
                        print("Wrong Product ID, Please Enter Correct Product Id")
                        continue
                    else:
                        print("Deleted Successfully")

            except Exception as E:
                print(E)
            else:
                while True:
                    choose = input("Choose:\n1. Delete Another Product\n2. Done\nEnter Your Choice: ").title()

                    if choose in ["1", "Delete Another Product"]:
                        break
                    elif choose in ["2", "Done"]:
                        return
                    else:
                        print("Invalid Choice")
                        continue

    def View_Products_info(self):
        try:
            Query = "SELECT * FROM Products"
            Cursor.execute(Query)
            Info = Cursor.fetchall()

            Line_2 = "Products Information"
            print(Line_2.center(20, "-"))

            if len(Info) == 0:
                print("No Data")
                return

            for info in Info:
                print(info)

        except Exception as E:
            print(E)
        else:
            while True:
                choose = input("Choose:\n1. Done\nEnter Your choice: ").title()

                if choose in ["1", "Done"]:
                    return
                else:
                    print("Invalid Choice")
                    continue

    def Search_Product(self):
        while True:
            try:
                Product_Name = input("Enter Product name - ").strip()

                Query = "SELECT * FROM Products WHERE Product_Name = %s"
                Cursor.execute(Query, (Product_Name,))
                Info = Cursor.fetchall()

                Line_3 = "Here is Your Related Search"
                print(Line_3.center(20, "-"))

                if len(Info) == 0:
                    print("Record Not Found, Please Enter Correct Product Name")
                    continue

                for info in Info:
                    print(info)

            except Exception as E:
                print(E)
            else:
                while True:
                    choose = input("Choose:\n1. Search Another Product\n2. Done\nEnter Your Choice: ").title()

                    if choose in ["1", "Search Another Product"]:
                        break
                    elif choose in ["2", "Done"]:
                        return
                    else:
                        print("Invalid Choice")
                        continue

    def Update_Product(self):
        while True:
            try:
                choose_Update_Options = input(
                    "Choose:\n1. Update Purchase Price\n2. Update Selling Price\n3. Update Stock\n4. Back To Product Menu\nEnter your choice: "
                ).title()

                if choose_Update_Options in ["1", "Update Purchase Price"]:
                    self.Update_Purchase_Price()
                elif choose_Update_Options in ["2", "Update Selling Price"]:
                    self.Update_Selling_Price()
                elif choose_Update_Options in ["3", "Update Stock"]:
                    self.Update_Stock()
                elif choose_Update_Options in ["4", "Back To Product Menu"]:
                    return
                else:
                    print("Invalid Choice")
                    continue

            except Exception as E:
                print(E)

    def Update_Purchase_Price(self):
        while True:
            try:
                Product_Name = input("Enter Product Name: ").strip()

                Query = "SELECT * FROM Products WHERE Product_Name = %s"
                Cursor.execute(Query, (Product_Name,))
                Info = Cursor.fetchall()

                if len(Info) == 0:
                    print("Product Not found, Please Type Correct Product Name")
                    continue

                Line_4 = "Here is Your Related Search"
                print(Line_4.center(20, "-"))

                for info in Info:
                    print(info)

                Product_ID = int(input("Enter Product Id of which you want to Update Purchase Price: "))
                New_Purchase_Price = float(input("Enter Updated Purchase Price - "))

                Query = "UPDATE Products SET Purchase_Price = %s WHERE Product_ID = %s"
                Cursor.execute(Query, (New_Purchase_Price, Product_ID))
                Connection.commit()

                if Cursor.rowcount == 0:
                    print("Invalid Product Id, Please Enter Correct Product Id")
                    continue

                print("Purchase Price Updated Successfully")
                Line_5 = "Updated Purchase Price"
                print(Line_5.center(20, "-"))

                Query = "SELECT * FROM Products WHERE Product_ID = %s"
                Cursor.execute(Query, (Product_ID,))
                updated_info = Cursor.fetchone()

                for info in updated_info:
                    print(info)

            except Exception as E:
                print(E)
            else:
                while True:
                    choose = input("Choose:\n1. Update Another Purchase Price\n2. Done\nEnter Your Choice: ").title()

                    if choose in ["1", "Update Another Purchase Price"]:
                        break
                    elif choose in ["2", "Done"]:
                        return
                    else:
                        print("Invalid Choice")
                        continue

    def Update_Selling_Price(self):
        while True:
            try:
                Product_Name = input("Enter Product Name: ").strip()

                Query = "SELECT * FROM Products WHERE Product_Name = %s"
                Cursor.execute(Query, (Product_Name,))
                Info = Cursor.fetchall()

                if len(Info) == 0:
                    print("Product Not found, Please Type Correct Product name")
                    continue

                Line_6 = "Here is Your Related Search"
                print(Line_6.center(20, "-"))

                for info in Info:
                    print(info)

                Product_ID = int(input("Enter Product Id of which you want to Update Selling Price: "))
                New_Selling_Price = float(input("Enter Updated Selling Price - "))

                Query = "UPDATE Products SET Selling_Price = %s WHERE Product_ID = %s"
                Cursor.execute(Query, (New_Selling_Price, Product_ID))
                Connection.commit()

                if Cursor.rowcount == 0:
                    print("Invalid Product Id, Please Enter Correct Product ID")
                    continue

                print("Selling Price Updated Successfully")
                Line_7 = "Updated Selling Price"
                print(Line_7.center(20, "-"))

                Query = "SELECT * FROM Products WHERE Product_ID = %s"
                Cursor.execute(Query, (Product_ID,))
                updated_info = Cursor.fetchone()

                for info in updated_info:
                    print(info)

            except Exception as E:
                print(E)
            else:
                while True:
                    choose = input("Choose:\n1. Update Another Selling Price\n2. Done\nEnter Your Choice: ").title()

                    if choose in ["1", "Update Another Selling Price"]:
                        break
                    elif choose in ["2", "Done"]:
                        return
                    else:
                        print("Invalid Choice")
                        continue

    def Update_Stock(self):
        while True:
            try:
                Product_Name = input("Enter Product Name: ").strip()

                Query = "SELECT * FROM Products WHERE Product_Name = %s"
                Cursor.execute(Query, (Product_Name,))
                Info = Cursor.fetchall()

                if len(Info) == 0:
                    print("Product Not found, Please Type Correct Product name")
                    continue

                Line_8 = "Here is Your Related Search"
                print(Line_8.center(20, "-"))

                for info in Info:
                    print(info)

                Product_ID = int(input("Enter Product Id of which you want to Update Stock: "))
                New_Stock = float(input("Enter Updated Stock - "))

                Query = "UPDATE Products SET Stock = %s WHERE Product_ID = %s"
                Cursor.execute(Query, (New_Stock, Product_ID))
                Connection.commit()

                if Cursor.rowcount == 0:
                    print("Invalid Product Id, Please Enter Correct Product ID")
                    continue

                print("Stock Updated Successfully")
                Line_9 = "Updated Stock"
                print(Line_9.center(20, "-"))

                Query = "SELECT * FROM Products WHERE Product_ID = %s"
                Cursor.execute(Query, (Product_ID,))
                updated_info = Cursor.fetchone()

                for info in updated_info:
                    print(info)

            except Exception as E:
                print(E)
            else:
                while True:
                    choose = input("Choose:\n1. Update Another Stock\n2. Done\nEnter Your Choice: ").title()

                    if choose in ["1", "Update Another Stock"]:
                        break
                    elif choose in ["2", "Done"]:
                        return
                    else:
                        print("Invalid Choice")
                        continue

    def Product_Menu(self):
        while True:
            choose_products_option = input(
                "Choose:\n1. Add Product\n2. Delete Product\n3. View All Products\n4. Search Product\n5. Update Product\n6. Back To Homepage\nEnter your choice: "
            ).title()

            if choose_products_option in ["1", "Add Product"]:
                self.add_product()
            elif choose_products_option in ["2", "Delete Product"]:
                self.Del_Product()
            elif choose_products_option in ["3", "View All Products"]:
                self.View_Products_info()
            elif choose_products_option in ["4", "Search Product"]:
                self.Search_Product()
            elif choose_products_option in ["5", "Update Product"]:
                self.Update_Product()
            elif choose_products_option in ["6", "Back To Homepage"]:
                return
            else:
                print("Invalid Choice")
                continue