import unittest
from app.Airport import Airport
from app.Plane import Plane
from app.Weather import Weather

class IntegrationTests(unittest.TestCase):

    def setUp(self):
        self.weather = Weather()
        self.airport = Airport()
        self.plane = Plane()

    def test_airport_can_store_plane_object(self):
        self.assertFalse(self.airport.hangar)
        self.airport.land(self.plane)
        self.assertEqual(self.plane.flying, False)
        self.assertEqual(self.airport.hangar, [self.plane])

    def test_airport_can_takeoff_plane_object(self):
        self.airport.land(self.plane)
        self.assertEqual(self.airport.hangar, [self.plane])
        self.airport.take_off(self.plane)
        self.assertEqual(self.plane.flying, True)
        self.assertFalse(self.airport.hangar)
