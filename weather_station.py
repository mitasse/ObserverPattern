"""Main function"""
from display_elements.current_conditions_display import \
    CurrentConditionsDisplay
from display_elements.forecast_display import ForecastDisplay
from weather_data import WeatherData


def main() -> None:
    """Main function"""
    # Create weather data
    weather_data = WeatherData()

    # Define current condition display
    CurrentConditionsDisplay(weather_data)
    ForecastDisplay(weather_data)

    # Simulate new weather measurements
    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)


if __name__ == "__main__":
    main()
