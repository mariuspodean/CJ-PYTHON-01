from random import randrange


class PerimeterMixin:

    def __init__(self, *args):
        self.sides = args

    def perimeter(self):
        # return f'the perimeter of triangle with {len(self.sides)} sides is {sum(self.sides)}'
        if len(self.sides) == 3:
            return f'the perimeter of triangle is {sum(self.sides)}'
        elif len(self.sides) == 4:
            return f'the perimeter of square is {sum(self.sides)}'
        elif len(self.sides) == 5:
            return f'the perimeter of pentagon is {sum(self.sides)}'
        elif len(self.sides) == 6:
            return f'the perimeter of hexagon is {sum(self.sides)}'


class Polygons(PerimeterMixin):

    def __init__(self, *args):
        super().__init__()
        self.sides = args

    def __str__(self):
        no_of_sides = len(self.sides)
        return '{} is the number of sides'.format(no_of_sides)

    def display(self):
        for side_index, length in enumerate(self.sides, start=1):
            print('Side {} with length: {}'.format(side_index, length))


class Triangle(Polygons):
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

    def from_area(self):
        #  build an Rectangle with same area as square
        area_rectangle, *_ = self.sides
        # rectangle area = L x l where we can choose s1 and s2 if we don't know which one is bigger
        s1 = randrange(1, stop=area_rectangle)  # choose a random number from 1 to area; if number is 1 in
        # order to obtain area we have to multiply with bigger no. example: at area 8 if s1 = 1 then s2 should be 8
        s2 = area_rectangle / s1
        rectangle_sides = (s1, s2, s1, s2)
        for rectangle_side_index, length in enumerate(rectangle_sides, start=1):
            print('Side {} with length: {:.2f}'.format(rectangle_side_index, length))


sq = Square(25)
print(sq.from_area())
tr = Triangle(8,9,10)
tr.display()
print(f'triangle area is {round(tr.area())}')
print(tr.perimeter())