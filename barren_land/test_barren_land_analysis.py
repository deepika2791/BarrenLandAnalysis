import unittest
from barren_land_analysis import Field

class TestBarrenland(unittest.TestCase):
    def setUp(self):
        self.field = Field(600, 400)

    def test_first(self):
        area = self.field.fertile_land(['0 292 399 307'])
        self.assertEqual(area, '116800 116800')

    def test_second(self):
        area = self.field.fertile_land(['48 192 351 207', '48 392 351 407', '120 52 135 547', '260 52 275 547'])
        self.assertEqual(area, '22816 192608')

    def test_no_fertile(self):
        area = self.field.fertile_land(['0 0 399 599'])
        self.assertEqual(area, '0')

