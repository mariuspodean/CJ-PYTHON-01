import unittest
from lesson_15.lesson_15_Turcu_Alexandru import homework


class TestSquareArea(unittest.TestCase):
    def test_area(self):
        elem = 2
        area = elem * elem
        self.assertAlmostEqual(area, elem*elem)

    def test_square_type(self):
        test_homework1 = homework.Polygons(1, 2, 3)
        self.assertIsInstance(1, int)
        self.assertIsInstance(2, int)
        self.assertIsInstance(3, int)



class TestPolygon(unittest.TestCase):
    def test_polygon_perimeter(self):
        elem1, elem2, elem3 = 1, 2, 3
        test_homework2 = homework.Polygons(1, 3, 5)
        perimeter = elem1+elem2+elem3
        self.assertEqual(perimeter, elem1+elem2+elem3)

    def test_sides(self):
        sides = 1, 3, 4, 5
        test_homework3 = homework.Polygons(sides)
        self.assertGreaterEqual(len(sides), 3, 'Invalid polygon')


class TestTriangle(unittest.TestCase):
    def test_triangle_attribute(self):
        a, b, c = 3, 4, 5
        test_homework4 = homework.Triangle(a, b, c)
        self.assertEqual(test_homework4.args, (a,b,c)), 'Invalid triangle'

    def test_triangle_perimeter(self):
        test_homework5 = homework.Triangle(2, 3, 4)

        self.assertEqual(test_homework5.perimeter(), 9)


if __name__ == '__main__':
    unittest.main()
