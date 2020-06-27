import unittest

import lesson_13


class TestTriangle(unittest.TestCase):

    def test_triangle_area(self):
        triangle1 = lesson_13.Triangle(4, 5, 6)
        triangle2 = lesson_13.Triangle(4, 5, 6, 7)

        self.assertIsInstance(triangle1, lesson_13.Triangle)
        self.assertEqual(triangle1.area(), 2)
        self.assertEqual(triangle2.area(), None)


class TestSquare(unittest.TestCase):

    def test_square_area(self):
        square1 = lesson_13.Square(2, 2, 2, 2)
        square2 = lesson_13.Square(2, 3, 4, 5)

    def test_square_4_sides(self):
        i = lesson_13.Square(1, 2, 3, 4)

        len_sides = len(i.sides)

        self.assertEqual(len_sides, 4, "Square must have 4 sides")


class TestPolygon(unittest.TestCase):

    def test_side_not_none(self):
        sides = 1

        i = lesson_13.Polygon(sides)

        self.assertIsNotNone(i, "Value cannot be None!")
