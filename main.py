from csv import reader
from pathlib import Path

from parsers import parse_amex, parse_chase_credit, parse_chase_debit, parse_venmo
from transaction_log import TransactionLog


def parse_statement(path, statement_parser):
    with open(path) as csv_file:
        statement = statement_parser(reader(csv_file, delimiter=','))
        transaction_log.add_statement(statement)


parsers = [
    {"dir": Path("./statements/amex"), "worker": parse_amex},
    {"dir": Path("./statements/chase_credit"), "worker": parse_chase_credit},
    {"dir": Path("./statements/chase_debit"), "worker": parse_chase_debit},
    {"dir": Path("./statements/venmo"), "worker": parse_venmo},
]

transaction_log = TransactionLog()

for parser in parsers:
    for statement_path in parser["dir"].iterdir():
        if statement_path.suffix == ".csv":
            parse_statement(statement_path, parser["worker"])

earliest_purchase_date = transaction_log.transactions[0]["transaction_date"]
latest_purchase_date = transaction_log.transactions[-1]["transaction_date"]
log_duration_days = (latest_purchase_date - earliest_purchase_date).days

number_of_transactions = len(transaction_log.transactions)
number_of_credits = sum(t["type"] == "CREDIT" for t in transaction_log.transactions)
number_of_debits = sum(t["type"] == "DEBIT" for t in transaction_log.transactions)
number_of_transfers = sum(t["type"] == "TRANSFER" for t in transaction_log.transactions)

earliest_purchase_date = transaction_log.transactions[0]["transaction_date"]
latest_purchase_date = transaction_log.transactions[-1]["transaction_date"]
log_duration_days = (latest_purchase_date - earliest_purchase_date).days

print("Overview")
print("----------")
print("")

print("Number of Transaction: " + str(number_of_transactions))
print("Number of Credits: " + str(number_of_credits))
print("Number of Debits: " + str(number_of_debits))
print("Number of Transfers: " + str(number_of_transfers))
print("")

print("Transaction per day: " + str(number_of_transactions / log_duration_days))
print("Credits per day: " + str(number_of_credits / log_duration_days))
print("")

# TODO total value of credits
# TODO average credit amount per day
# TODO total value of debits
# TODO average debit value per day
# TODO difference between credit and debit value

transaction_log.daily_net_worth_breakdown()
