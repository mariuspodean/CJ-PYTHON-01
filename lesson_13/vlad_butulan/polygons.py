import math

class Polygons(object):
    def __init__(self, *args):
        self.args = args
    
    def __str__(self):
        return str(len(self.args))
    
    def sides(self):
        for index, value in enumerate(self.args, start=1):
            print(f'Side {index} with lenght: {value}')


class Perimeter(object):
    def perimeter(self):
        return sum(self.args)


class Triangle(Perimeter, Polygons):
    def __init__(self, *args):
        super().__init__(*args)
    
    def area(self):
        if len(self.args) == 3:
            half_perimeter = sum(self.args) / 2
            return (half_perimeter*(half_perimeter-self.args[0])*(half_perimeter-self.args[1])*(half_perimeter-self.args[2])) ** 0.5
        else:
            return None


class Square(Polygons):
    def __init__(self, *args):
        super().__init__(*args)

    def area(self):
        if len(self.args) == 4 and len(set(self.args)) == 1:
            return self.args[0] ** 2
        else:
            None
    
    @classmethod
    def from_area(cls, area):
        square_side = math.sqrt(area)
        return cls(square_side)


triangle1 = Triangle(2, 3, 2)
print(f'Triangle nr of sides(__str__()): {triangle1}')
print(f'Triangle area: {triangle1.area()}')
print(f'Triangle perimeter: {triangle1.perimeter()}')

square1 = Square(2, 2, 2, 2)
print(f'Square nr of sides: {square1}')
print(f'Square area: {square1.area()}')

square2 = Square.from_area(4)
square2.sides()