"""
# Lesson 13 - Inheritance


We have new customers for our Polygons company.

    * They need to create square objects with a certain area

    * They need a method to compute the perimeter only for triangle objects

Requirements:

    * add an alternative constructor to Square class that takes the area as an
argument and creates a square object with the apropriate sides

> example :
>
>     >> sq = Square.from_area(4)
>     >> print(sq)
>     >> Side 1 with lenght: 2
>     >> Side 2 with lenght: 2
>     >> Side 3 with lenght: 2
>     >> Side 4 with lenght: 2


    * we want to make our perimeter method also available to other shapes in the future. Create a mixin

class for perimeter that contains the perimeter method
"""

from math import sqrt


# mixin class for calclate the perimeter of a instance of geometrig figures classes
class PerimeterMixin:

    def __init__(self, *args):
        self.sides = args

    def perimeter(self):
        perimeter = sum(self.sides)
        return perimeter


# main class
class Polygons:

    def __init__(self, *args):
        self.sides = args

    def __str__(self):
        no_of_sides = len(self.sides)
        return '- {} is the number of sides'.format(no_of_sides)

    # def display(self):
    #     for side_index, length in enumerate(self.sides, start=1):
    #         print('Side {} with length: {:.2f}'.format(side_index, length))


# class child define methods for Triangle instances
class Triangle(PerimeterMixin, Polygons):

    # `s(s-a)(s-b)(s-c) ** 0.5` where s = `(a+b+c) / 2`
    geometric_figure = 'Triangle'

    def __init__(self, *args):
        super().__init__(*args)
        s1, s2, s3 = self.sides
        if s1 >= s2 + s3 or s2 >= s1 + s3 or s3 >= s1 + s2:
            raise Exception('Triunghi imposibil')

    def __str__(self):
        printing_format = ''
        for side_index, length in enumerate(self.sides, start=1):
            printing_format += '- Side {} with length: {:.2f}\n'.format(side_index, length)
        return printing_format

    # methode calculate and return area of Triangle instance
    def area(self):
        s1, s2, s3 = self.sides
        s_p = sum(self.sides) / 2
        area = (s_p * (s_p - s1) * (s_p - s2) * (s_p - s3)) ** 0.5
        return area


# class child define methods for Square instances
class Square(Polygons):
    geometric_figure = 'Square'

    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        printing_format = ''
        for side_index, length in enumerate(self.sides, start=1):
            printing_format += 'Side {} with length: {:.2f}\n'.format(side_index, length)
        return printing_format

    # method calculate and return area from sides
    def area(self):
        side, *_ = self.sides
        area = side ** 2
        return area

    # calassmethod thet calculate a square from area an return a new Square instance
    @classmethod
    def from_area(cls, area):
        side = float(f'{sqrt(area):.2f}')
        return cls(side, side, side, side)


# Triangle exemple, create instance, print, calculate area, calculate perimeter
triangle_1 = Triangle(3, 4, 5)
print(f'{triangle_1.geometric_figure}:\n{triangle_1}')
area_tri = triangle_1.area()
print(f'The {triangle_1.geometric_figure} with:\n{triangle_1}has area: {area_tri}\n')
perimeter_triangle1 = triangle_1.perimeter
print(f'The {triangle_1.geometric_figure} with:\n{triangle_1}has the perimeter {perimeter_triangle1}\n')

# Square example , create instance , print , calculate area
square_1 = Square(5, 5, 5, 5)
print(f'{square_1.geometric_figure}:\n{square_1}')
area_square_1 = square_1.area()
print(f'The {square_1.geometric_figure} with:\n{square_1}has area: {area_square_1}\n')

# Square from area example
area_for_square = 16
new_square = Square.from_area(area_for_square)
print(f'From area {area_for_square} will get the {new_square.geometric_figure}:\n{new_square}')

# imposible triangle values - raise exceprion
imposible_triangle = Triangle(1, 2, 4)
