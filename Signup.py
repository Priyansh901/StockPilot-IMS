from Database_Connection import Connection , Cursor

class Signup:

    def signup(self):

        Full_name = input("Enter Full Name : ") 
        Username = input("Enter Username : ")
        Password = input("Enter Password : ")
        Phone = input("Enter Phone Number : ")
        Email = input("Enter Email : ") 

        try:

            Query = """
            INSERT INTO Users
            (username,password,full_name,phone,email)
            VALUES(%s,%s,%s,%s,%s)
            """

            Cursor.execute(
                Query,
                (Username, Password, Full_name, Phone, Email)
            )

            Connection.commit()

            print("Saved Successfully")

        except Exception as e:
            print(e)

        else:
            print("Signup Successfully")
            print("Welcome to Inventory Management System")
            self.Menu()