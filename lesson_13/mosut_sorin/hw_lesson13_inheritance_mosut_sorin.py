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


class PerimeterMixin:

    def perimeter(self):
        return f'The perimeter of a {self.geometric_figure} with sides {self.sides} is {sum(self.sides):.2f}\n'


class Polygons(PerimeterMixin):

    def __init__(self, *args):
        self.sides = args

    def __str__(self):
        no_of_sides = len(self.sides)
        return '{} is the number of sides'.format(no_of_sides)

    def display(self):
        for side_index, length in enumerate(self.sides, start=1):
            print('Side {} with length: {:.2f}'.format(side_index, length))


class Triangle(Polygons):
    geometric_figure = 'Triangle'

    # `s(s-a)(s-b)(s-c) ** 0.5` where s = `(a+b+c) / 2`

    def __init__(self, *args):
        super().__init__(*args)
        s1, s2, s3 = self.sides
        if s1 >= s2 + s3 or s2 >= s1 + s3 or s3 >= s1 + s2:
            raise Exception('Triunghi imposibil')

    def area(self):
        s1, s2, s3 = self.sides
        s_p = sum(self.sides) / 2
        return f'The area of a {self.geometric_figure} with sides {self.sides} is : ' \
               f'{(s_p * (s_p - s1) * (s_p - s2) * (s_p - s3)) ** 0.5}\n'


class Square(Polygons):
    geometric_figure = 'Square'

    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        printing_format = str()
        for side_index, length in enumerate(self.sides, start=1):
            printing_format += 'Side {} with length: {:.2f}\n'.format(side_index, length)
        return printing_format

    def area(self):
        side, *_ = self.sides
        return f'The area of a {self.geometric_figure} with sides {self.sides} is : {side ** 2}\n'

    def from_area(area):
        side = float(f'{sqrt(area):.2f}')
        print(f'From the area = {area} of a square the side = {side}')
        return Square(side, side, side, side)


print()

triangle_1 = Triangle(3, 4, 5)

area_tri = triangle_1.area()
print(area_tri)

perimeter_tri = triangle_1.perimeter()
print(perimeter_tri)

square_1 = Square(5, 5, 5, 5)

area_square_1 = square_1.area()
print(area_square_1)

perimeter_square_1 = square_1.perimeter()
print(perimeter_square_1)

sq = Square.from_area(30)
print(sq)

perimeter_sq = sq.perimeter()
print(perimeter_sq)

imposible_triangle = Triangle(1, 2, 4)
