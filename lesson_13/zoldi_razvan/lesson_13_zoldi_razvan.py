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
        self.area = args

    # overwrite str from Polygons
    def __str__(self, *args):
        # return '{} is the area desired'.format(self.area[0])
        return ''

    def area(self):
        side, *_ = self.sides
        return side ** 2

    @classmethod
    def from_area(cls, area_rectangle):
        #  starting from known area and using random to generate one side ,
        #  build an Rectangle with same area as square
        print(f'Desired area to accomplish is: {area_rectangle}')
        s1 = randrange(1, stop=area_rectangle)
        s2 = area_rectangle / s1
        rectangle_sides = (s1, s2, s1, s2)
        for rectangle_side_index, length in enumerate(rectangle_sides, start=1):
            print('Side {} with length: {:.2f}'.format(rectangle_side_index, length))
        return cls(s1, s2)


print('Instantiate Polygons')
print('-' * 30)
polygon1 = Polygons(1, 2, 3, 4)
print(polygon1)
print(polygon1.display())
print('*' * 30)

print('Instantiate Triangle')
print('-' * 30)
tr = Triangle(8, 9, 10)
tr.display()
print(f'triangle area is {round(tr.area())}')
print(tr.perimeter())
print('*' * 30)

print('Instantiate Square')
print('-' * 30)
sq = Square(4)
print(sq)
# generate random polygons with desired area using @classmethod from Square
print('random polygon 1')
Square.from_area(32)
print('random polygon 2')
Square.from_area(32)
print('*' * 30)