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

    def __init__(self, local_transaction: Transaction, exchange_rate: float):
        self._transaction = local_transaction
        self._exchange_rate = exchange_rate

    def __str__(self):
        return (
            f"Transaction(${self.amount}, "
            f"category='{self.category}', "
            f"exchange rate='{self._exchange_rate}')"
        )

    def __eq__(self, other):
        if (self.amount == other.amount) and (
            self._transaction.category == other.category
        ):
            return True
        else:
            return False
