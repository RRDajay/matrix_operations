from copy import deepcopy

def square_matrix(matrix):
    
    num_rows = len(matrix)

    for row in matrix:

        if len(row) != num_rows:
            return False

    return True

def find_determinant(matrix): # recursion
    if square_matrix(matrix):
        # base class
        if len(matrix) == 2:
            return matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]

        elif len(matrix) == 1:
            return matrix[0][0]
        else:
            determinant = 0
            for col in range(len(matrix)):
                cofactor = (-1) ** (0+col) * matrix[0][col] * find_determinant(cofactor_expansion(matrix, 0, col))
                determinant += cofactor
            return determinant
    else:
        print('Check matrix dimensions')
        return None

def cofactor_expansion(matrix, row, col):
    cofactor_matrices = deepcopy(matrix)
    cofactor_matrices.remove(matrix[row])
    for i in range(len(cofactor_matrices)):
        cofactor_matrices[i].pop(col)

    return cofactor_matrices

def Transpose(matrix):

    transpose = list(map(list,zip(*matrix)))
    
    return transpose

