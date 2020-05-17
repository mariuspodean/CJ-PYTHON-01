import unittest

from lesson_15.edmond_sabou import home1_les13


class TestPoligons(unittest.TestCase):

    def test_if_side_is_not_none(self):
        sides = 1

        i = home1_les13.Polygon(sides)

        self.assertIsNotNone(sides, "Value cannot be None!")

    def test_if_value_is_not_string(self):
        sides1, side2, side3, side4 = 1, 2, 2, 3

        i = home1_les13.Polygon(sides1, side2, side3, side4)

        assert isinstance((sides1, side2, side3, side4), int)

    def test_if_triangle_has_3_sides(self):
        sides = 1, 2, 3

        len_sides = len(sides)

        i = home1_les13.Triangle(sides)

        self.assertEqual(len_sides, 3, "Triangle must have 3 sides")

    def test_if_square_has_4_sides(self):
        sides = 1, 2, 3, 4

        len_sides = len(sides)

        i = home1_les13.Square(sides)

        self.assertEqual(len_sides, 4, "Square must have 4 sides")

    def test_if_sides_are_not_negative(self):
        sides = 1, 2, 3, 4, -56

        i = home1_les13.Polygon(sides)

        self.assertIsNot(sides, -56, "Cannot have negative values")


if __name__ == "__main__":
    unittest.main()
