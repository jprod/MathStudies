#   !/usr/bin/env python
"""
Returns the row reduced echelon form of a i by i+1 matrix implemented
with numpy and recursion.

Input must be a valid matrix in a numpy array. 
"""

import numpy as np

matrix1 = np.array([[2., 5., 1., 23.], 
                    [7., 3., 4., 39.], 
                    [3., 2., 3., 24.]])
matrix2 = np.array([[2., 5., 3., 2., 41.], 
                    [1., 6., 7., 3., 63.],
                    [5., 0., 2., 4., 38.], 
                    [7., 3., 1., 5., 52.]])

def rref(arrayMatrix):
    """ Modifys the given matrix to row reduced echelon form """
    # Reduces the first row to a [1., x1, x2, ... , xn] form
    arrayMatrix[0] = np.divide(arrayMatrix[0], arrayMatrix[0,0])
    # If it is not the last row, preform other row operations
    if (len(arrayMatrix) > 1):
        # Reduces the other rows to a [0., x1, ... , xn] form
        arrayMatrix[1:] = np.array([arrayMatrix[row] - 
            (arrayMatrix[row,0] * arrayMatrix[0]) 
            for row in range(1, len(arrayMatrix))])
        # Recurses with a bottom right sub-matrix
        rref(arrayMatrix[1:,1:])
        # Reduces the first row to a [1., 0., 0., ... , xn] form 
        arrayMatrix[0] = np.array([arrayMatrix[0] - 
            sum([arrayMatrix[0,i] * arrayMatrix[i]
            for i in range(1, len(arrayMatrix))])])
    return arrayMatrix

print("Input:")
print(matrix1)
print("Output:")
print(rref(matrix1))
print("Input:")
print(matrix2)
print("Output:")
print(rref(matrix2))

input("Press enter to quit")
