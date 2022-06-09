class Cell:
    def __init__(self, count):
        self.count = count

    def __str__(self):
        return f'{self.count}'

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if (self.count - other.count) < 0:
            raise ValueError('Ячеек в первой клетке меньше, чем во второй')

        return Cell(self.count - other.count)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count / other.count)

    def make_order(self, number):
        result = ''

        for el in range(0, self.count, number):
            result += '*' * (number if (self.count - el) >= number else self.count - el) + '\n'

        return result


cell_1 = Cell(10)
cell_2 = Cell(7)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
# print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1)
print(cell_1.make_order(2))
print(cell_1.make_order(3))
print(cell_1.make_order(4))
