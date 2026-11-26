class BankAccount:

    def __init__(self, account_number, holder, balance, customer_id, ifsc_code):

        self.account_number = account_number
        self.holder = holder
        self.balance = balance
        self.customer_id = customer_id
        self.ifsc_code = ifsc_code

    def deposit(self, amount):
        print("Depositing Rs.",amount,"in your account")
        self.balance = self.balance + amount

    def withdraw(self, amount):
        # to do: add a check to see if the balance is sufficient
        print("Withdrawing Rs.",amount,"from your account")
        self.balance = self.balance - amount

    def display_balance(self):
        print("Balance = Rs.", self.balance)


account1 = BankAccount(101, "Ahmed", 5000)
account1.display_balance()

account1.deposit(2000)
account1.display_balance()

account1.withdraw(15000)
account1.display_balance()
