from lesson_15.mosut_sorin.hw_lesson15_mosut_sorin_base_file import Triangle, Square
import unittest


class TestPolygins(unittest.TestCase):

    def test_triangle_class_has_proper_atributes(self):
        # arange
        l_1, l_2, l_3 = 2, 3, 4
        # act
        test_triangle = Triangle(l_1, l_2, l_3)
        s1, s2, s3 = test_triangle.sides
        # assert
        assert s1 == l_1 and s2 == l_2 and s3 == l_3, 'incorect Triangle object atributes'

    # def test_triangle_class_imposible_triangle_values(self):
    #     # arange
    #     l_1, l_2, l_3 = 1, 3, 4
    #     # act
    #     test_triangle = Triangle(l_1, l_2, l_3)
    #     s1, s2 ,s3 = test_triangle.sides
    #     # assert
    #     assert s1 == l_1 and s2 == l_2 and s3 == l_3, 'incorect Triangle object atributes'

    def test_triangle_object_area(self):
        # arange
        l_1, l_2, l_3 = 2, 3, 4
        # act
        test_triangle = Triangle(l_1, l_2, l_3)
        test_triangle_area = test_triangle.area()
        semi_per = (l_1 + l_2 + l_3) / 2
        refrence_area = (semi_per * (semi_per - l_1) * (semi_per - l_2) * (semi_per - l_3)) ** 0.5
        # assert
        assert test_triangle_area == refrence_area, 'incorect Triangle area result'

    def test_triangle_object_perimeter(self):
        # arange
        l_1, l_2, l_3 = 2, 3, 4
        # act
        test_triangle = Triangle(l_1, l_2, l_3)
        test_triangle_perimeter = test_triangle.perimeter()
        refrence_perimeter = l_1 + l_2 + l_3
        # assert
        assert test_triangle_perimeter == refrence_perimeter, 'incorect Triangle perimeter result'

    def test_square_class_has_proper_atributes(self):
        # arange
        l_1 = l_2 = l_3 = l_4 = 4
        # act
        test_square = Square(l_1, l_2, l_3, l_4)
        s1, s2, s3, s4 = test_square.sides
        # assert
        assert s1 == l_1 and s2 == l_2 and s3 == l_3 and s4 == l_4, 'incorect Square objects atributes'

    def test_square_object_area(self):
        # arange
        l_1 = l_2 = l_3 = l_4 = 4
        # act
        test_square = Square(l_1, l_2, l_3, l_4)
        test_square_area = test_square.area()
        refrence_area = l_1 ** 2
        # assert
        assert test_square_area == refrence_area, 'incorect Square area result'

    def test_square_object_from_area(self):
        # arange
        l_1 = l_2 = l_3 = l_4 = 5
        area = l_1 ** 2

        # act
        test_square_from_area = Square.from_area(area)
        test_square = Square(l_1, l_2, l_3, l_4)
        # assert
        assert test_square_from_area == test_square, 'incorect from_area result'


if __name__ == '__main__':
    unittest.main()
