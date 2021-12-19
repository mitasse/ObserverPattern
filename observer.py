"""Obseerver interface"""
from typing import Protocol


class Observer(Protocol):
    """Observer interface"""

    def update(self) -> None:
        """Update the state values the Observers get from the Subject"""
        ...
