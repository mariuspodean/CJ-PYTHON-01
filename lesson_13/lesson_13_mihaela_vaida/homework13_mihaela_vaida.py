class PerimeterMixin:
    def perimeter(self):
        return f' The perimeter is : {sum(self.sides)}"'


class Polygons(PerimeterMixin):
    def __init__(self, *args):
        self.sides = args
        # if len(self.sides) < 3:
        #   raise Exception('This is not a polygon!')
        for side_index, lenght in enumerate(self.sides, start=1):
            if (type(lenght) != int or type(lenght) != float) and lenght <= 0:
                raise Exception('Invalid lenght !')

    def __str__(self):
        no_of_sides = len(self.sides)
        return '{} is the number of sides'.format(no_of_sides)

    def display(self):
        for side_index, lenght in enumerate(self.sides, start=1):
            print('Side {} with lenght {}'.format(side_index, lenght))


class Triangle(Polygons):
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
        return f' Area is {side ** 2}'

    def from_area(area):
        for i in range(0, 4):
            if (type(area) == float or type(area) == int) and area > 0:

                print('Side {}  with lenght {}'.format(i, area ** 0.5))
            else:
                raise Exception('The side cannot be calculated')

    def perimeter(self):
        return sum(self.sides) * 4


tri = Triangle(3.4, 3, 23)
tri.perimeter()
tri.area()
tri.display()
tri.__str__()
patrat = Square(2)
patrat.perimeter()  # 8
patrat.area()  # 4
Square.from_area(16)

# Side 0  with lenght 4.0
# Side 1  with lenght 4.0
# Side 2  with lenght 4.0
# Side 3  with lenght 4.0

Square.from_area(15)
# Side 0  with lenght 3.872983346207417
# Side 1  with lenght 3.872983346207417
# Side 2  with lenght 3.872983346207417
# Side 3  with lenght 3.872983346207417
