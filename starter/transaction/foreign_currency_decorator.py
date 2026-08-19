# foreign_currency_decorator.py

from transaction.transaction import Transaction


class IForeignCurrency(Transaction):
    """
    Interface for Foreign Current Decorator
    """

    _transaction = Transaction
    _exchangeRate = 100.0  # Start with 1:1 currency exchange

    @property
    def amount(self):
        return self._transaction.amount * self._exchangeRate

    @property
    def category(self):
        return self._transaction.category


class ForeignCurrencyTransaction(IForeignCurrency):
    """
    Decorator for Currency Transaction to allow a Foreign Currency value
    """

    def __init__(self, localTransaction: Transaction, exchangeRate: float):
        self._transaction = localTransaction
        self._exchangeRate = exchangeRate

    def __str__(self):
        return (
            f"Transaction(${self.amount}, "
            f"category='{self.category}', "
            f"exchange rate='{self._exchangeRate}')"
        )

    def __eq__(self, other):
        if (self.amount == other.amount) and (
            self._transaction.category == other.category
        ):
            return True
        else:
            return False
