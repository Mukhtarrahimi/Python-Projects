class BankAccount:
    def __init__(self, owner_name, account_number, balance, account_type, pin_code, is_active=True):
        if not owner_name or not owner_name.isalpha():
            raise ValueError("Invalid owner name.")
        if not str(account_number).isdigit():
            raise ValueError("Account number must be numeric.")
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Balance must be a positive number.")
        if account_type not in ["savings", "current"]:
            raise ValueError("Account type must be 'savings' or 'current'.")
        if not pin_code.isdigit() or len(pin_code) != 4:
            raise ValueError("PIN code must be 4-digit.")
        if not isinstance(is_active, bool):
            raise ValueError("is_active must be True or False.")

        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.__pin_code = pin_code
        self.is_active = is_active

    def verify_pin(self, pin_input):
        return pin_input == self.__pin_code

    def show_information(self):
        status = "Active" if self.is_active else "Inactive"
        print(f"\n--- Account Information ---")
        print("Owner:", self.owner_name)
        print("Account Number:", self.account_number)
        print("Account Type:", self.account_type)
        print("Balance:", self.balance)
        print("Status:", status)

    def deposit(self, amount):
        if not self.is_active:
            print("Account is inactive.")
            return
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Invalid amount.")
            return
        self.balance += amount
        print("Deposit successful. New balance:", self.balance)

    def withdraw(self, amount, pin_code):
        if not self.is_active:
            print("Account is inactive.")
            return
        if not self.verify_pin(pin_code):
            print("Incorrect PIN.")
            return
        if amount <= 0 or amount > self.balance:
            print("Invalid amount or insufficient funds.")
            return
        self.balance -= amount
        print("Withdrawal successful. New balance:", self.balance)

    def check_balance(self, pin_code):
        if not self.verify_pin(pin_code):
            print("Incorrect PIN.")
            return
        print("Current balance:", self.balance)

    def change_pin(self, old_pin, new_pin):
        if not self.verify_pin(old_pin):
            print("Old PIN is incorrect.")
            return
        if not new_pin.isdigit() or len(new_pin) != 4:
            print("New PIN must be 4-digit.")
            return
        self.__pin_code = new_pin
        print("PIN changed successfully.")

    def deactivate_account(self, pin_code):
        if not self.verify_pin(pin_code):
            print("Incorrect PIN.")
            return
        self.is_active = False
        print("Account deactivated.")

    def activate_account(self, pin_code):
        if not self.verify_pin(pin_code):
            print("Incorrect PIN.")
            return
        self.is_active = True
        print("Account activated.")

    def transfer(self, other_account, amount, pin_code):
        if not isinstance(other_account, BankAccount):
            print("Invalid destination account.")
            return
        if not self.is_active or not other_account.is_active:
            print("Both accounts must be active.")
            return
        if not self.verify_pin(pin_code):
            print("Incorrect PIN.")
            return
        if amount <= 0 or amount > self.balance:
            print("Invalid amount or insufficient balance.")
            return
        self.balance -= amount
        other_account.balance += amount
        print(f"Transfer successful. New balance: {self.balance}")


class BankSystem:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        try:
            name = input("Enter owner name: ").capitalize()
            acc_num = input("Enter account number: ")
            if self.find_account(acc_num):
                print("Account number already exists.")
                return
            balance = float(input("Enter initial balance: "))
            acc_type = input("Enter account type (savings/current): ").lower()
            pin = input("Set 4-digit PIN: ")
            account = BankAccount(name, acc_num, balance, acc_type, pin)
            self.accounts.append(account)
            print("Account created successfully.")
        except ValueError as e:
            print("Error:", e)

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def login(self):
        acc_num = input("Enter your account number: ")
        pin = input("Enter your 4-digit PIN: ")
        account = self.find_account(acc_num)
        if account and account.verify_pin(pin):
            print(f"Welcome {account.owner_name}!")
            self.account_menu(account)
        else:
            print("Invalid account number or PIN.")

    def account_menu(self, account):
        while True:
            print("\n--- Account Menu ---")
            print("1. Show Information")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Change PIN")
            print("6. Deactivate Account")
            print("7. Activate Account")
            print("8. Transfer")
            print("9. Logout")
            choice = input("Choose an option: ")

            if choice == "1":
                account.show_information()
            elif choice == "2":
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == "3":
                amount = float(input("Enter amount to withdraw: "))
                pin = input("Enter your PIN: ")
                account.withdraw(amount, pin)
            elif choice == "4":
                pin = input("Enter your PIN: ")
                account.check_balance(pin)
            elif choice == "5":
                old_pin = input("Enter current PIN: ")
                new_pin = input("Enter new PIN: ")
                account.change_pin(old_pin, new_pin)
            elif choice == "6":
                pin = input("Enter your PIN: ")
                account.deactivate_account(pin)
            elif choice == "7":
                pin = input("Enter your PIN: ")
                account.activate_account(pin)
            elif choice == "8":
                target_acc_num = input("Enter recipient account number: ")
                target_account = self.find_account(target_acc_num)
                if not target_account:
                    print("Target account not found.")
                    continue
                amount = float(input("Enter amount to transfer: "))
                pin = input("Enter your PIN: ")
                account.transfer(target_account, amount, pin)
            elif choice == "9":
                print("Logged out.\n")
                break
            else:
                print("Invalid option.")


def main():
    bank = BankSystem()
    while True:
        print("\n====== Bank System ======")
        print("1. Create New Account")
        print("2. Login to Account")
        print("3. Exit")
        option = input("Choose an option: ")

        if option == "1":
            bank.create_account()
        elif option == "2":
            bank.login()
        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
