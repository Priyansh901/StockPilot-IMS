from Database_Connection import Connection , Cursor

class Products:
    
    def add_product(self):

        while True:
            
            try: 
                
                Product_Name = input("Enter Product name - ").strip()
                Category = input("Enter Category - ").strip()
                Purchase_Price = float(input("Enter Purchase Price - "))
                Selling_Price = float(input("Enter Selling Price - "))
                Stock = int(input("Enter Stock - "))

                Query = "insert into Products(Product_Name , Category , Purchase_Price , Selling_Price , Stock) values(%s,%s,%s,%s,%s)"
                Cursor.execute(Query , (Product_Name , Category , Purchase_Price , Selling_Price , Stock))
                Connection.commit()
                print("Added Successfully")

            except Exception as E:
                print(E)

            else:

                while True:
                    
                    choose = input("Choose :\n1. Add Another Product\n2. Done\n Enter Your Choice :").title()

                    if(choose == "Add Another Product"):
                        break
                        
                    elif(choose == "Done"):
                        return

                    else:
                        print("Invalid Choice")
                        continue
            
    def Del_Product(self):
        
        while True:
            
            try:
                
                Product_Name =  input("Enter Product Name: ").strip()

                Query = "Select *from Products where Product_Name = %s"
                Cursor.execute(Query, (Product_Name,))
                Info = Cursor.fetchall()

                if(len(Info) == 0):
                    print("Product Not found , Please Enter Correct Product Name")
                    continue

                else:
                    Line_1 = "Here is Your Related Search"
                    print(Line_1.center(20,"-"))
                    
                    for info in Info:
                        print(info)
                        
                    Product_ID = int(input("Enter Product Id which you want to Delete: "))

                    Query = "Delete from Products where Product_ID = %s"
                    Cursor.execute(Query, (Product_ID,))
                    Connection.commit()

                    if(Cursor.rowcount == 0):
                        print("Wrong Product ID , Please Enter Correct Product Id")
                        continue
                        
                    else:
                        print("Deleted Successfully")

            except Exception as E:
                print(E)

            else:

                while True:
                    
                    choose = input("Choose :\n1. Delete Another Product\n2. Done\n Enter Your Choice :").title()

                    if(choose == "Delete Another Product"):
                        break
                    
                    elif(choose == "Done"):
                        return

                    else:
                        print("Invalid Choice")
                        continue
                
    def View_Products_info(self):
        
        try:
            
            Query = "Select*from Products"
            Cursor.execute(Query)
            Info = Cursor.fetchall()

            Line_2 = "Products Information"
            print(Line_2.center(20,"-"))

            for info in Info:
                print(info)

            if(len(Info)==0):
                print("No Data")
                return

        except Exception as E:
            print(E)

        else:

            while True:
                
                choose = input("Choose :\n Done\nEnter Your choice :").title()

                if(choose == "Done"):
                    return

                else:
                    print("Invalid Choice")
                    continue

    def Search_Product(self):

        while True:
            
            try:
                
                Product_Name = input("Enter Product name - ").strip()

                Query = "Select*from Products where Product_Name = %s"
                Cursor.execute(Query , (Product_Name,))
                Info = Cursor.fetchall()

                Line_3 = "Here is Your Related Search"
                print(Line_3.center(20,"-"))

                for info in Info:
                    print(info)

                if(len(Info) == 0):
                    print("Record Not Found , Please Enter Correct Product Name")
                    continue

            except Exception as E:
                print(E)

            else:
                choose = input("Choose :\n1. Search Another Product\n2. Done\nEnter Your Choice :").title()

                if(choose == "Search Another Product"):
                    break

                elif(choose == "Done"):
                    return

                else:
                    print("Invalid Choice")
                    continue

    def Update_Product(self):

        while True:
            
            try:
                
                def Update_Purchase_Price():
                    
                    while True:
                        
                        try:
                            
                            Product_Name =  input("Enter Product Name: ").strip()

                            Query = "Select *from Products  where Product_Name = %s"
                            Cursor.execute(Query, (Product_Name,))
                            Info = Cursor.fetchall()

                            if(len(Info) == 0):
                                print("Product Not found , pls Type Correct Product Name")
                                continue

                            else:

                                Line_4 = "Here is Your Related Search"
                                print(Line_4.center(20,"-"))

                                for info in Info:
                                    print(info)
                                    
                                Product_ID = int(input("Enter Product Id of which you want to Update Purchase Price: "))
                                New_Purchase_Price = float(input("Enter Updated Purchase Price - "))
                
                                Query = "update Products set Purchase_Price = %s where Product_ID = %s"
                                Cursor.execute(Query , (New_Purchase_Price , Product_ID))
                                Connection.commit

                                if(Cursor.rowcount == 0):
                                    print("Type Invlaid Product Id , Please Enter Correct Product Id")
                                    continue

                                else:
                                    print("Purchase Price Updated Successfully")

                                    Line_5 = "Updated Purchase Price"
                                    print(Line_5.center(20,"-"))

                                    Query = "Select *from Products where Product_ID = %s"
                                    Cursor.execute(Query, (Product_ID,))
                                    Info = Cursor.fetchone()

                                    for info in Info:
                                        print(info)
                                
                        except Exception as E:
                            print(E)

                        else:

                            while True:
                                
                                choose = input("Choose :\n1. Update Another Purchase Price\n2. Done\nEnter Your Choice :").title()

                                if(choose == "Update Another Purchase Price"):
                                    break

                                elif(choose == "Done"):
                                    return

                                else:
                                    print("Invalid Choice")
                                    continue

                def Update_Selling_Price():
                    
                    while True:
                        
                        try:
                            
                            Product_Name =  input("Enter Product Name: ").strip()

                            Query = "Select *from Products  where Product_Name = %s"
                            Cursor.execute(Query, (Product_Name,))
                            Info = Cursor.fetchall()

                            if(len(Info) == 0):
                                print("Product Not found , Please Type Correct Product name")

                            else:

                                Line_6 = "Here is Your Reated Search"
                                print(Line_6.center(20,"-"))

                                for info in Info:
                                    print(info)
                                
                                Product_ID = int(input("Enter Product Id of which you want to Update Selling Price: "))
                                New_Selling_Price = float(input("Enter Updated Selling Price - "))
                
                                Query = "update Products set Purchase_Price = %s where Product_ID = %s"
                                Cursor.execute(Query , (New_Selling_Price , Product_ID))
                                Connection.commit()

                                if(Cursor.rowcount == 0):
                                    print("Type Invlaid Product Id , Please Enter Correct Product ID")
                                    continue

                                else:
                                    print("Selling Price Updated Successfully")

                                    Line_7 = "Updated Selling Price"
                                    print(Line.center(20,"-"))
                                
                                    Query = "Select *from Products where Product_ID = %s"
                                    Cursor.execute(Query, (Product_ID,))
                                    Info = Cursor.fetchone()

                                    for info in Info:
                                        print(info)

                        except Exception as E:
                            print(E)

                        else:

                            while True:
                                
                                choose = input("Choose :\n1. Update Another Selling Price\n2. Done\nEnter Your Choice :").title()
                                
                                if(choose == "Update Another Selling Price"):
                                    break

                                elif(choose == "Done"):
                                    return

                                else:
                                    print("Invalid Choice")
                                    continue

                def Update_Stock():
                    
                    while True:
                        
                        try:
                            
                            Product_Name =  input("Enter Product Name: ").strip()
    
                            Query = "Select *from Products  where Product_Name = %s"
                            Cursor.execute(Query, (Product_Name,))
                            Info = Cursor.fetchall()

                            if(len(Info) == 0):
                                print("Product Not found , Please Type Correct Product name")
                                continue

                            else:

                                Line_8 = "Here is Your Related Search"
                                print(Line_8.center(20,"-"))

                                for info in Info:
                                    print(info)
                                
                                Product_ID = int(input("Enter Product Id of which you want to Update Stock: "))
                                New_Stock = float(input("Enter Updated Stock - "))
                
                                Query = "update Products set Stock = %s where Product_ID = %s"
                                Cursor.execute(Query , ( New_Stock , Product_Id))
                                Connection.commit()

                                if(Cursor.rowcount == 0):
                                    print("Type Invlaid Product Id , Please Enter Correct Product ID")
                                    continue

                                else:
                                    print("Stock Updated Successfully")

                                    Line_9 = "Updated Stock"
                                    print(Line_9.center(20,"-"))
                                
                                    Query = "Select *from Products where Product_ID = %s"
                                    Cursor.execute(Query, (Product_ID,))
                                    Info = Cursor.fetchone()

                                    for info in Info:
                                        print(info)

                        except Exception as E:
                            print(E)

                        else:

                            while True:
                                
                                choose = input("Choose :\n1. Update Another Stock\n2. Done\nEnter Your Choice :").title()

                                if(choose == "Update Another Stock"):
                                    break
                                    
                                elif(choose == "Done"):
                                    return

                                else:
                                    print("Invalid Choice")
                                    continue

            except Exception as E:
                 print(E)

            else:

                choose_Update_Options = input("Choose:\n1. Update Purchase Price \n2. Update Selling Price\n3. Update Stock\n4. Back To Product Menu\nEnter your choice: ").title()

                if(choose_Update_Options == "Update Purchase Price"):
                    Update_Purchase_Price()

                elif(choose_Update_Options == "Update Selling Price"):
                    Update_Selling_Price()

                elif(choose_Update_Options == "Update Stock"):
                    Update_Stock()

                elif(choose_Update_Options == "Back To Product Menu"):
                    return

                else:
                    print("Invalid Choice")
                    continue

    def Product_Menu(self):

        while True:
                
                choose_products_option = input("Choose:\n1. Add Product\n2. Delete Product\n3. View All Products\n4. Search Product \n5. Update Product \n6. Back To Homepage\nEnter your choice: ").title()

                if(choose_products_option == "Add Product"):
                    self.add_product()

                elif(choose_products_option == "Delete Product"):
                    self.Del_Product()

                elif(choose_products_option == "View All Products"):
                    self.View_Products_info()

                elif(choose_products_option == "Search Product"):
                    self.Search_Product()

                elif(choose_products_option == "Update Product"):
                    self.Update_Product()

                elif(choose_products_option == "Back to Homepage"):
                    return

                else:
                    print("Invalid Choice")
                    continue 