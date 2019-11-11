from datetime import datetime
from decimal import Decimal
from re import sub


def get_transaction_type(amount, vendor_type):
    if vendor_type == "Standard Transfer":
        return "TRANSFER"
    return "CREDIT" if amount < 0 else "DEBIT"


def parse_venmo(statement_csv):
    statement = {
        "starting_balance": Decimal(0),
        "current_balance": Decimal(0),
        "transactions": [],
    }

    line_count = 0
    for row in statement_csv:
        if row[10] and row[10] != "Venmo balance":
            line_count += 1
            continue
        if line_count > 0:
            if line_count == 1:
                statement["starting_balance"] = Decimal(sub(r'[^\d\-.]', '', row[12]))
            else:
                statement["transactions"].append({
                    "transaction_date": datetime.strptime(row[2], "%Y-%m-%dT%H:%M:%S"),
                    "description": row[5],
                    "total_amount": Decimal(sub(r'[^\d\-.]', '', row[8])),
                    "amount_owed": Decimal(sub(r'[^\d\-.]', '', row[8])),
                    "type": get_transaction_type(Decimal(sub(r'[^\d\-.]', '', row[8])), row[3]),
                })
                statement["current_balance"] += Decimal(sub(r'[^\d\-.]', '', row[8]))
        line_count += 1

    return statement
