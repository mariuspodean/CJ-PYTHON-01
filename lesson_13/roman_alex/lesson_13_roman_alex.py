from math import sqrt


class PerimeterMixin:

    def perimeter(self):
        return f'Perimeter is {sum(self.sides)}'


class Polygons:

    def __init__(self, *args):
        self.sides = args

    def __str__(self):
        no_of_sides = len(self.sides)
        return '{} is the number of sides'.format(no_of_sides)

    def display(self):
        for side_index, length in enumerate(self.sides, start=1):
            print('Side {} with length: {}'.format(side_index, length))


class Triangle(Polygons, PerimeterMixin):
    # `s(s-a)(s-b)(s-c) ** 0.5` where s = `(a+b+c) / 2`
    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        s1, s2, s3 = self.sides
        s_p = sum(self.sides) / 2
        return (s_p * (s_p - s1) * (s_p - s2) * (s_p - s3)) ** 0.5


class Square(Polygons):

    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        side, *_ = self.sides
        return side ** 2

    def __str__(self):
        print_string = str()
        for square_tuple_index, length in enumerate(self.sides, start=1):
            print_string += 'Side {} with length: {:.2f}\n'.format(square_tuple_index, length)
        return print_string

    def from_area(self):
        side = sqrt(self)
        print(f'Resulting square has a side of = {side}')
        return Square(side, side, side, side)


# testing area constructor
square = Square.from_area(30)

# testing display
print(square)

# testing perimeter mixin
triangle = Triangle(8, 9, 10)
print(triangle.perimeter())
