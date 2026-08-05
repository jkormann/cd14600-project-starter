# foreign_currency_decorator.py

from transaction.transaction import Transaction
#from transaction.transaction_category import TransactionCategory

class IForeignCurrency (Transaction):
    _transaction = Transaction
    _exchangeRate = 0.0

class ForeignCurrencyTransaction(IForeignCurrency):

    def __init__(self, localTransaction: Transaction, exchangeRate: float):
        self._transaction = localTransaction
        # print (f"Creating Foreign Current transaction ${category} for $ ${amount}")
        self._exchangeRate = exchangeRate
        self._transaction.amount = self._transaction.amount * exchangeRate

    def __str__(self):
        return (f"Transaction(${self.amount}, category='{self.category}', exchange rate='{self._exchangeRate}')")

    def __eq__(self, other):
        if (self.amount == other.amount) and (self.category == other.category):
            return True
        else:
            return False
