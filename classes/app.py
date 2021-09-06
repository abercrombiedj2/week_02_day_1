from modules.bank_account import *

bank_account = BankAccount("John", 500, "business")
print(bank_account.holder_name)

bank_account.holder_name = "Craig"
print(bank_account.holder_name)

bank_account2 = BankAccount("Stan", 1000, "personal")

bank_account.pay_monthly_fee()
bank_account2.pay_monthly_fee()
print(bank_account.balance, bank_account2.balance)
