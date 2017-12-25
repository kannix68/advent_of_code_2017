## Advent of code 2017, AoC day 25 pt1.
## This solution by kannix68, @ 2017-12-25.
## tested on python 3.6

#from time import gmtime, localtime, time, strftime
from collections import defaultdict, OrderedDict
import os.path
import re
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

def solve_test():
  state = 'A'
  numsteps = 6
  tape = defaultdict(int)
  tpos = 0
  for i in range(numsteps):
    val = tape[tpos]
    if state == 'A':
      if val == 0:
        tape[tpos] = 1
        tpos += 1
        state = 'B'
      elif val == 1:
        tape[tpos] = 0
        tpos -= 1
        state = 'B'
    elif state == 'B':
      if val == 0:
        tape[tpos] = 1
        tpos -= 1
        state = 'A'
      elif val == 1:
        #tape[tpos] = 1 # same
        tpos += 1
        state = 'A'
  print("tape={}".format( OrderedDict(sorted(tape.items())) ))
  numones = len(list(filter(lambda v: v > 0, tape.values())))
  print("num 1s={}".format(numones))
  return numones

def solve():
  state = 'A'
  numsteps = 12386363
  tape = defaultdict(int)
  tpos = 0
  for i in range(numsteps):
    val = tape[tpos]
    if state == 'A':
      if val == 0:
        tape[tpos] = 1
        tpos += 1
        state = 'B'
      elif val == 1:
        tape[tpos] = 0
        tpos -= 1
        state = 'E'
    elif state == 'B':
      if val == 0:
        tape[tpos] = 1
        tpos -= 1
        state = 'C'
      elif val == 1:
        tape[tpos] = 0
        tpos += 1
        state = 'A'
    elif state == 'C':
      if val == 0:
        tape[tpos] = 1
        tpos -= 1
        state = 'D'
      elif val == 1:
        tape[tpos] = 0
        tpos += 1
        state = 'C'
    elif state == 'D':
      if val == 0:
        tape[tpos] = 1
        tpos -= 1
        state = 'E'
      elif val == 1:
        tape[tpos] = 0
        tpos -= 1
        state = 'F'
    elif state == 'E':
      if val == 0:
        tape[tpos] = 1
        tpos -= 1
        state = 'A'
      elif val == 1:
        tape[tpos] = 1
        tpos -= 1
        state = 'C'
    elif state == 'F':
      if val == 0:
        tape[tpos] = 1
        tpos -= 1
        state = 'E'
      elif val == 1:
        tape[tpos] = 1
        tpos += 1
        state = 'A'
  #print("tape={}".format( OrderedDict(sorted(tape.items())) ))
  print("tape len", len(tape.keys()))
  numones = len(list(filter(lambda v: v > 0, tape.values())))
  print("num 1s={}".format(numones))
  return numones

## MAIN
teststr = """
Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
"""

res = solve_test()
assert_msg(3, res, "equality expected")
#sys.exit(0)

#datastr = ""
#datafilename = os.path.basename(__file__)[:5]+".in" # day22.in
#with open(datafilename, 'r') as datafile:
#  datastr = datafile.read()
#print("problem datastr=", datastr)

res = solve()
print("problem result=", res)
print("end.")
