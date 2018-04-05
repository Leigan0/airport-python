import unittest
from mock import MagicMock
from app.Airport import Airport


class AirportTest(unittest.TestCase):

    def setUp(self):
        self.airport = Airport()
        self.plane = MagicMock()
        self.plane2 = MagicMock()

    def test_hangar_created_empty_list(self):
        self.assertFalse(self.airport.hangar)

    def test_airport_can_add_plane_to_hangar(self):
        self.airport.land(self.plane)
        self.assertTrue(self.plane.land.called)

    def test_airport_can_call_land_method_on_plane_added_to_hangar(self):
        self.airport.land(self.plane)
        self.assertEqual(len(self.airport.hangar),1)

    def test_airport_can_add_multiple_planes_to_hangar(self):
        self.airport.land(self.plane)
        self.airport.land(self.plane)
        self.airport.land(self.plane)
        self.assertEqual(len(self.airport.hangar),3)

    def test_airport_can_remove_plane_from_hangar(self):
        self.airport.land(self.plane)
        self.assertTrue(self.airport.hangar)
        self.airport.take_off(self.plane)
        self.assertFalse(self.airport.hangar)

    def test_airport_takeoff_removes_plane_passed_as_arg(self):
        self.airport.land(self.plane)
        self.airport.land(self.plane2)
        self.airport.take_off(self.plane)
        self.assertEqual(self.airport.hangar, [self.plane2])

    def test_airport_can_call_take_off_method_on_plane_removed_from_hangar(self):
        self.airport.land(self.plane)
        self.airport.take_off(self.plane)
        self.assertTrue(self.plane.take_off.called)
