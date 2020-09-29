import numpy as np

class Matrix():

    def __init__(self, matrix=[]):
        self.matrix = matrix

    def __add__(self, other):
        return self.matrix + other.matrix

    def __sub__(self, other):
        return self.matrix - other.matrix

    def __mul__(self, other):
        return self.matrix * other.matrix

    def __str__(self):
        return f'{self.matrix}'

    def edit(self, n_shape):
        matrix = []

        for i in range((n_shape)):
            row = []
            for j in range((n_shape)):
                row.append(input(f'\t\tInput element for index({i},{j}): '))            

            matrix.append(row)

        self.matrix = np.asarray(matrix, dtype='uint32')

    def transpose(self):

        if self.matrix.size == 0:
            print('Please fill matrix first')

        else:
            return np.transpose(self.matrix)

    def inverse(self):
        if self.matrix.size == 0:
            print('Please fill matrix first')

        else:
            return np.linalg.inv(self.matrix)

    def determinant(self):

        if self.matrix.size == 0:
            print('Please fill matrix first')

        else:
            return np.linalg.det(self.matrix)
            


