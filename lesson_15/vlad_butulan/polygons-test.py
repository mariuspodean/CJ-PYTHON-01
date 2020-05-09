import unittest
from polygons import Polygons, Triangle, Square

class Test_Triangle(unittest.TestCase):

    def test_triangle_object_attribute_initialization(self):
        x, y, z = 2, 3, 4

        triangle1 = Triangle(x, y, z)

        self.assertEqual(triangle1.args, (x, y, z)), 'Triangle class is missing the attributes'
    
    def test_triangle_area(self):
        triangle1 = Triangle(2, 3, 4)
        triangle2 = Triangle(2, 3, 4, 5)

        self.assertIsInstance(triangle1, Triangle)
        self.assertEqual(triangle1.area(), 2.9047375096555625)
        self.assertEqual(triangle2.area(), None)
    
    def test_triangle_perimeter(self):
        triangle1 = Triangle(2, 3, 4)

        self.assertEqual(triangle1.perimeter(), 9)


class Test_Square(unittest.TestCase):

    def test_square_object_attribute_initialization(self):
        x, y, z, w = 2, 2, 2, 2

        square1 = Square(x, y, z, w)

        self.assertEqual(square1.args, (x, y, z, w)), 'Square class is missing the attributes'

    def test_square_area(self):
        square1 = Square(2, 2, 2, 2)
        square2 = Square(2, 3, 4, 5)

        self.assertIsInstance(square1, Square)
        self.assertEqual(square1.area(), 4)
        self.assertEqual(square2.area(), None)

    def test_square_from_area_method(self):
        square3 = Square.from_area(4)

        self.assertIsInstance(square3, Square)
        self.assertEqual(square3.area(), 4)

if __name__ == '__main__':
    unittest.main()