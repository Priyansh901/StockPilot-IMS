from Database_Connection import Connection, Cursor

class Supplier:

    def Add_supplier(self):
        while True:
            try:
                Supplier_Name = input("Enter Supplier Name: ").strip()
                Phone_No = input("Enter Supplier Phone Number: ").strip()
                Email_Id = input("Enter Supplier Email ID: ").strip()
                Address = input("Enter Supplier Address: ").strip() 

                Query = "INSERT INTO Supplier (Supplier_Name, Phone, Email, Address) VALUES (%s, %s, %s, %s)"
                Cursor.execute(Query, (Supplier_Name, Phone_No, Email_Id, Address))
                Connection.commit()
                
                print("Added Successfully")

            except Exception as E:
                print(E)
            else:
                while True:
                    choose = input("Choose:\n1. Add Another Supplier\n2. Done\nEnter your choice: ").title()

                    if choose in ["1", "Add Another Supplier"]:
                        break
                    elif choose in ["2", "Done"]:
                        return
                    else:
                        print("Invalid Choice")
                        continue

    def Del_Supplier(self):
        while True:
            try:
                Supplier_Name = input("Enter Supplier Name: ").strip()

                Query = "SELECT * FROM Supplier WHERE Supplier_Name = %s"
                Cursor.execute(Query, (Supplier_Name,))
                Info = Cursor.fetchall()

                if len(Info) == 0:
                    print("Supplier Not Found, Please Enter Correct Supplier Name")
                    continue
                else:
                    Line_1 = "Here is Your Related Search"
                    print(Line_1.center(20, "-"))
                    
                    for info in Info:
                        print(info)
                        
                    Supplier_ID = int(input("Enter Supplier Id which you want to Delete: "))

                    Query = "DELETE FROM Supplier WHERE Supplier_ID = %s"
                    Cursor.execute(Query, (Supplier_ID,))
                    Connection.commit()

                    if Cursor.rowcount == 0:
                        print("Wrong Supplier ID, Please Type Correct Supplier ID")
                        continue
                    else:
                        print("Deleted Successfully")

            except Exception as E:
                print(E)
            else:
                while True:
                    choose = input("Choose:\n1. Delete Another Supplier\n2. Done\nEnter your choice: ").title()

                    if choose in ["1", "Delete Another Supplier"]:
                        break
                    elif choose in ["2", "Done"]:
                        return
                    else:
                        print("Invalid Choice")
                        continue

    def View_Supplier_info(self):
        try:
            Query = "SELECT * FROM Supplier"
            Cursor.execute(Query)
            Info = Cursor.fetchall()

            if len(Info) == 0:
                print("No Data")
                return
            else:
                Line_2 = "Supplier Information"
                print(Line_2.center(20, "-"))

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

    def Search_Supplier(self):
        while True:
            try:
                Supplier_Name = input("Enter Supplier name - ").strip()

                Query = "SELECT * FROM Supplier WHERE Supplier_Name = %s"
                Cursor.execute(Query, (Supplier_Name,))
                Info = Cursor.fetchall()

                if len(Info) == 0:
                    print("Supplier Not Found, Please Type Correct Supplier Name")
                    continue
                else:
                    Line_3 = "Here is Your Related Search"
                    print(Line_3.center(20, "-"))

                    for info in Info:
                        print(info)

            except Exception as E:
                print(E)
            else:
                while True:
                    choose = input("Choose:\n1. Search Another Supplier\n2. Done\nEnter Your Choice: ").title()

                    if choose in ["1", "Search Another Supplier"]:
                        break
                    elif choose in ["2", "Done"]:
                        return
                    else:
                        print("Invalid Choice")
                        continue
                        
    def Update_Supplier(self):
        while True:
            try:
                choose_Update_Options = input(
                    "Choose:\n1. Update Supplier Name\n2. Update Phone Number\n3. Update Email\n4. Back To Supplier Menu\nEnter your choice: "
                ).title()

                if choose_Update_Options in ["1", "Update Supplier Name"]:
                    self.Update_Supplier_Name()
                elif choose_Update_Options in ["2", "Update Phone Number"]:
                    self.Update_Supplier_Phone_No()
                elif choose_Update_Options in ["3", "Update Email"]:
                    self.Update_Email()
                elif choose_Update_Options in ["4", "Back To Supplier Menu"]:
                    return
                else:
                    print("Invalid Choice")
                    continue

            except Exception as E:
                print(E)

    def Update_Supplier_Name(self):
        while True:
            try:
                Supplier_Name = input("Enter Supplier Name: ").strip()

                Query = "SELECT * FROM Supplier WHERE Supplier_Name = %s"
                Cursor.execute(Query, (Supplier_Name,))
                Info = Cursor.fetchall()

                if len(Info) == 0:
                    print("Supplier Not found, Please Type Correct Supplier Name")
                    continue
                else:
                    Line_4 = "Here is Your Related Search"
                    print(Line_4.center(20, "-"))

                    for info in Info:
                        print(info)
                        
                    Supplier_ID = int(input("Enter Supplier Id of which you want to Update Supplier Name: "))
                    Supplier_new_name = input("Enter Updated Supplier Name: ").strip()
        
                    Query = "UPDATE Supplier SET Supplier_Name = %s WHERE Supplier_ID = %s"
                    Cursor.execute(Query, (Supplier_new_name, Supplier_ID))
                    Connection.commit()

                    if Cursor.rowcount == 0:
                        print("Invalid Supplier Id, Please Type Correct Supplier Id")
                        continue
                    else:
                        print("Name Updated Successfully")

                        Line_5 = "Updated Supplier Name"
                        print(Line_5.center(20, "-"))

                        Query = "SELECT * FROM Supplier WHERE Supplier_ID = %s"
                        Cursor.execute(Query, (Supplier_ID,))
                        updated_info = Cursor.fetchone()

                        for info in updated_info:
                            print(info)
                        
            except Exception as E:
                print(E)
            else:
                while True:
                    choose = input("Choose:\n1. Update Another Supplier Name\n2. Done\nEnter Your Choice: ").title()
                    
                    if choose in ["1", "Update Another Supplier Name"]:
                        break
                    elif choose in ["2", "Done"]:
                        return
                    else:
                        print("Invalid Choice")
                        continue

    def Update_Supplier_Phone_No(self):
        while True:
            try:
                Supplier_Name = input("Enter Supplier Name: ").strip()

                Query = "SELECT * FROM Supplier WHERE Supplier_Name = %s"
                Cursor.execute(Query, (Supplier_Name,))
                Info = Cursor.fetchall()

                if len(Info) == 0:
                    print("Supplier Not found, Please Type Correct Supplier name")
                    continue
                else:
                    Line_6 = "Here is Your Related Search"
                    print(Line_6.center(20, "-"))

                    for info in Info:
                        print(info)
                        
                    Supplier_ID = int(input("Enter Supplier Id of which you want to Update Phone Number: "))
                    New_Supplier_Phone_No = input("Enter Updated Phone Number - ").strip()

                    Query = "UPDATE Supplier SET Phone = %s WHERE Supplier_ID = %s"
                    Cursor.execute(Query, (New_Supplier_Phone_No, Supplier_ID))
                    Connection.commit()

                    if Cursor.rowcount == 0:
                        print("Invalid Supplier Id, Please Enter Correct Supplier ID")
                        continue
                    else:
                        print("Phone Number Updated Successfully")
                        
                        Line_7 = "Updated Phone Number"
                        print(Line_7.center(20, "-"))
                        
                        Query = "SELECT * FROM Supplier WHERE Supplier_ID = %s"
                        Cursor.execute(Query, (Supplier_ID,))
                        updated_info = Cursor.fetchone()

                        for info in updated_info:
                            print(info)

            except Exception as E:
                print(E)
            else:
                while True:
                    choose = input("Choose:\n1. Update Another Phone Number\n2. Done\nEnter Your Choice: ").title()
                    
                    if choose in ["1", "Update Another Phone Number"]:
                        break
                    elif choose in ["2", "Done"]:
                        return
                    else:
                        print("Invalid Choice")
                        continue

    def Update_Email(self):
        while True:
            try:
                Supplier_Name = input("Enter Supplier Name: ").strip()
    
                Query = "SELECT * FROM Supplier WHERE Supplier_Name = %s"
                Cursor.execute(Query, (Supplier_Name,))
                Info = Cursor.fetchall()

                if len(Info) == 0:
                    print("Supplier Not found, Please Type Correct Supplier name")
                    continue
                else:
                    Line_8 = "Here is Your Related Search"
                    print(Line_8.center(20, "-"))

                    for info in Info:
                        print(info)

                    Supplier_ID = int(input("Enter Supplier Id of which you want to Update Email: "))
                    New_Email = input("Enter Updated Email - ").strip()
        
                    Query = "UPDATE Supplier SET Email = %s WHERE Supplier_ID = %s"
                    Cursor.execute(Query, (New_Email, Supplier_ID))
                    Connection.commit()

                    if Cursor.rowcount == 0:
                        print("Invalid Supplier Id, Please Enter Correct Supplier ID")
                        continue
                    else:
                        print("Email Updated Successfully")

                        Line_9 = "Updated Email"
                        print(Line_9.center(20, "-"))
                        
                        Query = "SELECT * FROM Supplier WHERE Supplier_ID = %s"
                        Cursor.execute(Query, (Supplier_ID,))
                        updated_info = Cursor.fetchone()

                        for info in updated_info:
                            print(info)

            except Exception as E:
                print(E)
            else: 
                while True:
                    choose = input("Choose:\n1. Update Another Email\n2. Done\nEnter Your Choice: ").title()
                    
                    if choose in ["1", "Update Another Email"]:
                        break
                    elif choose in ["2", "Done"]:
                        return
                    else:
                        print("Invalid Choice")
                        continue

    def Supplier_Menu(self):
        while True:
            choose_supplier_option = input(
                "Choose:\n1. Add Supplier\n2. Delete Supplier\n3. View All Suppliers\n4. Search Supplier\n5. Update Supplier\n6. Back To Homepage\nEnter your choice: "
            ).title()
            
            if choose_supplier_option in ["1", "Add Supplier"]:
                self.Add_supplier()
            elif choose_supplier_option in ["2", "Delete Supplier"]:
                self.Del_Supplier()
            elif choose_supplier_option in ["3", "View All Suppliers"]:
                self.View_Supplier_info()
            elif choose_supplier_option in ["4", "Search Supplier"]:
                self.Search_Supplier()
            elif choose_supplier_option in ["5", "Update Supplier"]:
                self.Update_Supplier()
            elif choose_supplier_option in ["6", "Back To Homepage"]:
                return
            else:
                print("Invalid Choice")
                continue