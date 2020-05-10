import unittest


class TestPoligons(unittest.TestCase):

    def test_if_side_is_not_none(self):
        sides = 1, "asd", 3

        self.assertIsNotNone(sides, "Value cannot be of type None")

    def test_if_value_is_not_string(self):
        x = 1
        y = 2

        tp_x = type(x)
        tp_y = type(y)

        assert tp_y == int, 'Value is not Integer!'

    def test_if_triangle_has_3_sides(self):
        sides = 1, 2, 3

        length = len(sides)

        self.assertEqual(length, 3, "Triangle must have 3 sides")

    def test_if_square_has_4_sides(self):
        sides = 4

        self.assertIs(sides, 4, "Square must have 4 sides")

    def test_if_sides_are_not_negative(self):
        sides = 2, 1, 2, 3, 4

        for x in sides:
            self.assertIsNot(x, -3, "Cannot have negative values")


if __name__ == "__main__":
    unittest.main()
