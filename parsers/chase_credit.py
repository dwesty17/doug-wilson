from datetime import datetime
from decimal import Decimal


def get_transaction_type(amount, ext_type):
    if ext_type == "Payment":
        return "TRANSFER"
    return "DEBIT" if amount > 0 else "CREDIT"


def parse_chase_credit(statement_csv):
    statement = {
        "starting_balance": Decimal(0),
        "current_balance": Decimal(0),
        "transactions": [],
    }

    line_count = 0
    for row in statement_csv:
        if line_count > 0:
            statement["transactions"].append({
                "vendor": "CHASE_CREDIT",
                "transaction_date": datetime.strptime(row[0], "%m/%d/%Y"),
                "description": row[2],
                "total_amount": Decimal(row[5]),
                "type": get_transaction_type(Decimal(row[5]), row[4]),
            })
            statement["current_balance"] -= Decimal(row[5])
        line_count += 1

    return statement
