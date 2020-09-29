from determinant import find_determinant
from copy import deepcopy

def cramers(matrix):

    constant_column = deepcopy(matrix)
    determinant_list = []
    
    # seperate constants from variables

    for row in constant_column:
        del row[:len(row)-1]

    for row in matrix:
        row.pop(-1)

    base_determinant = find_determinant(matrix)
    matrix_copy = deepcopy(matrix)

    for col in range(len(matrix_copy)):
        for row in range(len(matrix_copy)):
            matrix_copy[row][col] = constant_column[row][0]

        determinant_list.append(find_determinant(matrix_copy))
        matrix_copy = deepcopy(matrix)

    return [result/base_determinant for result in determinant_list]

a = [
    [5, 7, 3],
    [2, 4, 1]   
]
b = [
    [4, 1, 6],
    [3, 2, 7]
]
c = [
    [3, -2, 3],
    [-4, 6, -5]
]


print(f'solution set of system{a} are: {cramers(a)}')
print(f'solution set of system{b} are: {cramers(b)}')
print(f'solution set of system{c} are: {cramers(c)}')

