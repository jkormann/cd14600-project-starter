# balance_observer.py

import balance
import transaction
from abc import ABC, abstractmethod

class IBalanceObserver(ABC):
# class IBalanceObserver():
    alert_triggered = False
    threshold = 0.0

    def __init__(self, threshold):
        super().__init__()
        print (f"IBalaceObserver::ctr")
        self.threshold = threshold

    @abstractmethod
    def update(self, balance, transaction) -> None:
        print (f"IBalance::update")
        # """Handle balance updates."""
        # raise NotImplementedError("Subclasses must implement update method.")


class PrintObserver(IBalanceObserver):
    # def __init__(self, threshold):
    #     super().__init__()

    def update(self, balance, transaction) -> None:
        """Print balance update message."""
        print (f"PrintObserver::update")
        balance.get_balance()


class LowBalanceAlertObserver(IBalanceObserver):
    def __init__(self, threshold):
        super().__init__(threshold)
        print (f"LowBalance::ctr")
        self.threshold = threshold

    def update(self, balance, transaction) -> None:
        print (f"LowBalance::update")
        """Alert if balance drops below threshold."""
        balance.apply_transaction(transaction)
        if balance.get_balance <= self.threshold:
            self.alert_triggered = True
        pass
