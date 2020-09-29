from copy import deepcopy
from determinant import *

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def find_inverse(matrix):

    determinant = find_determinant(matrix)

    if determinant == 0:
        input("Determinant is zero, will not continue to solve for inverse")
        return None
    # placeholder matrix
    inverse_matrix = deepcopy(matrix) 

    # matrix of minor
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            minor = (find_determinant(getMatrixMinor(matrix, row, col)))
            inverse_matrix[row][col] = minor * (-1)**(row+col)

    # matrix of cofactors
    inverse_matrix = Transpose(inverse_matrix)

    # matrix of cofactors divided by determinant to get inverse
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            inverse_matrix[row][col] = inverse_matrix[row][col] / determinant

    return inverse_matrix

