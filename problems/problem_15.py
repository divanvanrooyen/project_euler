# Lattice Paths

# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

import math

matrix_y = 20
matrix_x = matrix_y * 2

paths = (math.factorial(matrix_x)) / (math.factorial(matrix_x - matrix_y) * math.factorial(matrix_y))

print(paths)
