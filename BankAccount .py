class BankAccount:
    interest_rate = 0.06  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder  # Instance variable
        self.balance = 0  # Instance variable

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def apply_interest(self):
        self.balance += self.balance * BankAccount.interest_rate

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

# Test the BankAccount class
account1 = BankAccount("Gavamukulya Samson")
account2 = BankAccount("Makubuya David")
account3 = BankAccount("Dave Kwagala")

# Perform operations
print()
account1.deposit(2000)
account1.withdraw(500)
account1.apply_interest()
account1.display_account_info()
print()
account2.deposit(4000)
account2.apply_interest()
account2.display_account_info()
print()
account3.deposit(5000)
account3.apply_interest()
account3.display_account_info()
