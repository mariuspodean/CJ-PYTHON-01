import unittest
from lesson_15.lesson_15_Turcu_Alexandru.polygons_homework import Square, Triangle, Polygons


class TestSquareArea(unittest.TestCase):
    def test_area(self):
        a, b, c, d = 3, 3, 3, 4
        test_square = Square(a, b, c, d)
        self.assertEqual(test_square.is_valid(), 'Invalid square')

    def test_square_type(self):
        test_homework1 = Polygons(1, 2, 3)
        self.assertIsInstance(test_homework1.args[0], int)
        self.assertIsInstance(test_homework1.args[1], int)
        self.assertIsInstance(test_homework1.args[2], int)

    def test_square_with_area_method(self):
        test_square2 = Square.from_area(4)
        self.assertIsInstance(test_square2, Square)
        self.assertEqual(test_square2.area(), 4)


class TestPolygon(unittest.TestCase):
    def test_sides(self):
        z, y, x, q = 1, 3, 4, 5
        test_polygon = Polygons(z, y, x, q)
        self.assertGreaterEqual(test_polygon.args, 'Invalid polygon')


class TestTriangle(unittest.TestCase):
    def test_triangle_attribute(self):
        a, b, c = 3, 4, 5
        test_triangle1 = Triangle(a, b, c)
        self.assertEqual(test_triangle1.args, 'Invalid triangle')

    def test_triangle_perimeter(self):
        test_triangle1 = Triangle(2, 3, 4)
        self.assertEqual(test_triangle1.perimeter(), 9)


if __name__ == '__main__':
    unittest.main()

