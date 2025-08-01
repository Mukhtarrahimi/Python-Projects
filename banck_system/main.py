class BankAccount:
    def __init__(self, owner_name, account_number, balance, account_type, pin_code, is_active=True):
        if not owner_name or not owner_name.isalpha():
            raise ValueError("Invalid owner name.")
        if not str(account_number).isdigit():
            raise ValueError("Account number must be numeric.")
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Balance must be a positive number.")
        if account_type not in ["savings", "current"]:
            raise ValueError("Account type must be either 'savings' or 'current'.")
        if not pin_code.isdigit() or len(pin_code) != 4:
            raise ValueError("PIN code must be a 4-digit number.")
        if not isinstance(is_active, bool):
            raise ValueError("is_active must be a boolean value.")

        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.__pin_code = pin_code
        self.is_active = is_active

    def show_information(self):
        status = "Active" if self.is_active else "Inactive"
        print("Account Owner:", self.owner_name)
        print("Account Number:", self.account_number)
        print("Account Type:", self.account_type)
        print("Account Balance:", self.balance)
        print("Account Status:", status)

    def verify_pin(self, pin_input):
        return pin_input == self.__pin_code

    def deposit(self, amount):
        if not self.is_active:
            print("Account is inactive. Cannot deposit.")
            return
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Invalid deposit amount.")
            return
        self.balance += amount
        print("Deposit successful. New balance:", self.balance)

    def withdraw(self, amount, pin_code):
        if not self.is_active:
            print("Account is inactive. Cannot withdraw.")
            return
        if not self.verify_pin(pin_code):
            print("Incorrect PIN.")
            return
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Invalid withdrawal amount.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print("Withdrawal successful. New balance:", self.balance)

    def check_balance(self, pin_code):
        if not self.is_active:
            print("Account is inactive.")
            return
        if not self.verify_pin(pin_code):
            print("Incorrect PIN.")
            return
        print("Your balance is:", self.balance)

    def change_pin(self, old_pin, new_pin):
        if not self.verify_pin(old_pin):
            print("Old PIN is incorrect.")
            return
        if not new_pin.isdigit() or len(new_pin) != 4:
            print("New PIN must be a 4-digit number.")
            return
        if new_pin == old_pin:
            print("New PIN must be different from the old PIN.")
            return
        self.__pin_code = new_pin
        print("PIN changed successfully.")

    def deactivate_account(self, pin_code):
        if not self.verify_pin(pin_code):
            print("Incorrect PIN.")
            return
        if not self.is_active:
            print("Account is already inactive.")
            return
        self.is_active = False
        print("Account deactivated successfully.")

    def activate_account(self, pin_code):
        if not self.verify_pin(pin_code):
            print("Incorrect PIN.")
            return
        if self.is_active:
            print("Account is already active.")
            return
        self.is_active = True
        print("Account activated successfully.")
