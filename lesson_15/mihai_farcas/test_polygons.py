import unittest

import polygons

class TestPolygons(unittest.TestCase):
    def test_square_has_init_values_for_sides(self):
        self.sides = '3'
        test_square = polygons.Square(self.sides)
        assert isinstance(test_square.sides, int)




unittest.main()
