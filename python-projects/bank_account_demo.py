from bank_account import BankAccount 

account1 = BankAccount(247834, 750.00)
account2 = BankAccount(123452,)
account3 = BankAccount (249847, 400.52)

print(account1)
print(account2)
print(account3)
print()

account1.deposit(500.00)
account2.deposit(1500.00)
account3.withdraw(42.54)

print(account1)
print(account2)
print(account3)
print()
