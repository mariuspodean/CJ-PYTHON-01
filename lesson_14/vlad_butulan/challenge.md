##Matrix operations

Design a class that deals with matrix operations (sum and multiply) without importing any external libraries
Requirements:
 1) any matrix instance will be created from a nested list: [[1, 2, 3], [3, 2, 1]]
 2) the matrix class should check if input list is a matrix like:
    m1 = Matrix([1, 2], [3]) -> "input list is not a matrix"
 3) when using print(), the matrix should be displayed like this:
        [1, 3]
        [2, 4]
 4) use operator overloading so you can add two or more matrixes: M1 + M2
 5) use operator overloading so you can multiply two or more matrixes: M1 * M2
 6) the matrix class should check if '+' and '*' are possible:
    m1 = Matrix([1, 2], [3, 4])
    m2 = Matrix([1, 2, 3], [2, 3, 4]) -> "Incompatible matrixes for +"
 7) create a method "size()" that returns a string format like M(x, y)
         [1, 2, 3]
         [3, 2, 1]  ->  'M(2, 3)'
 8) create a method "T()" that transpose the matrix