import unittest
from app.Plane import Plane

class PlaneTest(unittest.TestCase):

    def setUp(self):
        self.plane = Plane()

    def test_plane_created_flying_none(self):
        self.assertEqual(self.plane.flying, None)

    def test_plane_land(self):
        self.plane.land()
        self.assertEqual(self.plane.flying, False)

    def test_plane_take_off(self):
        self.plane.take_off()
        self.assertEqual(self.plane.flying, True)
