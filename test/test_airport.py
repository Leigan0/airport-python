import unittest
from mock import MagicMock
from app.Airport import Airport

class AirportTest(unittest.TestCase):

    def setUp(self):
        self.mock_weather = MagicMock()
        self.airport = Airport(self.mock_weather)
        self.airport.weather.is_stormy.return_value = False
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

    def test_airport_raises_exception_land_stormy_weather(self):
        self.airport.weather.is_stormy.return_value = True
        with self.assertRaises(Exception): self.airport.land(self.plane)

    def test_airport_raises_exception_take_off_stormy_weather(self):
        self.airport.land(self.plane)
        self.airport.weather.is_stormy.return_value = True
        with self.assertRaises(Exception): self.airport.take_off(self.plane)

    def test_airport_raises_exception_take_off_plane_not_in_hangar(self):
        with self.assertRaises(Exception): self.airport.take_off(self.plane)

    def test_airport_raises_exception_when_airport_full(self):
        for plane in range(self.airport.DEFAULT_CAPACITY()):
            self.airport.land(self.plane)
        with self.assertRaises(Exception): self.airport.land(self.plane)
