#!/usr/bin/env python

import os
import datetime

filename_init = 'solved.log'
# filename_current = 'trying.log'
filename_current = 'solving.log'

n_stickers_per_cell = 1 + 6 + 8 + 36 + 24 # 
n_cells = 48

index_cell = [21] # 1
index_8face = [12, 18, 22, 36, 45, 59] # 6
index_3face = [3, 14, 16, 19, 24, 28, 39, 68] # 8
index_edge = [1, 2, 6, 7, 9, 10, 13, 15, 17, 20, 23, 26, 27, 30, 31, 33, 34, 37, 38, 41, 42, 44, 46, 48, 50, 52, 55, 56, 58, 60, 62, 65, 66, 69, 70, 72] # 36
index_vertex = [0, 4, 5, 8, 11, 25, 29, 32, 35, 40, 43, 47, 49, 51, 53, 54, 57, 61, 63, 64, 67, 71, 73, 74] # 24

index_types = [
  {'name': 'Cells', 'ind': index_cell, 'nColor':1},
  {'name': 'Octas', 'ind': index_8face, 'nColor':2},
  {'name': 'Trias', 'ind': index_3face, 'nColor':2},
  {'name': 'Edges', 'ind': index_edge, 'nColor':3},
  {'name': 'Verti', 'ind': index_vertex, 'nColor':4}]

def read_status(filename):
  file = open(filename,'r')
  counter = 0
  status_code = ''
  for line in file:
    counter += 1
    if counter <= 12:
      continue
    status_code += line[:-1]
    if counter > 40:
      break

  for line in file:
    timemille = line[7:]
    timedt = datetime.timedelta(milliseconds = eval(timemille))
    break
  
  file.close()
  
  status_for_cell = [status_code[i_cell * n_stickers_per_cell * 2 : (i_cell+1) * n_stickers_per_cell * 2] for i_cell in range(n_cells)]
  status = [ [ entry[i:i+2] for i in range(0, len(entry), 2)   ]        for entry in status_for_cell ]
  return (timedt, status)

def main():
  (initTime, initStatus) = read_status (filename_init)  
  (curTime, curStatus) = read_status (filename_current)

  progressVector = []
  for i in range(0, n_stickers_per_cell):
    progressVector.append(0)

  incomplete_indices = set()
  
  completedType = {}
  for type in index_types:
    completedType[type['name']] = 0
  
  
  for i in range(0,n_cells):
    for j in range(0,n_stickers_per_cell):
      if initStatus[i][j] == curStatus[i][j]:
        progressVector[j] += 1
      else:
        incomplete_indices.add(j)

    for type in index_types:
      flag = True
      for j in type['ind']:
        if initStatus[i][j] != curStatus[i][j]:
          flag = False
          break
      if flag:
        completedType [type['name']] += 1

  print '----------------------------------------------------------------------------'
  print 'Type \tSolved Pieces\tSolved Stickers\tPercentage\tCompleted Cells'
  print '----------------------------------------------------------------------------'
  
  for type in index_types:
    totalSolvedSticker = sum([progressVector[i] for i in type['ind']])
    totalSticker = n_cells * len(type['ind'])
    totalSolvedPiece = totalSolvedSticker/type['nColor']
    totalPiece = totalSticker/type['nColor']
    
    percentage = 100.0 * totalSolvedPiece / totalPiece
    
    print type['name']+': \t%4d/%4d, \t%4d/%4d, \t%6.2f'%(totalSolvedPiece, totalPiece, totalSolvedSticker,totalSticker,percentage)+'%, '+('\t%3d/%3d'%(completedType[type['name']],n_cells))
    
  print '----------------------------------------------------------------------------'
  hours = curTime.seconds/3600
  totalhours = curTime.days * 24 + hours
  minutes = (curTime.seconds%3600)/60
  minutesStr = str(100 + minutes)[1:]
  seconds = curTime.seconds%60
  secondsStr = str(100 + seconds)[1:]
  milliseconds = curTime.microseconds/1000
  millisecondsStr = str(1000 + milliseconds)[1:]
  print ('Current solving time is: %d:%s:%s.%s,   %s'%(totalhours, minutesStr, secondsStr, millisecondsStr,str(curTime)[:-3]))

if __name__ == '__main__':
  main()
