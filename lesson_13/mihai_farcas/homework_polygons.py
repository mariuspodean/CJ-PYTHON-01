from math import sqrt

class Polygons(object):

    def __init__(self, *args):
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

    def from_area(area):
        print('Patratul are laturile de : {}'.format(sqrt(area)))
        for i in range(4): print('Side {} with lenght {}'.format(i + 1, sqrt(area)))

triunghi= Triangle(5,5,5)
# triunghi.area()
triunghi.display()
print('_________________________________')
sq = Square.from_area(4)
print(sq)
# s.display()
# print(s)
