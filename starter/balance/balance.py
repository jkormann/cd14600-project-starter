# balance.py

from transaction.transaction_category import TransactionCategory
from transaction.transaction import Transaction
from balance.balance_observer import IBalanceObserver


class Balance:
    """Singleton to track the balance."""

    _instance = None
    _balance = 0.0
    _balance_observer = []

    def __init__(self):
        """Initialize the balance. Prevent direct instantiation."""
        self._balance = 0.0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._balance = 0.0
            cls._instance._balance_observer = []
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance

    def register_observer(self, balance_observer):
        self._balance_observer.append(balance_observer)
        pass

    def reset(self):
        """Reset the net balance to zero."""
        self._balance = 0.0

    def add_income(self, amount):
        """Add income to the balance."""
        self._balance = self._balance + amount

    def add_expense(self, amount):
        """Subtract expense from the balance."""
        self._balance = self._balance - amount
        # pass

    def apply_transaction(self, transaction):
        """
        Apply a Transaction object to update the balance.

        Args:
            transaction (Transaction): The transaction to apply.
        """
        if transaction.category == TransactionCategory.INCOME:
            self._balance = self._balance + transaction.amount
        elif transaction.category == TransactionCategory.EXPENSE:
            self._balance = self._balance - transaction.amount
        else:
            raise ValueError("Do better")
        for oby in self._balance_observer:
            oby.update(self._balance, transaction)

    def get_balance(self):
        """Get the current net balance."""
        return self._balance

    def summary(self):
        """Return a summary string of the net balance."""
