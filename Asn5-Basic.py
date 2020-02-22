# Assignment 5 - Basic question

#import librairies
import numpy as np
import random

# Create a numpy array and print contents
# Explore ndim, shape, size and dtype attributes

b1_array = np.array([1,22.4,5,35,4,6.7,3,8,40])

print(f'\nThe array contains: {b1_array}\n')

print(f'The dimensions of the array are: {b1_array.ndim}\nThe shape is: {b1_array.shape}\n'
      f'The size is: {b1_array.size}\nThe data type is: {b1_array.dtype}')

# Create a numpy matrix and print contents
# Explore ndim, shape, size and dtype attributes

b1_matrix = np.array([['a','b'], ['c', 'd'], [3,3]])

print(f'\nThe matrix contains:\n {b1_matrix}\n')

print(f'The dimensions of the matrix are: {b1_matrix.ndim}\nThe shape is: {b1_matrix.shape}\n'
      f'The size is: {b1_matrix.size}\nThe data type is: {b1_matrix.dtype}')

# Create a 1-dimensional numpy array with arange and rand functions

aranged_array = np.arange(0,10)
r_array= np.random.rand(1,10)

print(f'\nA 1-dim array using arange:\n\n{aranged_array}\n\nA 1-dim array of random numbers\n\n{r_array}')

# Create a 2-dimensional numpy matrix using zeros and rand functions

zeros_matrix = np.zeros((2,2), dtype=int)
random_matrix = np.random.rand(2,2)

print(f'\nA 2x2 matrix of zeros:\n{zeros_matrix}\n\nA 2x2 random number matrix:\n{random_matrix}')

# Create an array containing 20 times the value 7. Reshape it to a 4 x 5 Matrix

array_of_7s = np.full((1,20), 7, dtype=int)
matrix_of_7s = array_of_7s.reshape((4,5))

print(f'\n{matrix_of_7s}')

# Create a 6 x 6 matrix with all numbers up to 36, then print:
#
#     only the first element on it
#     only the last 2 rows for it
#     only the two mid columns and 2 mid rows for it
#     the sum of values for each column

matrix_36 = np.arange(1,37)

matrix_36 = matrix_36.reshape((6,6)); print('\n',matrix_36, '\n\n')

print(f'The first element is: {matrix_36[0,0]}\n'
      f'\nThe last two rows are:\n\n{matrix_36[4:,:]}\n'
      f'\nThe two mid columns are:\n\n{matrix_36[:,2:4]}\n'
      f'\nThe two mid rows are:\n\n{matrix_36[2:4,:]}\n'
      f'\nThe intersection of the mid-columns and rows is:\n\n{matrix_36[2:4,2:4]}\n\n')

print(f'The sum of the values for each column (1-6) is:\n\n{matrix_36.cumsum(axis=0)[-1,:]}')



