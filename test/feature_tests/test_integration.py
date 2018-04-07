import unittest
from mock import MagicMock
from app.Airport import Airport
from app.Plane import Plane
from app.Weather import Weather

class IntegrationTests(unittest.TestCase):

    def setUp(self):
        self.airport = Airport(Weather)
        self.plane = Plane()
        self.airport.weather.check_weather = MagicMock(return_value=2)

    def test_airport_can_store_plane_object(self):
        self.assertFalse(self.airport.hangar)
        self.airport.land(self.plane)
        self.assertEqual(self.plane.flying, False)
        self.assertEqual(self.airport.hangar, [self.plane])

    def test_plane_cannot_land_if_weather_object_confirms_stormy(self):
        self.airport.weather.check_weather = MagicMock(return_value=0)
        self.assertFalse(self.airport.hangar)
        with self.assertRaises(Exception): self.airport.land(self.plane)
        self.assertFalse(self.airport.hangar)

    def test_airport_can_takeoff_plane_object(self):
        self.airport.land(self.plane)
        self.assertEqual(self.airport.hangar, [self.plane])
        self.airport.take_off(self.plane)
        self.assertEqual(self.plane.flying, True)
        self.assertFalse(self.airport.hangar)

    def test_plane_cannot_take_off_if_weather_object_confirms_stormy(self):
        self.airport.land(self.plane)
        self.airport.weather.check_weather = MagicMock(return_value=0)
        with self.assertRaises(Exception): self.airport.land(self.plane)
        self.assertEqual(self.airport.hangar, [self.plane])
