class PerimeterMixin:

    def perimeter(self):
        return sum(self.sides)

class Polygons:

    def __init__(self, *args):
        self.sides = args

    def __str__(self):
        no_of_sides = len(self.sides)
        return f'Number of sides: {no_of_sides}'

    def display(self):
        for side_idx, side_length in enumerate(self.sides, start=1):
            print(f'Side {side_idx} with length: {side_length}')


class Triangles(Polygons, PerimeterMixin):

    def __init__(self, *args):
        if len(args) > 3:
            raise Exception(f'Shape is not a triangle. Number of sides: {len(args)}')
        else:
            super().__init__(*args)

    # s(s-a)(s-b)(s-c) ** 0.5` where s = `(a+b+c) / 2
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
        return side ** 2

    @classmethod
    def from_area(cls, area):
        square_sides = area ** 0.5
        return cls(square_sides, square_sides, square_sides, square_sides)

    def __str__(self):
        sq_sides = str()
        for idx, length in enumerate(self.sides, start=1):
            sq_sides += f'Side {idx}: {length} \n'
        return sq_sides

triangle = Triangles(3, 4, 5)
print(triangle.__str__())
print(triangle.display())
print(triangle.area())
print(f'Triangle perimeter is: {triangle.perimeter()}')
print('---')

# other_shape = Triangles(1,2,3,4,5)
# print(f'Other shape perimeter is: {triangle.perimeter()}')
# print('---')

square = Square(5, 5, 5, 5)
print(square.area())


sq = Square.from_area(16)
print(sq)


