import requests
from unittest.mock import patch, MagicMock


def get_weather(city_name):
    """
    Fetch the current temperature for a given city using a public weather API.

    API Endpoint:
        https://api.weather.example.com/current?city={city_name}

    Handles:
    - Non-200 HTTP status codes
    - Connection timeouts
    - Connection errors
    - JSON decoding errors
    - Missing temperature field

    Parameters:
        city_name (str): Name of the city.

    Returns:
        float or None: Temperature if successful, otherwise None.
    """

    url = f"https://api.weather.example.com/current?city={city_name}"

    try:
        response = requests.get(url, timeout=5)

        # Handle non-200 responses
        if response.status_code != 200:
            print(f"Error: Received HTTP {response.status_code}")
            return None

        try:
            data = response.json()
        except ValueError:
            print("Error: Invalid JSON response")
            return None

        # Check for temperature field
        if "temperature" not in data:
            print("Error: 'temperature' field missing in response")
            return None

        return data["temperature"]

    except requests.Timeout:
        print("Error: Request timed out")
        return None

    except requests.ConnectionError:
        print("Error: Connection error occurred (check network)")
        return None

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
