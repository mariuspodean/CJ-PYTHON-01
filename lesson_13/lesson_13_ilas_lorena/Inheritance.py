import math


class PerimeterMixin:

    def perimeter(self):
        return f'The perimeter is {sum(self.sides)}'


class Polygons:

    def __init__(self, *args):
        self.sides = args

    def __str__(self):
        n_of_sides = len(self.sides)
        return '{} is the number of sides'.format(n_of_sides)

    def display(self):
        for side_index, length in enumerate(self.sides, start=1):
            print('Side {} with length: {}'.format(side_index, length))


class Triangle(PerimeterMixin, Polygons):

    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        s1, s2, s3 = self.sides
        s_p = sum(self.sides) / 2
        return f'The triangle area is {math.sqrt(s_p * (s_p - s1) * (s_p - s2) * (s_p - s3))}'


class Square(Polygons):

    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        side, *_ = self.sides
        return f'The square area is {side ** 2}'

    @classmethod
    def from_area(cls, area):
        return f'The side length is {math.sqrt(area)}'


polygon = Polygons(4, 5, 6, 7, 9)
print(polygon)
polygon.display()

sq = Square.from_area(9)
print(sq)

sq2 = Square(6)
print(sq2.area())

tr = Triangle(3, 4, 5)
print(tr.perimeter())
print(tr.area())
