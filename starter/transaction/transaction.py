# transaction.py

from transaction.transaction_category import TransactionCategory


class Transaction:
    """Represents a financial transaction with an amount and category."""

    amount = 0.0
    category = TransactionCategory.EXPENSE

    def __init__(
        self, amount, category: TransactionCategory, invoice_id="", description=""
    ):
        self.amount = amount
        self.category = category
        self.description = description
        self.invoice_id = invoice_id
        print(
            f"Creating transaction {category} for $ {amount} "
            "invoice {invoice_id} desc {description}"
        )

    def __str__(self):
        return f"Transaction(${self.amount}, category='{self.category}')"

    def __eq__(self, other):
        if (
            (self.amount == other.amount)
            and (self.category == other.category)
            and (self.description == other.description)
            and (self.invoice_id == other.invoice_id)
        ):
            return True
        else:
            return False
        # pass
