class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''

        for row in self.matrix:
            result += '\t'.join([str(el) for el in row]) + '\n'

        return result

    def __add__(self, other):
        result = self.matrix[:]

        for index_row, row in enumerate(self.matrix):
            for index_item, item in enumerate(row):
                result[index_row][index_item] = self.matrix[index_row][index_item] + other.matrix[index_row][index_item]

        return Matrix(result)


matrix_1 = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

matrix_2 = Matrix([
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18],
])

print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
