import math


class Polygons:

    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return str(len(self.args))

    def display(self):
        for side_index, length in enumerate(self.args, start=1):
            print('Side {} with length: {}'.format(side_index, length))


class PerimeterMixin:
    def perimeter(self):
        return sum(self.args)


class Triangle(Polygons, PerimeterMixin):

    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        if len(self.args) == 3:
            half_perimeter = sum(self.args) / 2
            return (half_perimeter * (half_perimeter - self.args[0]) * (half_perimeter - self.args[1]) * (
                        half_perimeter - self.args[2])) ** 0.5
        else:
            return None


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

    def is_valid(self):
        valid = all(x == self.args[0] for x in self.args)
        if not valid:
            return 'Invalid square'

    def area(self):
        if len(self.args) == 4 and len(set(self.args)) == 1:
            return self.args[0] ** 2
        else:
            return None

    @classmethod
    def from_area(cls, area):
        square_side = int(math.sqrt(area))
        return cls(square_side, square_side, square_side, square_side)


random_square = Square(11)
print(random_square.area())
area_square = Square(init_area=121)
print(area_square)
print(area_square.sides)
random_triangle = Triangle(9, 5, 9)
print(random_triangle.perimeter())