from datetime import datetime
from decimal import Decimal


def get_transaction_type(amount, vendor_type):
    if vendor_type == "ACCT_XFER" or "AMERICAN EXPRESS ACH PMT" in vendor_type:
        return "TRANSFER"
    return "DEBIT" if amount > 0 else "CREDIT"


def parse_chase_debit(statement_csv):
    statement = {
        "starting_balance": Decimal(0),
        "current_balance": Decimal(0),
        "transactions": [],
    }

    line_count = 0
    for row in statement_csv:
        if line_count > 0:
            if line_count == 1:
                statement["starting_balance"] = Decimal(row[5])
            else:
                statement["transactions"].append({
                    "transaction_date": datetime.strptime(row[1], "%m/%d/%Y"),
                    "description": row[2],
                    "total_amount": Decimal(row[3]),
                    "amount_owed": Decimal(row[3]),
                    "type": row[0],
                })
                statement["current_balance"] += Decimal(row[3])
        line_count += 1

    return statement
