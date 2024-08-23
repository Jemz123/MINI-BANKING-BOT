class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}."
            else:
                return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

    def check_balance(self):
        return f"Current balance: ${self.balance:.2f}."


class BankingBot:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, account_holder)
            return f"Account created for {account_holder} with account number {account_number}."
        else:
            return "Account already exists."

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def process_command(self, command):
        parts = command.split()
        if not parts:
            return "No command entered."

        action = parts[0].lower()

        if action == 'create':
            if len(parts) == 3:
                return self.create_account(parts[1], parts[2])
            else:
                return "Usage: create <account_number> <account_holder>"
        elif action == 'deposit':
            if len(parts) == 3:
                try:
                    amount = float(parts[2])
                    account = self.get_account(parts[1])
                    if account:
                        return account.deposit(amount)
                    else:
                        return "Account not found."
                except ValueError:
                    return "Invalid amount. Please enter a number."
            else:
                return "Usage: deposit <account_number> <amount>"
        elif action == 'withdraw':
            if len(parts) == 3:
                try:
                    amount = float(parts[2])
                    account = self.get_account(parts[1])
                    if account:
                        return account.withdraw(amount)
                    else:
                        return "Account not found."
                except ValueError:
                    return "Invalid amount. Please enter a number."
            else:
                return "Usage: withdraw <account_number> <amount>"
        elif action == 'balance':
            if len(parts) == 2:
                account = self.get_account(parts[1])
                if account:
                    return account.check_balance()
                else:
                    return "Account not found."
            else:
                return "Usage: balance <account_number>"
        else:
            return "Unknown command. Available commands: create, deposit, withdraw, balance."


def main():
    bot = BankingBot()
    print("Welcome to the Banking Bot!")

    while True:
        command = input("\nEnter command (or 'exit' to quit): ")
        if command.lower() == 'exit':
            print("Goodbye!")
            break
        response = bot.process_command(command)
        print(response)

if __name__ == "__main__":
    main()
