# transaction.py

from transaction.transaction_category import TransactionCategory

class Transaction:
    """Represents a financial transaction with an amount and category."""

    amount = 0.0
    category = TransactionCategory.EXPENSE

    def __init__(self, amount, category: TransactionCategory):
        self.amount = amount
        self.category = category
        print (f"Creating transaction ${category} for $ ${amount}")

    def __str__(self):
        return (f"Transaction(${self.amount}, category='{self.category}')")

    def __eq__(self, other):
        if (self.amount == other.amount) and (self.category == other.category):
            return True
        else:
            return False
        #pass
