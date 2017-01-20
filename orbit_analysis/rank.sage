import random

load matrix_2c.py

MS2C8 = MatrixSpace(GF(2), 18, 48)
Matrix2C8 = MS2C8(matrix_2c8)

MS2C3 = MatrixSpace(GF(2), 32, 48)
Matrix2C8 = MS2C3(matrix_2c8)

MS2C83 = MatrixSpace(GF(2), 18 + 32, 48)
Matrix2C3C = MS2C3C(matrix_2c8 + matrix_2c3)

Move = VectorSpace(GF(2), 48)
State2C = VectorSpace(GF(2), 18)
State3C = VectorSpace(GF(2), 32)

print ''
print 'The 2C8 matrix is:'
print Matrix2C8

print 'The rank of the 2C8 matrix is: ' + str(Matrix2C8.rank())

print ''
print 'The row space of the 2C8 matrix is: '
print Matrix2C8.row_space()

print ''
print 'The 2C3 matrix is:'
print Matrix2C3

print 'The rank of the 2C3 matrix is: ' + str(Matrix2C3.rank())

print ''
print 'The row space of the 2C3 matrix is: '
print Matrix2C3.row_space()

print ''
print 'The 2C8 + 2C3 matrix is:'
print Matrix2C83

print 'The rank of the 2C8 + 2C3 matrix is: ' + str(Matrix2C83.rank())

return
original_moves = Move([random.randint(0, 1) for b in range(120)])

scrambled_state = State3C(Matrix3C * original_moves)
solution = Matrix3C.solve_right(scrambled_state)
all_moves_that_solve_3c = solution + original_moves

state_2c_when_3c_solved = Matrix2C * all_moves_that_solve_3c
print 'Starting from a random scramble, when 3C are solved, the state of 2C orbit is: (zero means even permutation)'
print state_2c_when_3c_solved
