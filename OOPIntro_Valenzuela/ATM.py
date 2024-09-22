class ATM():
    def __init__(self, serial_number):
        self.serial_number = serial_number

    def deposit(self, account, amount):
        account.current_balance = account.current_balance + amount
        print("Deposit Complete")
        account.deposit_summ = amount

    def withdraw(self, account, amount):
        account.current_balance = account.current_balance - amount
        print("Withdraw Complete")
        account.withdraw_summ = amount

    def check_currentbalance(self, account):
        print(account.current_balance)
        
    def view_transactionsummary(self, account):
        print("Transaction Summary:")
        print("You deposited ", account.deposit_summ)
        print("You withdrawn", account.withdraw_summ)
        view_transactionsummary()
