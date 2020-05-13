from math import sqrt


class Polygon:

    def __init__(self, *args):
        self.sides = args

    def __str__(self):
        no_of_sides = len(self.sides)
        return f"{no_of_sides} is the number of sides.\n"

    def display(self):
        for side_index, length in enumerate(self.sides, start=1):
            print(f"Side {side_index} with length: {length}.\n")


class Square(Polygon):

    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        class_name = type(self).__name__
        side, *_ = self.sides
        return side ** 2

    @classmethod
    def from_area(cls, sq):
        sq = sqrt(sq)
        return sq


class Perimeter:

    def perimeter(self):
        class_name = type(self).__name__
        return f'The perimeter for {class_name} is {sum(self.sides)}.\n'


class Triangle(Polygon, Perimeter):
    # `s(s-a)(s-b)(s-c) ** 0.5` where s = `(a+b+c) / 2`
    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        class_name = type(self).__name__
        a, b, c = self.sides
        s = sum(self.sides) / 2
        return f"The {class_name}'s area is {s * (s - a) * (s - b) * (s - c) ** 0.5}."


p = Polygon(3, 4, 5, 5, 7, 8, 9)


t = Triangle(3, 4, 5)
print(t.area())
print(t.perimeter())

s = Square(5)
print(s.area())

sq = Square.from_area(25)
print(sq)
