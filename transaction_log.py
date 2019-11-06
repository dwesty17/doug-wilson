class TransactionLog:
    def __init__(self, starting_balance):
        self.starting_balance = starting_balance
        self.transactions = []

    def add_statement(self, statement):
        self.starting_balance += statement.starting_balance
        self.transactions.extend(statement.transactions)
