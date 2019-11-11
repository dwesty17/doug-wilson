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

        payment_count_today = 0
        amount_spent_today = Decimal(0)
        csv_out = []
        for transaction in self.transactions:
            if transaction["transaction_date"].day != current_date.day:
                print(current_date.strftime("%m-%d-%Y") + ": $" + str(amount_spent_today))
                csv_out.append([current_date.strftime("%m-%d-%Y"), amount_spent_today, payment_count_today])
                current_date = transaction["transaction_date"]
                amount_spent_today = Decimal(0)
                payment_count_today = 0
            elif transaction["type"] == "CREDIT":
                amount_spent_today -= transaction["total_amount"]
                payment_count_today += 1

    def add_statement(self, statement):
        self.starting_balance += statement["starting_balance"]
        self.transactions.extend(statement["transactions"])
        self.transactions = sorted(self.transactions, key=lambda t: t["transaction_date"])
