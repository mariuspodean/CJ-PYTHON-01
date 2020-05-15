from math import sqrt


class PerimeterMixin:
    def __init__(self):
        self.sides = None

    def perimeter(self):
        return sum(self.sides)


class Polygons(PerimeterMixin):
    def __init__(self, *args):
        super().__init__()
        self.sides = args


    def __str__(self):
        no_of_sides = len(self.sides)
        return '{} is the number of sides'.format(no_of_sides)

    def display(self):
        for side_index, length in enumerate(self.sides, start=1):
            print(f'side {side_index} with length: {length}')


class Triangle(Polygons):
    def __init__(self, *args):
        super().__init__(*args)
        s1, s2, s3 = self.sides
        if s1 > s2 + s3 or s2 > s1 + s3 or s3 > s1 + s2:
            raise Exception("Impossible Triangle!")

    def area(self):
        s1, s2, s3 = self.sides
        s_p = sum(self.sides) / 2

        return sqrt(s_p * (s_p - s1) * (s_p - s2) * (s_p - s3))


class Square(Polygons):
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        to_be_printed = str()
        for side_index, length in enumerate(self.sides, start=1):
            to_be_printed += 'Side {} with length: {:.2f} \n'.format(side_index, length)
        return to_be_printed

    def area(self):
        return self.sides[0] ** 2

    @staticmethod
    def from_area(area):

        side = float(f'{sqrt(area):.2f}')
        if (type(area) == float or type(area) == int) and area > 0:

            print(f'From the area = {area} of a square the side = {side} \n')

            return Square(side, side, side, side)
        else:
            raise Exception('The side cannot be calculated')


# tri = Triangle(1, 2, 3)
# print(tri.perimeter())
# print(tri.area())
# tri.display()
# pol = Polygons(2, 3, 4, 6)
# print(pol.perimeter())
#
# sq = Square.from_area(81)
# print(sq)
