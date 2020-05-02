from math import sqrt


class Perimeter:

    def perimeter(self):
        class_name = type(self).__name__
        return f'The perimeter for {class_name} is {sum(self.sides)}.\n'


class Polygon(Perimeter):
    def __init__(self, *args):
        self.sides = args

    def __str__(self):
        no_of_sides = len(self.sides)
        return f"{no_of_sides} is the number of sides.\n"

    def display(self):
        for side_index, length in enumerate(self.sides, start=1):
            print(f"Side {side_index} with length: {length}.\n")


class Triangle(Polygon):
    # `s(s-a)(s-b)(s-c) ** 0.5` where s = `(a+b+c) / 2`
    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        class_name = type(self).__name__
        a, b, c = self.sides
        s = sum(self.sides) / 2
        return f"The {class_name}'s area is {s * (s - a) * (s - b) * (s - c) ** 0.5}."


class Square(Polygon):
    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        class_name = type(self).__name__
        side, *_ = self.sides
        return f"The {class_name}'s area is {side ** 2}."

    def from_area(self):
        class_name = type(self).__name__
        sq = sqrt(self)
        return f"The side length for is {sq}.\n"


p = Polygon(3, 4, 5, 5, 7, 8, 9)
print(p.perimeter())

t = Triangle(3, 4, 5)
print(t.area())
print(t.perimeter())

s = Square(5)
print(s.area())
print(s.perimeter())

sq = Square.from_area(25)
print(sq)
