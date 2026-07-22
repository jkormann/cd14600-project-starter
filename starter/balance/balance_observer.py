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
        self.threshold = threshold

    @abstractmethod
    def update(self, balanceValue, transaction) -> None:
        """Handle balance updates."""
        raise NotImplementedError("Subclasses must implement update method.")


class PrintObserver(IBalanceObserver):
    def update(self, balanceValue, transaction) -> None:
        """Print balance update message."""
        print (f"Balance is ${balanceValue}")


class LowBalanceAlertObserver(IBalanceObserver):
    def update(self, balanceValue, transaction) -> None:
        """Alert if balance drops below threshold."""
        if balanceValue < self.threshold:
            self.alert_triggered = True
        else:
            self.alert_triggered = False
