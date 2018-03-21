import unittest
from mock import MagicMock
from app.Airport import Airport


class AirportTest(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()
        self.plane = MagicMock()

    def test_hangar_created_empty_list(self):
        self.assertFalse(self.airport.hangar)

    def test_airport_can_add_plane_to_hangar(self):
        self.airport.land(self.plane)
        self.assertEqual(len(self.airport.hangar),1)

    def test_airport_can_add_multiple_planes_to_hangar(self):
        self.airport.land(self.plane)
        self.airport.land(self.plane)
        self.airport.land(self.plane)
        self.assertEqual(len(self.airport.hangar),3)
