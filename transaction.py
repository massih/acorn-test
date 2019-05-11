from datetime import datetime


class Transaction:
    def __init__(self, date, account, type, amount):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.account = account
        self.type = type
        self.amount = int(amount)