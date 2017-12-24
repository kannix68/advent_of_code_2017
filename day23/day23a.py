## Advent of code 2017, AoC day 23 pt1.
## This solution by kannix68, @ 2017-12-23.
## tested on python 3.6

#from time import gmtime, localtime, time, strftime
from collections import defaultdict
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
regs = defaultdict(int)

def reg_or_int(s):
  if isint(s): # set a 1
    v = int(s)
  else:        # set a b
    v = regs[s]
  return v

def solve(s):
  rex = re.compile(r"^(\w+) ([\w]+) ?([\-\d\w]+)?$")
  instrct = 0
  instructs = []
  for line in s.splitlines():
    print("line=",line)
    m = rex.match(line)
    cmd, p1, p2 = m.group(1), m.group(2), m.group(3)
    fcmd = [cmd, p1, p2]
    print("fcmd #{} > {}".format(instrct, fcmd))
    instructs.append(fcmd)
    instrct += 1
  #regs = {}
  ptr = 0
  cmdct = 0
  mulct = 0
  proglen = len(instructs)
  while 1:
    if ptr >= proglen or ptr < 0:
      print("  program counter={} out of bounds, proglen={}".format(ptr, proglen))
      break
    cmdct += 1
    cmd, p1, p2 = instructs[ptr]
    print("intrct={}; regs={}".format(instructs[ptr], regs))
    if cmd == "set":
      regs[p1] = reg_or_int(p2)
      ptr += 1
    elif cmd == "sub":
      regs[p1] -= reg_or_int(p2)
      ptr += 1
    elif cmd == "mul":
      mulct += 1
      regs[p1] *= reg_or_int(p2)
      ptr += 1
    elif cmd == "jnz":
      if reg_or_int(p1) == 0:
        ptr += 1
      else:
        ptr += reg_or_int(p2)
    else:
      assert false, "unknown cmdset"
    if cmdct > 1e5: # failsafe
      print("  break on failsafe={}".format(1e5))
      break
  print("regs={}".format(regs))
  return mulct

## MAIN
teststr = ""

#res = solve(teststr)
#assert_msg(4, res, "equality expected")
#sys.exit(0)

datastr = ""
datafilename = os.path.basename(__file__)[:5]+".in" # day22.in
with open(datafilename, 'r') as datafile:
  datastr = datafile.read()
print("problem datastr=", datastr)

res = solve(datastr)
print("problem result=", res)
print("end.")
