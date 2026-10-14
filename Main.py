Login_choose = input("Choose:\n1. Login\n2. Signup\nEnter your choice: ")

if (Login_choose == "Login"):
    L = Login()
    L.login()
    
elif (Login_choose == "Signup"):
    S = Signup() 
    S.signup()
    
else:
    print("Invalid Choice")