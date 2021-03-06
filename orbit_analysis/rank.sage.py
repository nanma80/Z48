# This file was *autogenerated* from the file rank.sage
from sage.all_cmdline import *   # import sage library
_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_48 = Integer(48); _sage_const_32 = Integer(32); _sage_const_18 = Integer(18)
import random

sage.repl.load.load(sage.repl.load.base64.b64decode("bWF0cml4XzJjLnB5"),globals(),False)

MS2C8 = MatrixSpace(GF(_sage_const_2 ), _sage_const_18 , _sage_const_48 )
Matrix2C8 = MS2C8(matrix_2c8)

MS2C3 = MatrixSpace(GF(_sage_const_2 ), _sage_const_32 , _sage_const_48 )
Matrix2C3 = MS2C3(matrix_2c3)

MS2C83 = MatrixSpace(GF(_sage_const_2 ), _sage_const_18  + _sage_const_32 , _sage_const_48 )
Matrix2C83 = MS2C83(matrix_2c8 + matrix_2c3)

Move = VectorSpace(GF(_sage_const_2 ), _sage_const_48 )
State2C8 = VectorSpace(GF(_sage_const_2 ), _sage_const_18 )
State2C3 = VectorSpace(GF(_sage_const_2 ), _sage_const_32 )

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

original_moves = Move([random.randint(_sage_const_0 , _sage_const_1 ) for b in range(_sage_const_48 )])

scrambled_state = State2C8(Matrix2C8 * original_moves)
solution = Matrix2C8.solve_right(scrambled_state)
all_moves_that_solve_2c8 = solution + original_moves

state_2c3_when_2c8_solved = Matrix2C3 * all_moves_that_solve_2c8
print 'Starting from a random scramble, when 2C8 are solved, the state of 2C3 orbit is: (zero means even permutation)'
print state_2c3_when_2c8_solved
