import unittest
from mock import MagicMock
from app.Weather import Weather

class WeatherTest(unittest.TestCase):

    def setUp(self):
        self.weather = Weather()

    def test_weather_created_stormy_none(self):
        self.assertEqual(self.weather.stormy, None)

    def test_stormy_returns_true_if_rand_method_less_than_2(self):
        self.weather.check_weather = MagicMock(return_value=1)
        self.weather.is_stormy()
        self.assertTrue(self.weather.stormy)

    def test_stormy_returns_true_if_rand_method_less_than_2(self):
        self.weather.check_weather = MagicMock(return_value=0)
        self.weather.is_stormy()
        self.assertTrue(self.weather.stormy)

    def test_stormy_returns_false_if_rand_method_more_than_2(self):
        self.weather.check_weather = MagicMock(return_value=2)
        self.weather.is_stormy()
        self.assertFalse(self.weather.stormy)

    def test_stormy_returns_false_if_rand_method_more_than_2(self):
        self.weather.check_weather = MagicMock(return_value=5)
        self.weather.is_stormy()
        self.assertFalse(self.weather.stormy)
