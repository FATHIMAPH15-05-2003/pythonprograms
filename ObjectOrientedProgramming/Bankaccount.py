class BankAccount:
    # customer_name:str
    # mpin:int
    # account_type:str
    # balance:int

    def __init__(self,customer_name,mpin,account_type,balance):
        self.customer_name=customer_name
        self.__mpin=mpin
        self.account_type=account_type
        self.__balance=balance

    def get_balance(self):
        print(self.__balance)

    def __str__(self):
        return self.customer_name


bank_acount_instance=BankAccount("hari",2345,"saving",13000)
print(bank_acount_instance.mpin)