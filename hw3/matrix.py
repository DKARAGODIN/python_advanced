import numpy as np


class Matrix:
    def __init__(self, matrix: np.ndarray | list[list] | list[np.ndarray]):
        if len(matrix) == 0:
            raise ValueError("Invalid input")
        cols = len(matrix[0])
        self.matrix = []
        for row in matrix:
            if len(row) != cols:
                raise ValueError("Invalid input")

            self.matrix.append([])
            for col in row:
                self.matrix[-1].append(col)

    def __add__(self, other):
        self._validate(other)
        new_matrix = []
        for i in range(len(self.matrix)):
            new_matrix.append([])
            for j in range(len(self.matrix[0])):
                new_matrix[-1].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(new_matrix)

    def __mul__(self, other):
        self._validate(other)
        new_matrix = []
        for i in range(len(self.matrix)):
            new_matrix.append([])
            for j in range(len(self.matrix[0])):
                new_matrix[-1].append(self.matrix[i][j] * other.matrix[i][j])
        return Matrix(new_matrix)

    def __matmul__(self, other):
        self._validate(other)
        new_matrix = []
        for i in range(len(self.matrix)):
            new_matrix.append([])
            for j in range(len(other.matrix[0])):
                new_matrix[-1].append(sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0]))))
        return Matrix(new_matrix)

    def __str__(self):
        output = ""
        for row in self.matrix:
            output += " ".join([str(col) for col in row]) + "\n"
        return output

    def __eq__(self, other):
        self._validate(other)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def _validate(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices do not have the same shape")


np.random.seed(0)
generated1 = np.random.randint(0, 10, (10, 10))
generated2 = np.random.randint(0, 10, (10, 10))

m1 = Matrix(generated1)
m2 = Matrix(generated2)

# Test
a = m1 + m2
if a == Matrix(generated1 + generated2):
    print("Addition works")
b = m1 * m2
if b == Matrix(generated1 * generated2):
    print("Multiplication works")
c = m1 @ m2
if c == Matrix(generated1 @ generated2):
    print("Matrix multiplication works")

with open("hw3_1/matrix+.txt", "w") as f:
    f.write(str(a))
with open("hw3_1/matrix_mul.txt", "w") as f:
    f.write(str(b))
with open("hw3_1/matrix@.txt", "w") as f:
    f.write(str(c))
