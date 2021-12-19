"""Current conditions display concrete class"""
from weather_data import WeatherData


class CurrentConditionsDisplay:
    """Current conditions display concrete class"""

    def __init__(self, weather_data) -> None:
        self.temperature: float
        self.humidity: float
        self.weather_data: WeatherData = weather_data
        self.weather_data.register_observer(self)

    def update(self) -> None:
        """Update the state values the Observers get from the Subject"""
        self.temperature = self.weather_data.temperature
        self.humidity = self.weather_data.humidity
        self.display()

    def display(self) -> None:
        """Display the element that need to be displayed"""
        print(
            f"Current conditions: {self.temperature} F degrees and {self.humidity} % humidity"
        )
