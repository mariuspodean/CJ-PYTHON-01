class Matrix(object):
    def __init__(self, lst):
        self.lst = lst
        self.x_dim = len(self.lst[0])
        self.y_dim = len(self.lst)
        if not all([self.x_dim == len(line) for line in lst]):
            raise ValueError("input list is not a valid matrix")
    
    def size(self):
        return f'M({self.y_dim}, {self.x_dim})'

    def __str__(self):
        result = ""
        for line in self.lst:
            result += ("{}\n".format(line))
        return result

    def __repr__(self):
        return str(self.lst)
    
    def __add__(self, other):
        if self.x_dim != other.x_dim and self.y_dim != other.y_dim:
            raise ValueError("Incompatible matrixes for +")
        result = []
        for y in range(self.y_dim):
            result.append([self.lst[y][x] + other.lst[y][x] for x in range(self.x_dim)])
        return Matrix(result)
    
    def __mul__(self, other):
        if self.x_dim != other.y_dim and self.y_dim != other.x_dim:
            raise ValueError("Incompatible matrixes for *")
        result = []
        for y in range(self.y_dim):
            result.append([self.lst[y][x] * other.lst[x][y] for x in range(self.x_dim)])
        return Matrix(result)
    
    def T(self):
        new_lst = [[self.lst[Y][X] for Y in range(self.y_dim)] for X in range(self.x_dim)]
        return Matrix(new_lst)


if __name__ == '__main__':
    #Example:
    matrix1 = Matrix([[1,1], [2,2]])
    matrix2 = Matrix([[3,1], [4,1]])

    #Use these "asserts" for self-checking
    assert matrix1.size() == 'M(2, 2)'
    assert str(matrix1 + matrix2) == str(Matrix([[4,2], [6,3]])), "Sum not working. Expected result [[4,2], [6,3]]"
    assert str(matrix1 * matrix2) == str(Matrix([[3,4], [2,2]])), "Mul not working. Expected result [[3,4], [2,2]]"
    assert str(matrix2.T()) == str(Matrix([[3, 4], [1, 1]])), "Matrix transposing not working"
    print("The local tests are done.")
