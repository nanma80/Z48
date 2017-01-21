#!/usr/bin/env python

from cell48 import *

def orbits_to_matrix(orbits):
  matrix = []

  for orbit in orbits:
    row = []
    for i in range(48):
      if i in orbit.moves:
        row.append(1)
      else:
        row.append(0)
    matrix.append(row)

  return matrix

cell48 = Cell48()

with open('matrix_2c.py', 'w') as f:
  f.write('matrix_2c8 = ' + str(orbits_to_matrix(cell48.face8_orbits)))
  f.write('\n')
  f.write('matrix_2c3 = ' + str(orbits_to_matrix(cell48.face3_orbits)))
  f.write('\n')
