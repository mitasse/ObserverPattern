"""Display element interface"""
from typing import Protocol


class DisplayElement(Protocol):
    """Display element interface"""

    def display(self):
        """Display the element that need to be displayed"""
        ...
