#bank [acc no,balane,ac_type,customer_name]   [initialize,deposit(amout),withdrow(amout),get_balance()]



class bank:
    account_number:int
    balance:int
    account_type:str
    customer_name:str


    def __init__(self,account_number,balance,account_type,customer_name):
        self.account_number=account_number
        self.balance=balance
        self.account_type=account_type
        self.customer_name=customer_name

    def deposit(self,amount):
        self.balance+=amount
        print(f"your account{self.account_number}has been credited witha amount {amount}avl balance{self.balance}")


    def withdraw(self,amount):
        if self.balance<amount:
            print("insufficent amount")
        else:
            self.balance-=amount    
            print(f"your account{self.account_number}has been debited witha amount {amount}avl balance{self.balance}")

    def get_balance(self):
        print("your aval balance",self.balance)        
        

customer_instance1=bank(100000,25000,"savings","asru")
customer_instance1.withdraw(500)

        