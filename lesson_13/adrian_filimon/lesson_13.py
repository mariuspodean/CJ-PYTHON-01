from math import sqrt

class PerimeterMixin:
    def perimeter(self):

        class_name = type(self).__name__

        return f"This is the perimeter for {class_name}: {sum(self.sides)}"


class Polygon(PerimeterMixin):
    def __init__(self, *args):
        self.sides = args

    def __str__(self):
        no_of_sides = len(self.sides)
        return f"{no_of_sides} is the number of sides."

    def display(self):
        for side_index, length in enumerate(self.sides, start=1):
            print(f"Side {side_index} with length: {length}")


class Triangle(Polygon):
    # `s(s-a)(s-b)(s-c) ** 0.5` where s = `(a+b+c) / 2`
    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        a, b, c = self.sides
        s = sum(self.sides) / 2
        return s * (s - a) * (s - b) * (s - c) ** 0.5


class Square(Polygon):
    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        side, *_ = self.sides
        return side ** 2

    @classmethod
    def from_area(cls, area):
        sq = sqrt(area)
        return f"Length of side is {sq}"





p = Polygon(3, 4, 5, 8, 22)
print(p.perimeter())

t = Triangle(3, 4, 5)
print(t.area())
print(t.perimeter())

s = Square(4)
print(s.area())
print(s.perimeter())
sq = Square.from_area(25)

print(sq)

