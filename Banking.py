# Banking-app-in-OOP-in-python.
print("-" *24 + "Banking.py" + "-" * 26)
class Bank():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def get_balance(self):
        return self.name + f" your balance is:  R{self.balance}"
        
    def deposit(self, amount):
        self.balance += amount
        return self.name + f" your new balance is: R {self.balance}"
    def  withdraw(self, amount):
         return self.name + f" your remaining balance is R{self.balance - amount}"
                 
        
       
while True:
        print("*" *24 + " NEPTEC " + "*" * 24)
        name = input("Customer please enter your name: ").upper()
        if name.isalpha() == False:
            print("your name must not contain numbers")
            continue
        while True:
            try:
                balance = float(input("Enter you balance"))
                break
            except ValueError:
                print("Please enter numeric amount and + amount:")
                continue
        customer = Bank(name, balance)
        print("—" * 20)
        print("Welcome : " + name)
        print("—" * 20)
        tasks = ["1. Check balance", "2. Deposit", "3. Withdraw"]
        for task in tasks:
            print(task)
        try:     
            choice = int(input("Choose what you would like to do from the above 1/2/3: ")) 
        except ValueError:
             print("Please enter a the provided option")
             
        if choice == 1:
             print("—" * 60)
             print(customer.get_balance())
             print("—" * 60)
        elif choice == 2:     
            while True:
                try:
                    print("—" * 60)
                    amount = float(input("How much would you like to deposit: "))
                    print("—" * 60)
                except ValueError:
                     print("Please enter numeric amount(123..): ")   
                if amount < 0:
                    print("You cannot deposit a negative amount")
                else:
                     break
            print(customer.deposit(amount)) 
            print("*" * 60) 
          
        elif choice == 3:
            while True:
                try:
                    amount = float(input("How much would you like to withdraw: "))
                except ValueError:
                     print("Please enter numeric amount(123..): ")   
                if amount <= 0:
                    print("You cannot withdraw a negative amount")
                elif amount > balance:
                    print("Bro you have that amount of money")   
                else:
                     break      
            print(customer.withdraw(amount))
            print("*" * 60)               
