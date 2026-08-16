# balance_observer.py

import balance
import transaction
from abc import ABC, abstractmethod


class IBalanceObserver(ABC):
    alert_triggered = False
    threshold = 0.0

    def __init__(self, threshold=0.0):
        super().__init__()
        self.threshold = threshold

    @abstractmethod
    def update(self, balanceValue, transaction) -> None:
        """Handle balance updates."""
        raise NotImplementedError("Subclasses must implement update method.")


class PrintBalanceObserver(IBalanceObserver):
    def update(self, balanceValue, transaction) -> None:
        """Print balance update message."""
        self.threshold = 0.0
        self.alert_triggered = False  # Print only
        print(f"Balance is ${balanceValue}")


class LowBalanceAlertObserver(IBalanceObserver):
    def update(self, balanceValue, transaction) -> None:
        """Alert if balance drops below threshold."""
        if balanceValue < self.threshold:
            print("Triggered")
            self.alert_triggered = True
        else:
            self.alert_triggered = False
