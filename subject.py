"""Subject interface"""
from typing import Protocol

from observer import Observer


class Subject(Protocol):
    """Subject interface"""

    def register_observer(self, observer: Observer) -> None:
        """Register an observer

        Args:
            observer (Observer): an observer
        """
        ...

    def remove_observer(self, observer: Observer) -> None:
        """Remove an observer

        Args:
            observer (Observer): an observer
        """
        ...

    def notify_observers(self) -> None:
        """Notify all observers when the Subject's state has changed"""
        ...
