class PerimeterMixin:

    def perimeter(self):
        return f'perimeter is {sum(self.sides)}'


class Polygons(PerimeterMixin):

    def __init__(self, *args):
        self.sides = args

    def __str__(self):
        stringu = ''
        for side_index, length in enumerate(self.sides, start=1):
            stringu += f'side {side_index} with length: {length}\n'
        return stringu

    def display(self):
        for side_index, length in enumerate(self.sides, start=1):
            print(f'side {side_index} with length: {length}')


class Triangle(Polygons):

    def __index__(self, *args):
        super().__init__(*args)

    def area(self):
        s1, s2, s3 = self.sides
        ssum = sum(self.sides)/2
        return (ssum*(ssum-s1)*(ssum-s2)*(ssum-s3))**0.5


class Square(Polygons):

    def __init__(self, *args):
        super().__init__(*args * 4)

    def area(self):
        return f'area is {self.sides[0] ** 2}'

    def from_area(input_area):
        print(f'side size {input_area ** 0.5}')
        return Square(input_area ** 0.5)


poly = Polygons(2, 3, 4, 5)
poly.display()
print(poly)
print()
triunghi = Triangle(3, 4, 5)
triunghi.display()
print(triunghi)
print(triunghi.area())
print(triunghi.perimeter())
print()
patrat = Square(5)
patrat.display()
print(patrat)
print(patrat.area())

print('\ntest')
sq3 = Square(9**0.5)
print(sq3)
print('\ntest2')
sq = Square.from_area(64)
print(sq)
