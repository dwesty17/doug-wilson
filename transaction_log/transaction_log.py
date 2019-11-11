from decimal import Decimal


class TransactionLog:
    def __init__(self):
        self.transactions = []
        self.starting_balance = Decimal(0)

    def daily_breakdown(self):
        print("Daily Breakdown")
        print("----------")
        print("")
        current_date = self.transactions[0]["transaction_date"]

        amount_spent_today = Decimal(0)
        for transaction in self.transactions:
            if transaction["transaction_date"].day != current_date.day:
                print(current_date.strftime("%m-%d-%Y") + ": $" + str(amount_spent_today))
                amount_spent_today = Decimal(0)
                current_date = transaction["transaction_date"]
            else:
                amount_spent_today -= transaction["total_amount"] if transaction["type"] == "CREDIT" else Decimal(0)

    def add_statement(self, statement):
        self.starting_balance += statement["starting_balance"]
        self.transactions.extend(statement["transactions"])
        self.transactions = sorted(self.transactions, key=lambda t: t["transaction_date"])
