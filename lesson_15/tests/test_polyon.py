import unittest

from lesson_15.lesson_15_mihaela_vaida.polygon import *


class TestPolygon(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Start testing!')

    @classmethod
    def tearDownClass(cls):
        print('End testing!')

    def setUp(self):
        self.pol1 = Polygons(2, 3, 5, 6)
        self.pol2 = Polygons(4, 6, 7)

    def test_polygon_object_len_of_sides(self):
        self.sides= 3,4,5,3
        test_polygon= Polygons(self.sides)
        self.assertGreaterEqual(len(self.sides), 3, "Not a valid polygon!")


    def test_polygon_perimeter(self):
        pol1 = Polygons(2, 3, 5, 6)
        self.assertEqual(pol1.perimeter(), 16)


    def tearDown(self):
        self.pol1.display()
        self.pol2.display()

class TestTriangle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Start testing!')

    @classmethod
    def tearDownClass(cls):
        print('End testing!')

    def test_triangle_object_init(self):
        a,b,c = 3,4,5
        tri1=Triangle(a,b,c)
        self.assertEqual(tri1.sides, (a,b,c)),\
        'Triangle class is missing attributes!'

    def test_triangle_area_perim(self):
        a, b, c = 3, 4, 5
        tri1 = Triangle(a, b, c)
        self.assertEqual(tri1.area(), 6)
        self.assertEqual(tri1.perimeter(), 12)

class TestSquare(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Start testing!')

    @classmethod
    def tearDownClass(cls):
        print('End testing!')

    def test_square_init(self):
        sq1= Square(3,3,3,3)


        self.assertIsInstance(sq1, Square)
        self.assertEqual(sq1.area(), 9)
        self.assertEqual(sq1.perimeter(), 12)

    def test_calculate_side_from_area(self):
        sq2=Square.from_area(4)

        self.assertIsInstance(sq2, Square)
        self.assertEqual(sq2.area(),4)







if __name__ == '__main__':
    unittest.main(verbosity=2)

# ----------------------------------------------------------------------
# Ran 6 tests in 0.002s
# OK
# Process finished with exit code 0
