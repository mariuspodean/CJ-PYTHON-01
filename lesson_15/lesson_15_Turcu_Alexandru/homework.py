from math import sqrt


class Polygons():

    def __init__(self, *args):
        self.sides = args

    def __str__(self):
        no_of_sides = len(self.sides)
        return '{} is the number of sides'.format(no_of_sides)

    def display(self):
        for side_index, length in enumerate(self.sides, start=1):
            print('Side {} with length: {}'.format(side_index, length))


class PerimeterMixin:
    def perimeter(self):
        return sum(self.sides)


class Triangle(Polygons, PerimeterMixin):
    # `s(s-a)(s-b)(s-c) ** 0.5` where s = `(a+b+c) / 2`
    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        s1, s2, s3 = self.sides
        s_p = sum(self.sides) / 2
        return (s_p*(s_p - s1)*(s_p - s2)*(s_p - s3))** 0.5


class Square(Polygons):

    def __init__(self, *args, init_area=None):
        super().__init__(*args)
        self.init_area = init_area
        if self.init_area is not None:
            self.sides = [self.init_area ** 0.5] * 4

    def __str__(self):
        to_return = ''
        for side, index in enumerate(self.sides, start=1):
            to_return += 'Side {} with length: {} \n'.format(side, index)
        return to_return

    def area(self):
        side, *_ = self.sides
        return side ** 2

    @classmethod
    def from_area(cls, area):
        square_side = sqrt(area)
        self = cls(square_side)
        self.sides = 2

        return self


sq = Square.from_area(4)
random_square = Square(11)
print(random_square.area())
area_square = Square(init_area=121)
print(area_square)
print(area_square.sides)
random_triangle = Triangle(9, 5, 9)
print(random_triangle.perimeter())

