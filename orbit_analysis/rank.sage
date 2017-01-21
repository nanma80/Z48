import random

load matrix_2c.py

MS2C8 = MatrixSpace(GF(2), 18, 48)
Matrix2C8 = MS2C8(matrix_2c8)

MS2C3 = MatrixSpace(GF(2), 32, 48)
Matrix2C3 = MS2C3(matrix_2c3)

MS2C83 = MatrixSpace(GF(2), 18 + 32, 48)
Matrix2C83 = MS2C83(matrix_2c8 + matrix_2c3)

Move = VectorSpace(GF(2), 48)
State2C8 = VectorSpace(GF(2), 18)
State2C3 = VectorSpace(GF(2), 32)

print ''
print 'The 2C8 matrix is:'
print Matrix2C8

print 'The rank of the 2C8 matrix is: ' + str(Matrix2C8.rank())
# 14 out of 18

print ''
print 'The row space of the 2C8 matrix is: '
print Matrix2C8.row_space()
# Vector space of degree 48 and dimension 14 over Finite Field of size 2

print ''
print 'The 2C3 matrix is:'
print Matrix2C3

print 'The rank of the 2C3 matrix is: ' + str(Matrix2C3.rank())
# 16 out of 32

print ''
print 'The row space of the 2C3 matrix is: '
print Matrix2C3.row_space()
# Vector space of degree 48 and dimension 16 over Finite Field of size 2

print ''
print 'The 2C8 + 2C3 matrix is:'
print Matrix2C83

print 'The rank of the 2C8 + 2C3 matrix is: ' + str(Matrix2C83.rank())
# 20 out of 50

bases = []
n_bases = 50
for index in range(n_bases):
    original_moves = Move([random.randint(0, 1) for b in range(48)])
    scrambled_state = State2C8(Matrix2C8 * original_moves)
    solution = Matrix2C8.solve_right(scrambled_state)
    all_moves_that_solve_2c8 = solution + original_moves

    state_2c3_when_2c8_solved = Matrix2C83 * all_moves_that_solve_2c8
    solution2c3 = Matrix2C83.solve_right(state_2c3_when_2c8_solved)
    bases.append(solution2c3)

MSbases = MatrixSpace(GF(2), n_bases, 48)
Matrix_bases = MSbases(bases)
Matrix_bases.rank()
Matrix_bases.row_space()

# 6
# Vector space of degree 48 and dimension 6 over Finite Field of size 2
# Basis matrix:
# [1 0 0 1 0 0 1 0 0 1 0 0 0 1 0 0 1 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
# [0 1 0 0 0 0 1 0 1 1 1 0 0 1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
# [0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
# [0 0 0 0 1 0 1 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
# [0 0 0 0 0 1 1 0 1 1 0 1 0 1 0 1 1 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
# [0 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]