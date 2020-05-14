from math import sqrt


class PerimetruMixin:

    def perimetru(self):
        class_name = type(self).__name__
        return 'The perimeter for {} is : {}'.format(class_name, sum(self.sides))


class Polygons():

    def __init__(self, *args):
        self.sides = args

    def __str__(self):
        no_of_sides = len(self.sides)
        return '{} is the number of sides'.format(no_of_sides)

    def display(self):
        for side_index, length in enumerate(self.sides, start=1):
            print('Side {} with length: {}'.format(side_index, length))


class Triangle(PerimetruMixin,Polygons):
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
    @classmethod
    def from_area(cls,area):
        print('Patratul are laturile de : {}'.format(round(sqrt(area))))
        for i in range(4): print('Side {} with lenght {}'.format(i + 1, round(sqrt(area))))


triunghi = Triangle(5, 5, 5)
triunghi.display()
print('_________________________________')
area_of_square=81
sq_from_area = Square.from_area(area_of_square)
print('_________________________________')
sq=Square(4,4,4,4)
print(sq)
print('Aria patratului este {}'.format(sq.area()))
print('_________________________________')
# print(sq.perimetru()) nu mai are Perimetrumixin
print(triunghi.perimetru())