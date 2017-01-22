#!/usr/bin/env python

import unittest
import math
from vector import Vector
from line import Line
from orbit import Orbit

class Cell48:
  def __init__(self):
    self.cells = self.populate_cells()

    distance_face8 = (1 - 1.0/math.sqrt(2))**2 + 0.5
    self.faces8 = self.populate_faces(distance_face8)
    self.face8_orbits = self.populate_face_orbits(self.faces8, 8)

    distance_face3 = 1
    self.faces3 = self.populate_faces(distance_face3)
    self.face3_orbits = self.populate_face_orbits(self.faces3, 6)
    self.populate_cell_nicknames()
    self.populate_face3_orbit_nicknames()

  def populate_cells(self):
    cells = []
    cells.extend(list(Vector((0, 0, 0, 1)).plus_minus_all_perm()))
    cells.extend(list(Vector((0.5, 0.5, 0.5, 0.5)).plus_minus()))

    norm = math.sqrt(2)
    cells.extend(list(Vector((0, 0, 1, 1), norm).plus_minus_all_perm()))

    return sorted(cells, key = lambda cell: - cell.value[3])

  def populate_faces(self, cell_distance):
    epsilon = 1e-6
    faces = []
    nc = len(self.cells)
    for i in range(nc):
      for j in range(nc):
        if (i < j):
          distance_square = self.cells[i].distance_to(self.cells[j])
          if distance_square < cell_distance + epsilon and distance_square > cell_distance - epsilon:
            faces.append(Line(self.cells[i], self.cells[j], set([i, j])))
    return faces

  def populate_face_orbits(self, original_faces, n_faces_per_orbit):
    orbits = []
    faces = original_faces[:]

    while len(faces) > 0:
      orbit = Orbit()
      face = faces[0]
      seed = faces.pop()
      orbit.add_line(seed)
      moves = list(seed.moves)
      axis = moves[0]
      for j in range(n_faces_per_orbit - 1):
        face_centers = [face.center() for face in faces]
        mirror_index = face_centers.index(seed.center().mirror_around(self.cells[axis]))
        seed = faces.pop(mirror_index)
        orbit.add_line(seed)
        moves = list(seed.moves)
        moves.remove(axis)
        axis = moves[0]

      orbits.append(orbit)

    return orbits

  def populate_cell_nicknames(self):
    self.cell_nicknames = ['C', 'D', 'B', 'F', 'L', 'R', 'U'] \
      + ['UBL', 'DBR', 'BRU', 'FRU', 'FLD', 'FLU', 'FRD', 'BLD'] \
      + ['U2', 'L2', 'F2', 'R2', 'B2', 'D2'] \
      + ['LU', 'BL', 'LD', 'FD', 'BU', 'FU', 'FL', 'FR', 'BD', 'RD', 'BR', 'RU'] \
      + [''] * 16

  def populate_face3_orbit_nicknames(self):
    self.face3_orbit_nicknames = []

class Cell48Tests(unittest.TestCase):
  def test_basic_counts(self):
    c = Cell48()
    assert len(c.cells) == 48
    assert len(c.faces8) == 48 * 6 / 2 # 144
    assert len(c.faces3) == 48 * 8 / 2 # 192

  def test_face_orbits(self):
    c = Cell48()
    assert isinstance(c.face8_orbits, list)
    assert len(c.face8_orbits) == 18
    for orbit in c.face8_orbits:
      assert orbit.move_count() == 8
      assert orbit.line_count() == 8
    
    assert isinstance(c.face3_orbits, list)
    assert len(c.face3_orbits) == 32
    for orbit in c.face3_orbits:
      assert orbit.move_count() == 6
      assert orbit.line_count() == 6

if __name__ == "__main__":
  unittest.main()
