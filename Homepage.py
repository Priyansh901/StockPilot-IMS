class Homepage:
 
    def Menu(self):
        
        choose = input("Choose:\n1. Products Info\n2. Suppliers Info\n3. Customer Info\n4. Purchase Info\nEnter your choice: ")

        if (choose == "Products Info"):
            self.Product_Menu() 

        elif (choose == "Suppliers Info"):
