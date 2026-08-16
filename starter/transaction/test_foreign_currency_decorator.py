import unittest
from transaction.foreign_currency_decorator import ForeignCurrencyTransaction
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory
from balance.balance import Balance


class TestForeignCurrency(unittest.TestCase):

    def test_transaction(self):
        t = Transaction(50, TransactionCategory.INCOME)
        self.assertEqual(str(t),
                         "Transaction($50, "
                         "category='TransactionCategory.INCOME')")

        ft = ForeignCurrencyTransaction(t, 0.75)
        self.assertEqual(str(ft),
                         "Transaction($37.5, "
                         "category='TransactionCategory.INCOME', "
                         "exchange rate='0.75')")

        # Test by creating an account with a balance,
        # and applying the base transaction with a foreign transation
        currBalance = Balance.get_instance()
        currBalance.reset()
        currBalance.apply_transaction(ft)
        self.assertEqual(currBalance.get_balance(), 37.5)


if __name__ == "__main__":
    unittest.main()
