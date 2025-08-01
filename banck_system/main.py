class BankAccount:
    def __init__(self, owner_name, account_number, balance, account_type, pin_code, is_active):
        self.owner_name = owner_name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.__pin_code = pin_code
        self.is_active = is_active
    
    def show_information(self):
        print("Account Owner: ", self.owner_name)
        print("Account Number: ", self.account_number)
        print("Account Type: ", self.account_type)
        print("Account Balance: ", self.balance)
        print("Account Status: ", self.is_active)
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful. New balance: ", self.balance)
        else:
            print("Invalid deposit amount. Please enter a positive number.")
        
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance and self.is_active:
            self.balance -= amount
            print("Withdrawal successful. New balance: ", self.balance)
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Account is inactive. Please activate the account first.")
            
    def activate_account(self):
        self.is_active = True
        print("Account activated successfully.")
        
    def deactivate_account(self):
        self.is_active = False
        print("Account deactivated successfully.")
        
        
            
            