import unittest

from lesson_15.lesson_15_mihaela_vaida import polygon


class TestPolygon(unittest.TestCase):
    def test_polygon_object_len_of_sides(self):
        sides = 4, 3, 4, 5
        test_polygon = polygon.Polygons(sides)
        # assert hasattr(test_polygon, 'args'), 'Polygons class is missing  attribute'
        # assert isinstance(test_polygon.sides, int)
        self.assertGreaterEqual(len(sides),3, "Not a valid polygon!")

    def test_polygon_object_sides_type(self):

       test_polygon = polygon.Polygons(3, 4, 5)
       self.assertIsInstance(3, int)
       self.assertIsInstance(4, int)
       self.assertIsInstance(5, int)

    def test_polygon_perimeter_sum(self):
        a,b,c=3,5,4
        test_polygon = polygon.Polygons(3, 5, 4)
        perimeter=a+b+c

        self.assertEqual(perimeter, a+b+c)
        
    def test_triangle_area(self):
        a,b,c= 3,5,4
        test_triangle = polygon.Triangle(3, 5, 4)
        sp=(a+b+c)/2
        area = (sp * (sp - a) * (sp - b) * (sp - c))**0.5
        self.assertEqual(sp, (a+b+c)/2)
        self.assertEqual(area, (sp * (sp - a) * (sp - b) * (sp - c))**0.5)

    def test_square_area(self):
        a=4
        area=a*a
        self.assertEqual(area, a*a)

    def test_square_calculate_side_from_area(self):
        area=25
        side=area**0.5
        self.assertEqual(side, area**0.5)
        self.assertNotIsInstance(side, str,'Invalid side')





if __name__ == '__main__':
    unittest.main()
