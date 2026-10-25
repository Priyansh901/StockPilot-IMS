from Database_Connection import Connection , Cursor

class Supplier:

    def Add_supplier(self):

        while True:

            try:

                Supplier_Name = input("Enter Supplier Name: ").strip()
                Phone_No = input("Enter Supplier Phone Number: ").strip()
                Email_Id = input("Enter Supplier Email ID: ").strip()
                Address = input("Enter Supplier Address: ").strip() 

                Query = "insert into Supplier(Supplier_Name , Phone , Email , Address) values(%s,%s,%s,%s)"
                Cursor.execute(Query, (Supplier_Name , Phone_No , Email_Id , Address))
                Connection.commit()
                
                print("Added Successfully")

            except Exception as E:
                print(E)

            else:
        
                while True:
                    
                    choose = input("Choose:\n1. Add Another Supplier\n2. Done\nEnter your choice: ").title()
                    
                    if (choose == "Done"):
                        return

                    elif(choose == "Add Another Supplier"):
                        break
                        
                    else:
                        print("Invalid Choice")
                        continue

    def Del_Supplier(self):

        while True:

            try:

                Supplier_Name =  input("Enter Supplier Name: ").strip()

                Query = "Select *from Supplier where Supplier_Name = %s"
                Cursor.execute(Query, (Supplier_Name,))
                Info = Cursor.fetchall()

                if(len(Info) == 0):
                    print("Supplier Not found , Please Enter Coorect Supplier Name")
                    continue

                else:
                    Line_1 = "Here is Your Related Search"
                    print(Line_1.center(20,"-"))
                    
                    for info in Info:
                        print(info)
                        
                    Supplier_ID = int(input("Enter Supplier Id which you want to Delete: "))

                    Query = "Delete from Supplier where Supplier_ID = %s"
                    Cursor.execute(Query, (Supplier_ID,))
                    Connection.commit()

                    if(Cursor.rowcount == 0):
                        print("Worong Supplier ID , Please Type Correct Supplier ID")
                        continue
                    else:
                        print("Deleted Successfully")


            except Exception as E:
                print(E)

            else:

                while True:
                    
                    choose = input("Choose:\n1. Delete Another Supplier\n2. Done\nEnter your choice: ").title()

                    if(choose == "Delete Another Supplier"):
                        break

                    elif(choose == "Done"):
                        return

                    else:
                        print("Invalid Choice")
                        continue

    def View_Supplier_info(self):

        try:
            
            Query = "Select*from Supplier"
            Cursor.execute(Query)
            Info = Cursor.fetchall()

            if(len(Info)==0):
                print("No Data")
                return
                
            else:
                
                Line_2 = "Supplier Information"
                print(Line_2.center(20,"-"))

                for info in Info:
                    print(info)

        except Exception as E:
            print(E)

        else:

            while True:
                
                choose = input("Choose :\n Done\nEnter Your choice").title()

                if(choose == "Done"):
                    return

                else:
                    print("Invalid Choice")
                    continue


    def Search_Supplier(self):

        while True:
            
            try:
                
                Supplier_Name = input("Enter Supplier name - ").strip()

                Query = "Select*from Supplier where Supplier_Name = %s"
                Cursor.execute(Query , (Supplier_Name,))
                Info = Cursor.fetchall()

                if(len(Info) == 0):
                    print("Supplier Not Found , Please Type Correct Supplier Name")
                    continue

                else:
                    
                    Line_3 = "Here is Your Related Search"
                    print(Line_3.center(20,"-"))

                    for info in Info:
                        print(info)

            except Exception as E:
                print(E)

            else:

                while True:
                    
                    choose = input("Choose :\n1. Search Another Supplier\n2. Done\nEnter Your Choice :").title()

                    if(choose == "Search Another Supplier"):
                        break

                    elif(choose == "Done"):
                        return

                    else:
                        print("Invalid Choice")
                        continue
                        
    def Update_Supplier(self):

        while True:
            
            def Update_Supplier_Name():
                
                while True:
                    
                    try:
                        
                        Supplier_Name =  input("Enter Supplier Name: ").strip()

                        Query = "Select *from Supplier  where Supplier_Name = %s"
                        Cursor.execute(Query, (Supplier_Name,))
                        Info = Cursor.fetchall()

                        if(len(Info) == 0):
                            print("Supplier Not found , Please Type Correct Supplier Name")
                            continue

                        else:

                            Line_4 = "Here is Your Related Search"
                            print(Line_4.center(20,"-"))

                            for info in Info:
                                print(info)
                                    
                            Supplier_ID = int(input("Enter Supplier Id of which you want to Update Supplier Name: "))
                            Supplier_new_name = input("Enter Updated Supplier Name: ").strip()
                
                            Query = "update Supplier set Supplier_Name = %s where Supplier_ID = %s"
                            Cursor.execute(Query , (Supplier_new_name ,Supplier_ID))
                            Connection.commit()

                            if(Cursor.rowcount == 0):
                                print("Type Invlaid Supplier Id , P322222222lease Type Correct Supplier Id")
                                continue

                            else:
                                print("Name Updated Successfully")

                                Line_5 = "Updated Supplier Name"
                                print(Line_5.center(20,"-"))

                                Query = "Select *from Supplier where Supplier_ID = %s"
                                Cursor.execute(Query, (Supplier_ID,))
                                Info = Cursor.fetchone()

                                for info in Info:
                                    print(info)
                                
                    except Exception as E:
                        print(E)

                    else:
                        
                        while True:
                            
                            choose = input("Choose :\n1. Update Another Supplier Name\n2. Done\nEnter Your Choice :").title()
                            
                            if(choose == "Update Another Supplier Name"):
                                break

                            elif(choose == "Done"):
                                return

                            else:
                                print("Invalid Choice")
                                continue

            def Update_Supplier_Phone_No():
                
                while True:
                    
                    try:
                        
                        Supplier_Name =  input("Enter Supplier Name: ").strip()

                        Query = "Select *from Supplier  where Supplier_Name = %s"
                        Cursor.execute(Query, (Supplier_Name,))
                        Info = Cursor.fetchall()

                        if(len(Info) == 0):
                            print("Supplier Not found , Please Type Correct Supplier name")
                            continue

                        else:
                            
                            Line_6 = "Here is Your Reated Search"
                            print(Line_6.center(20,"-"))

                            for info in Info:
                                print(info)
                                
                            Supplier_ID = int(input("Enter Supplier Id of which you want to Update Phone Number: "))
                            New__Supplier_Phone_No = input("Enter Updated Phone Number - ").strip()

                            Query = "update Supplier set Phone = %s where Supplier_ID = %s"
                            Cursor.execute(Query , (New__Supplier_Phone_No , Supplier_ID))
                            Connection.commit()

                            if(Cursor.rowcount == 0):
                                print("Type Invlaid Supplier Id , Please Enter Correct Supplier ID")
                                continue

                            else:
                                
                                print("Phone Number Updated Successfully")
                                
                                Line_7 = "Updated Phone Number"
                                print(Line_7.center(20,"-"))
                                
                                Query = "Select *from Supplier where Supplier_ID = %s"
                                Cursor.execute(Query, (Supplier_ID,))
                                Info = Cursor.fetchone()

                                for info in Info:
                                    print(info)

                    except Exception as E:
                        print(E)

                    else:
                        
                        while True:
                            
                            choose = input("Choose :\n1. Update Another Phone Number\n2. Done\nEnter Your Choice :").title()
                                
                            if(choose == "Update Another Phone Number"):
                                break

                            elif(choose == "Done"):
                                return

                            else:
                                print("Invalid Choice")
                                continue

            def Update_Email():

                while True:

                    try:

                        Supplier_Name =  input("Enter Supplier Name: ").strip()
    
                        Query = "Select *from Supplier  where Supplier_Name = %s"
                        Cursor.execute(Query, (Supplier_Name,))
                        Info = Cursor.fetchall()

                        if(len(Info) == 0):
                            print("Supplier Not found , Please Type Correct Supplier name")
                            continue

                        else:
                            
                            Line_8 = "Here is Your Related Search"
                            print(Line_8.center(20,"-"))

                            for info in Info:
                                print(info)

                            Supplier_ID = int(input("Enter Supplier Id of which you want to Update Email: "))
                            New_Email = input("Enter Updated Email - ").strip()
                
                            Query = "update Supplier set Email = %s where Supplier_ID = %s"
                            Cursor.execute(Query , ( New_Email , Supplier_ID))
                            Connection.commit()

                            if(Cursor.rowcount == 0):
                                print("Type Invlaid Supplier Id , Please Enter Correct Supplier ID")
                                continue

                            else:
                                print("Email Updated Successfully")

                                Line_9 = "Updated Email"
                                print(Line_9.center(20,"-"))
                                
                                Query = "Select *from Supplier where Supplier_ID = %s"
                                Cursor.execute(Query, (Supplier_ID,))
                                Info = Cursor.fetchone()

                                for info in Info:
                                    print(info)

                    except Exception as E:
                        print(E)

                    else: 
                        
                        while True:
                            
                            choose = input("Choose :\n1. Update Another Email\n2. Done\nEnter Your Choice :").title()
                            
                            if(choose == "Update Another Email"):
                                break
                                    
                            elif(choose == "Done"):
                                return

                            else:
                                print("Invalid Choice")
                                continue