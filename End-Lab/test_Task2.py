import unittest
from unittest.mock import patch, MagicMock
import requests
from Task2 import get_weather

class TestGetWeather(unittest.TestCase):
    
    @patch('Task2.requests.get')
    def test_successful_weather_fetch(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"temperature": 25.5}
        mock_get.return_value = mock_response
        
        result = get_weather("London")
        self.assertEqual(result, 25.5)
    
    @patch('Task2.requests.get')
    def test_non_200_status_code(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        result = get_weather("InvalidCity")
        self.assertIsNone(result)
    
    @patch('Task2.requests.get')
    def test_invalid_json_response(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_get.return_value = mock_response
        
        result = get_weather("Paris")
        self.assertIsNone(result)
    
    @patch('Task2.requests.get')
    def test_missing_temperature_field(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"humidity": 65}
        mock_get.return_value = mock_response
        
        result = get_weather("Tokyo")
        self.assertIsNone(result)
    
    @patch('Task2.requests.get')
    def test_timeout_error(self, mock_get):
        mock_get.side_effect = requests.Timeout()
        
        result = get_weather("Berlin")
        self.assertIsNone(result)
    
    @patch('Task2.requests.get')
    def test_connection_error(self, mock_get):
        mock_get.side_effect = requests.ConnectionError()
        
        result = get_weather("Madrid")
        self.assertIsNone(result)
    
    @patch('Task2.requests.get')
    def test_unexpected_error(self, mock_get):
        mock_get.side_effect = Exception("Unexpected error")
        
        result = get_weather("Rome")
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()