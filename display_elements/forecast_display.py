"""Current conditions display concrete class"""
from weather_data import WeatherData


class ForecastDisplay:
    """Forecast display concrete class"""

    def __init__(self, weather_data) -> None:
        self.current_pressure: float = 29.92
        self.last_pressure: float
        self.weather_data: WeatherData = weather_data
        self.weather_data.register_observer(self)

    def update(self) -> None:
        """Update the state values the Observers get from the Subject"""
        self.last_pressure = self.current_pressure
        self.current_pressure = self.weather_data.pressure
        self.display()

    def display(self) -> None:
        """Display the element that need to be displayed"""
        if self.current_pressure > self.last_pressure:
            print("Improving weather on the way!")
        elif self.current_pressure == self.last_pressure:
            print("More of the same")
        else:
            print("Watch out for cooler, rainy weather")
