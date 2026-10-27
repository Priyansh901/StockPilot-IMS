from Database_Connection import Connection, Cursor

class Customers:
    
    def Add_Customer(self):
        while True:
            try:
                Customer_Name = input("Enter Customer Name: ").strip()
                Phone_No = input("Enter Customer Phone Number: ").strip()
                Email_ID = input("Enter Customer Email ID: ").strip()
                Address = input("Enter Customer Address: ").strip()
                City = input("Enter Customer City: ").strip()
                State = input("Enter Customer State: ").strip()
                Pincode = input("Enter Customer Pincode: ").strip()

                Query = """
                        INSERT INTO Customers
                        (Customer_Name, Phone_No, Email_ID, Address, City, State, Pincode)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """
                Cursor.execute(Query, (Customer_Name, Phone_No, Email_ID, Address, City, State, Pincode))
                Connection.commit()
                
                print("Added Successfully")

            except Exception as E:
                print(E)

            else:
                while True:
                    choose = input("Choose:\n1. Add Another Customer\n2. Done\nEnter your choice: ").title()

                    if choose in ["1", "Add Another Customer"]:
                        break
                    elif choose in ["2", "Done"]:
                        return
                    else:
                        print("Invalid Choice")
                        continue

    def Del_Customer(self):
        while True:
            try:
                Customer_Name = input("Enter Customer Name: ").strip()

                Query = "SELECT * FROM Customers WHERE Customer_Name = %s"
                Cursor.execute(Query, (Customer_Name,))
                Info = Cursor.fetchall()

                if len(Info) == 0:
                    print("Customer Not Found, Please Enter Correct Customer Name")
                    continue
                else:
                    Line_1 = "Here is Your Related Search"
                    print(Line_1.center(20, "-"))
                    
                    for info in Info:
                        print(info)
                        
                    Customer_ID = int(input("Enter Customer ID which you want to Delete: "))

                    Query = "DELETE FROM Customers WHERE Customer_ID = %s"
                    Cursor.execute(Query, (Customer_ID,))
                    Connection.commit()

                    if Cursor.rowcount == 0:
                        print("Wrong Customer ID, Please Type Correct Customer ID")
                        continue
                    else:
                        print("Deleted Successfully")

            except Exception as E:
                print(E)

            else:
                while True:
                    choose = input("Choose:\n1. Delete Another Customer\n2. Done\nEnter your choice: ").title()

                    if choose in ["1", "Delete Another Customer"]:
                        break
                    elif choose in ["2", "Done"]:
                        return
                    else:
                        print("Invalid Choice")
                        continue

    def View_Customer_info(self):
        try:
            Query = "SELECT * FROM Customers"
            Cursor.execute(Query)
            Info = Cursor.fetchall()

            if len(Info) == 0:
                print("No Data")
                return
            else:
                Line_2 = "Customer Information"
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