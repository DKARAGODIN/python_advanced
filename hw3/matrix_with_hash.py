import numpy as np


class Matrix():
    """key is hash of matrices that were multiplied together, value is the result of the multiplication."""
    matmul_cache: dict = {}

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
        h1 = hash(self)
        h2 = hash(other)
        if (h1, h2) in self.matmul_cache:
            return self.matmul_cache[(h1, h2)]

        new_matrix = []
        for i in range(len(self.matrix)):
            new_matrix.append([])
            for j in range(len(other.matrix[0])):
                new_matrix[-1].append(sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0]))))

        result = Matrix(new_matrix)
        self.matmul_cache[(h1, h2)] = result
        return result

    def dot_product(self, other):
        self._validate(other)
        new_matrix = []
        for i in range(len(self.matrix)):
            new_matrix.append([])
            for j in range(len(other.matrix[0])):
                new_matrix[-1].append(sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0]))))
        result = Matrix(new_matrix)
        return result

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

    def __hash__(self):
        """Hash the first element of the matrix."""
        return hash(self.matrix[0][0])

    def _validate(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices do not have the same shape")


A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])
C = Matrix([[1, 5], [10, 50]])
D = Matrix([[5, 6], [7, 8]])

with open("hw3_3/A.txt", "w") as f:
    f.write(str(A))
with open("hw3_3/B.txt", "w") as f:
    f.write(str(B))
with open("hw3_3/C.txt", "w") as f:
    f.write(str(C))
with open("hw3_3/D.txt", "w") as f:
    f.write(str(D))

if (hash(A) == hash(C)) and (A != C) and (B == D) and (A @ B != C @ D):
    print("Strange hashing works")

AB = A @ B
print(AB)

with open("hw3_3/AB.txt", "w") as f:
    f.write(str(AB))

CD = C.dot_product(D)
print(CD)

with open("hw3_3/CD.txt", "w") as f:
    f.write(str(CD))

CD_collision = C @ D
if AB == CD_collision:
    print("Collision works")

ab_hash = hash(AB)
cd_hash = hash(CD)

with open("hw3_3/hash.txt", "w") as f:
    f.write(str(ab_hash))
    f.write("\n")
    f.write(str(cd_hash))