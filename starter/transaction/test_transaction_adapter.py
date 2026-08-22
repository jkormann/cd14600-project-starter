import unittest
from transaction.external_income_transaction import ExternalFreelanceIncome
from transaction.transaction_adapter import TransactionAdapter
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory


class TestTransactionAdapter(unittest.TestCase):

    def test_adapter_converts_freelance_income(self):
        ext_txn = ExternalFreelanceIncome(
            500, "INV-12345", "Website development")
        adapter = TransactionAdapter(ext_txn)
        txn = adapter.to_transaction()
        self.assertEqual(
            txn,
            Transaction(
                500,
                TransactionCategory.INCOME,
                description="Website development",
                invoice_id="INV-12345",
            ),
        )

    def test_adapter_converts_freelance_income_FAIL(self):
        ext_txn = ExternalFreelanceIncome(
            500, "INV-12345", "Website development")
        adapter = TransactionAdapter(ext_txn)
        txn = adapter.to_transaction()
        txn.invoice_id = "NONE"
        self.assertNotEqual(
            txn,
            Transaction(
                500,
                TransactionCategory.INCOME,
                description="Website development",
                invoice_id="INV-12345",
            ),
        )


if __name__ == "__main__":
    unittest.main()
