class Bank_Account:

    account_holder = ""
    balance = 0.0
    account_type = ["Savings", "Current"]

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print(self.balance)

    def __str__(self):
        return "Account Holder : " + self.account_holder + "Account Type " + self.account_type + "Account Balance " + str(self.balance)

if __name__ == "__main__":
    office_account = Bank_Account()
    office_account.balance = 200
    office_account.account_holder = "Raju_Office"
    office_account.account_type = "Current"
    office_account.display_balance()
    office_account.deposit(10000.00)
    print(office_account)
    personal_account = Bank_Account()
    personal_account.account_holder = "Raju_Personal"
    personal_account.account_type = "Savings"
    print(personal_account)
    personal_account.withdraw(500)
    print(personal_account)
    a=0
    a -= 500
    print(a)