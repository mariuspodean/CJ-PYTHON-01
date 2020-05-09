class Matrix(object):
    "your code here :) "


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
