import unittest

from lesson_15.edmond_sabou import home1_les13


class TestPoligons(unittest.TestCase):

    def test_if_side_is_not_none(self):
        sides = home1_les13.Polygon = 1

        self.assertIsInstance(sides, int, "Value cannot be of type None")

    def test_if_value_is_not_string(self):
        sides = home1_les13.Polygon = 10

        assert isinstance(sides, int)

    def test_if_triangle_has_3_sides(self):
        sides = home1_les13.Triangle = 1, 2, 3

        length = len(sides)

        self.assertEqual(length, 3, "Triangle must have 3 sides")

    def test_if_square_has_4_sides(self):
        sides = home1_les13.Square = 4

        self.assertIs(sides, 4, "Square must have 4 sides")

    def test_if_sides_are_not_negative(self):
        sides = home1_les13.Polygon = 10, 1, 2, -4, 4

        for x in sides:
            self.assertIsNot(x, -4, "Cannot have negative values")


if __name__ == "__main__":
    unittest.main()
