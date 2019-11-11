from datetime import datetime
from decimal import Decimal


def get_transaction_type(amount, description):
    if description == "ONLINE PAYMENT - THANK YOU":
        return "TRANSFER"
    return "DEBIT" if amount < 0 else "CREDIT"


def parse_amex(statement_csv, purchase_split=Decimal(1)):
    statement = {
        "starting_balance": Decimal(0),
        "current_balance": Decimal(0),
        "transactions": [],
    }

    for row in statement_csv:
        statement["transactions"].append({
            "transaction_date": datetime.strptime(row[0], "%m/%d/%Y %a"),
            "description": row[2],
            "total_amount": -Decimal(row[7]),
            "amount_owed": -Decimal(row[7]) * purchase_split,
            "type": get_transaction_type(Decimal(row[7]), row[2]),
        })
        statement["current_balance"] += Decimal(row[7]) * purchase_split

    return statement
