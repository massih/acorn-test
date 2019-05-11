import json


class Report:

    INTEREST_RATE = 10

    def __init__(self, month, transactions, accounts, types):
        self.month = month
        self.transactions = transactions
        self.accounts = accounts
        self.types = dict((transaction_type, 0) for transaction_type in types)

    def print_report(self):
        print(f"For month :{self.month}")
        print('Accounts balance in the beginning of the month')
        self.pretty_print(self.accounts)
        for row in self.transactions:
            print(row.__dict__)
            self.apply_transaction(row)

        print('Accounts balance at the end of the month')
        self.pretty_print(self.accounts)
        print(f'sum of all types this month {self.types}')
        print('*' * 50)

    @staticmethod
    def pretty_print(msg):
        print(json.dumps(msg, sort_keys=True, indent=4))

    def apply_transaction(self, transaction):
        if transaction.type == 'Withdrawal':
            self.accounts[transaction.account] -= transaction.amount
            self.types[transaction.type] += transaction.amount
        else:
            self.accounts[transaction.account] += transaction.amount
            self.types[transaction.type] += transaction.amount

    def calculate_interest(self):
        pass