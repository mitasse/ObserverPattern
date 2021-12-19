"""Weather data concrete class"""
from observer import Observer


class WeatherData:
    """Weather data concrete class"""

    def __init__(self) -> None:
        self.observers: list = []
        self.temperature: float
        self.humidity: float
        self.pressure: float

    def register_observer(self, observer: Observer) -> None:
        """Register an observer

        Args:
            observer (Observer): an observer
        """
        self.observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        """Remove an observer

        Args:
            observer (Observer): an observer
        """
        self.observers.remove(observer)

    def notify_observers(self) -> None:
        """Notify all observers when the Subject's state has changed"""
        for observer in self.observers:
            observer.update()

    def measurements_changed(self) -> None:
        """Notify the observers when we get updated measurements from Weather Station"""
        self.notify_observers()

    def set_measurements(
        self, temperature: float, humidity: float, pressure: float
    ) -> None:
        """Set measurements.

        Args:
            temperature (float): temperature
            humidity (float): humidity
            pressure (float): pressure
        """
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()
