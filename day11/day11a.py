## Advent of code 2017, AoC day 11 pt1.
## This solution by kannix68, @ 2017-12-25.
## tested on python 3.6

#from time import gmtime, localtime, time, strftime
#from collections import defaultdict, OrderedDict
import os.path
#import re
import sys

## LIB
def assert_msg(expected, term, msg):
  assert term == expected, "ERROR on assert, got={} but expected={}: {}".format(term, expected, msg)
  print("assert-OK result={}: {}".format(expected, msg))

def isint(s):
  try: 
    int(s)
    return True
  except ValueError:
    return False

## PROB
# see: good explanation: https://www.redblobgames.com/grids/hexagons/
#  using flat topped grid/geometry and axial coordinates
#  using axis notation [q,r]
tr = {'n':[0,1], 's':[0,-1], 'nw':[-1,1], 'sw':[-1,0], 'ne':[1,0], 'se':[1,-1]}

def axial_to_cube(hex):
    x = hex[0]
    z = hex[1]
    y = -x-z
    return [x, y, z]

def cube_distance(a, b):
  return int((abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])) / 2)

def hex_distance(a, b):
  return int((abs(a[0] - b[0]) + abs(a[0] + a[1] - b[0] - b[1]) + abs(a[1] - b[1])) / 2)
  #return cube_distance(axial_to_cube(a), axial_to_cube(b))

def solve(s):
  pos = [0,0]
  movect = 0
  for move in s.split(","):
    movect += 1
    mv = tr[move]
    pos[0] += mv[0]
    pos[1] += mv[1]
    #print("moved mv={} ~ {}, new pos={}".format(move, mv, pos))
  print("final pos={}; moved {} moves".format(pos, movect))
  hexdist = hex_distance(pos, [0,0])
  print("hexdist=", hexdist)
  return hexdist

## MAIN
teststr = "ne,ne,ne"
res = solve(teststr)
assert_msg(3, res, "equality expected")

teststr = "ne,ne,sw,sw"
res = solve(teststr)
assert_msg(0, res, "equality expected")

teststr = "ne,ne,s,s"
res = solve(teststr)
assert_msg(2, res, "equality expected")

teststr = "se,sw,se,sw,sw"
res = solve(teststr)
assert_msg(3, res, "equality expected")
#sys.exit(0)

datastr = ""
datafilename = os.path.basename(__file__)[:5]+".in" # day22.in
with open(datafilename, 'r') as datafile:
  datastr = datafile.read().strip()
#print("problem datastr=", datastr)

res = solve(datastr)
print("problem result=", res)
print("end.")
