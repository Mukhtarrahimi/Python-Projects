class BankAccount:
    def __init__(self, owner_name, account_number, balance, account_type, __pin_code, is_acctive):
        self.owner_name = owner_name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.__pin_code = __pin_code
        self.is_acctive = is_acctive
    
    def show_infomation(self):
        print("Account Owner: ", self.owner_name)
        print("Account Number: ", self.account_number)
        print("Account Type: ", self.account_type)
        print("Account Balance: ", self.balance)
        print("Account Status: ", self.is_acctive)
        
        