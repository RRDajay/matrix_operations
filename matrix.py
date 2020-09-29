import os
from itertools import starmap
from determinant import *
from inverse import *


def UserChoice(matrix):

    instruction = """
        Matrix A: {},
        Matrix B: {}

        1. Edit Matrix
        2. Add Matrix (A + B)
        3. Subtract Matrix (A - B)
        4. Multiply Matrix
        5. Transpose 
        6. Find Matrix Inverse
        7. Find Matrix Determinant
        """.format(matrix.matrix_A, matrix.matrix_B)
    choice = int(input(instruction+"\nEnter desired operation: "))
    
    if choice == 1:
        matrix.edit_matrix()

    elif choice == 2:
        matrix.add()

    elif choice == 3:
        matrix.subtract()

    elif choice == 4:
        matrix.multiply()

    elif choice == 5:
        matrix.transpose()

    elif choice == 6:
        matrix.inverse()
        
    elif choice == 7:
        matrix.determinant()
    
    else:
        pass

    os.system('cls')

class Matrix():

    def __init__(self):

        self.matrix_A = [
            [1,2],
            [3,4]
        ]

        self.matrix_B = [
            [5,6],
            [7,8]
        ]

        # self.matrix_A = []
        # self.matrix_B = []
        
    def edit_matrix(self): 

        # Input size of square matrix, eg (2x2), (3x3), ...etc
        matrix = []

        selected_matrix = input('\tInput matrix to be edited (A or B): ')

        n_shape = int(input('\tInput shape of matrix: (if 3, matrix will be 3x3): '))

        for i in range((n_shape)):
            row = []
            for j in range((n_shape)):
                row.append(int(input(f'\t\tInput element for index({i},{j}): ')))            

            matrix.append(row)

        if selected_matrix == 'A':
            self.matrix_A = matrix

        else:
            self.matrix_B = matrix

    def add(self):

        result = []
        
        if len(self.matrix_A) != len(self.matrix_B):
            input("Matrix dimensions doesn't match")

        else:
            for (a_element, b_element) in zip(self.matrix_A, self.matrix_B):

                addition = list(map(lambda x, y: x + y, a_element, b_element))
                result.append(addition)

        
            input("""\n{} - {}\n\nResult: {} \n\nPress any key to continue..."""
                    .format(self.matrix_A, self.matrix_B, result))

    def subtract(self):

        result = []

        if len(self.matrix_A) != len(self.matrix_B):
            input("Matrix dimensions doesn't match")

        else:
    
            for (a_element, b_element) in zip(self.matrix_A, self.matrix_B):

                subtraction = list(map(lambda x, y: x - y, a_element, b_element))
                result.append(subtraction)

            
            input("""\n{} - {}\n\nResult: {} \n\nPress any key to continue..."""
                    .format(self.matrix_A, self.matrix_B, result))

    def multiply(self):

        result = deepcopy(self.matrix_A)

        if len(self.matrix_A) != len(self.matrix_B):
            input("Matrix dimensions doesn't match")

        else:

            result = [[sum(a_element*b_element for a_element, b_element in zip(A_row, B_col)) for B_col in zip(*self.matrix_B)] for A_row in self.matrix_A]

            input("""{} x {} = {}""".format(self.matrix_A, self.matrix_B, result))
        

    def inverse(self):
        
        select_matrix = input('Find inverse of matrix A or matrix B (A or B)? ')

        if select_matrix == 'A':
            input("""\Inverse of {}: {} \n\nPress any key to continue..."""
                .format(self.matrix_A, find_inverse(self.matrix_A)))
        else:
            input("""\Inverse of {}: {} \n\nPress any key to continue..."""
                .format(self.matrix_A, find_inverse(self.matrix_A)))
        
    def determinant(self):
        
        select_matrix = input('Find determinant of matrix A or matrix B (A or B)? ')

        if select_matrix == 'A':
            input("""\nDeterminant of {}: {} \n\nPress any key to continue..."""
                .format(self.matrix_A, find_determinant(self.matrix_A)))
        else:
            input("""\nDeterminant of {}: {} \n\nPress any key to continue..."""
                .format(self.matrix_A, find_determinant(self.matrix_A)))

    def transpose(self):
        
        select_matrix = input('Find Transpose of matrix A or matrix B (A or B)?')

        if select_matrix == 'A':

            input("""\Transpose of {} is {} \n\nPress any key to continue..."""
                .format(self.matrix_A, Transpose(self.matrix_A)))
        else:
            input("""\Transpose of {} is {} \n\nPress any key to continue..."""
                .format(self.matrix_B, Transpose(self.matrix_B)))

    def __str__(self):
        return (f'Given Matrix:\n\n\tMatrix A: {self.matrix_A}\n\tMatrix B: {self.matrix_B}\n')





