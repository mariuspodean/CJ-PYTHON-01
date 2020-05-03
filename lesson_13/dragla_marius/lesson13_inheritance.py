class PerimeterMixin:

    def perimeter(self):
        return sum(self.sides)

class Polygons(PerimeterMixin):

    def __init__(self, *args):
        self.sides = args

    def __str__(self):
        no_of_sides = len(self.sides)
        return f'Number of sides: {no_of_sides}'

    def display(self):
        for side_idx, side_length in enumerate(self.sides, start=1):
            print (f'Side {side_idx} with length: {side_length}')


class Triangles(Polygons):
    # s(s-a)(s-b)(s-c) ** 0.5` where s = `(a+b+c) / 2
    def __init__(self, *args):
        if len(args) > 3:
            raise Exception(f'Shape is not a triangle. Number of sides: {len(args)}')
        else:
            super().__init__(*args)

    def area(self):
        s1, s2, s3 = self.sides
        s_p = sum(self.sides) / 2
        return f'Triangle area is {int((s_p*(s_p-s1)*(s_p-s2)*(s_p-s3)) ** 0.5)}'

    def __len__(self):
        return len(self.sides)


class Square(Polygons):

    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        side, *_ = self.sides
        return f'Square area is {side ** 2}'

    def from_area(self):
        return f'Square with side length of {int(self ** 0.5)}'


triangle = Triangles(3, 4, 5)
print(triangle.__str__())
print(triangle.display())
print(triangle.area())
print(f'Triangle perimeter is: {triangle.perimeter()}')
print('---')

other_shape = Triangles(1,2,3,4,5)
print(f'Other shape perimeter is: {triangle.perimeter()}')
print('---')

square = Square(5, 5, 5, 5)
print(square.area())
print(f'Square perimeter: {square.perimeter()}')

sq = Square.from_area(25)
print(sq)

# We have new customers for our Polygons company.
#
# * They need to create square objects with a certain area
# * They need a method to compute the perimeter only for triangle objects
#
# Requirements:
#
# * add an alternative constructor to Square class that takes the area as an argument and creates a square object with the apropriate sides
#
#     example:
#
#     >> sq = Square.from_area(8)
#     >> print(sq)
#     >> Side 1 with lenght: 2
#     >> Side 2 with lenght: 4
#     >> Side 3 with lenght: 2
#     >> Side 4 with lenght: 4
#
# * we want to make our perimeter method also available to other shapes in the future. Create a mixin class for perimeter that contains the perimeter method