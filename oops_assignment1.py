# Q2) Create a Python program to demonstrate polymorphism using the following classes:
# Class: Account
# Method: interest_rate() → (no implementation, just a placeholder).
# Class: SavingsAccount (inherits from Account)
# Method: interest_rate() → prints "Savings Account Interest Rate: 4%".
# Class: CurrentAccount (inherits from Account)
# Method: interest_rate() → prints "Current Account Interest Rate: 0%".
# Class: FixedDeposit (inherits from Account)
# Method: interest_rate() → prints "Fixed Deposit Interest Rate: 7%".
# Create a function show_interest(account_obj) that accepts an Account object and calls its interest_rate() method.
# Pass objects of SavingsAccount, CurrentAccount, and FixedDeposit to demonstrate polymorphism.

class Account:
    def interest_rate(self):
        pass
class SavingsAccount(Account):
    def interest_rate(self):
        print("Savings Account Interest Rate: 4%")
class CurrentAccount(Account):
    def interest_rate(self):
        print("Current Account Interest Rate: 0%")
class FixedDeposit(Account):
    def interest_rate(self):
        print("Fixed Deposit Interest Rate: 7%")
def show_interest(account_obj):
        account_obj.interest_rate()
obj1=SavingsAccount()
obj2=CurrentAccount()
obj3=FixedDeposit()
show_interest(obj1)
show_interest(obj2)
show_interest(obj3)



