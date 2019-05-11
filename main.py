from data import DATA
from report import Report
from transaction import Transaction


def get_data():
    return [Transaction(row['Date'], row['Account'], row['Type'], row['Amount']) for row in DATA]


def get_all_month_types(data):
    months = []
    types = []
    accounts = {}
    for row in data:
        if row.date.month not in months:
            months.append(row.date.month)
        if row.type not in types:
            types.append(row.type)
        if row.account not in accounts:
            accounts[row.account] = 0

    return months, types, accounts


def filter_by_date(data, month):
    return [row for row in data if row.date.month == month]


def filter_by_type(data, transaction_type):
    return [row for row in data if row.type == transaction_type]


def main():
    data = get_data()
    months, types, accounts = get_all_month_types(data)
    for month in months:
        month_transaction = filter_by_date(data, month)
        report = Report(month, month_transaction, accounts, types)
        report.print_report()


if __name__ == '__main__':
    main()
