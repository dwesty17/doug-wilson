from decimal import Decimal


class TransactionLog:
    def __init__(self):
        self.transactions = []
        self.starting_balance = Decimal(0)
        self.current_balance = Decimal(0)

    def daily_net_worth_breakdown(self):
        print("Net worth overview")
        print("----------")
        print("")

        current_net_worth = self.starting_balance
        print("Starting net worth: " + str(current_net_worth))
        print("")

        print("Net worth by day")
        print("----------")
        print("")
        current_day = self.transactions[0]["transaction_date"].day
        for transaction in self.transactions:
            if transaction["transaction_date"].day != current_day:
                print(str(current_day) + ": " + str(current_net_worth))
                current_day = transaction["transaction_date"].day
            else:
                current_net_worth += transaction["amount_owed"]

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.transactions = sorted(
            self.transactions,
            key=lambda t: t["transaction_date"]
        )
