class bank:
    def __init__(self):
        self.account_number=int(input("Enter the account number:"))
        self.name=input("Enter the name:")
        self.type_of_account=input("Enter the type of account:")
        self.balance=0
    def deposit(self):
        self.amount=int(input("Enter the amount to be deposited:"))
        self.balance+=self.amount
        print("\n Amount deposited:",self.amount)
    def withdraw(self):
        self.with_amount=int(input("Enter the amount to be withdrawed:"))
        if(self.balance>=self.with_amount):
            self.balance-=self.with_amount
            print("\n You withdrew:",self.with_amount)
        else:
            print("\n Insufficient balance")
    def display(self):
        print("Avalilable Balance:",self.balance)

a = bank()
a.deposit()
a.withdraw()
a.display()
