## Advent of code 2017, AoC day 18 pt1.
## This solution by kannix68, @ 2017-12-18.
## tested on python 3.6

#from time import gmtime, localtime, time, strftime
from collections import defaultdict
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
  regs = defaultdict(lambda: 0)
  ptr = 0
  cmdct = 0
  lastfreq = 0
  proglen = len(instructs)
  while 1:
    cmdct += 1
    cmd, p1, p2 = instructs[ptr]
    print("intrct={}; regs={}".format(instructs[ptr], regs))
    if cmd == "snd": # snd 4
      lastfreq = regs[p1]
      print("snd >>", lastfreq)
      ptr += 1
    elif cmd == "set":
      if isint(p2): # set a 1
        v = int(p2)
      else:         # set a b
        v = regs[p2]
      regs[p1] = v
      ptr += 1
    elif cmd == "add":
      if isint(p2): # add a 1
        v = int(p2)
      else:         # add a b
        v = regs[p2]
      regs[p1] += v
      ptr += 1
    elif cmd == "mul":
      if isint(p2): # mul a 2
        v = int(p2)
      else:         # mul a b
        v = regs[p2]
      regs[p1] *= v
      ptr += 1
    elif cmd == "mod":
      if isint(p2): # mod a 2
        v = int(p2)
      else:         # mod a b
        v = regs[p2]
      regs[p1] %= v
      ptr += 1
    elif cmd == "jgz":
      if isint(p1):
        j = int(p1)
      else:
        j = regs[p1]
      if isint(p2):
        v = int(p2)
      else:
        v = regs[p2]
      if j <= 0:
        ptr += 1
      else:
        ptr += v
    elif cmd == "rcv":
      if isint(p1): # rcv 1
        j = int(p1)
      else:         # rcv a
        j = regs[p1]
      if j == 0:
        ptr += 1
      else:
        break # search for this condition!
    else:
      assert false, "unknown cmdset"
    if cmdct > 10000: # failsafe
      break
  return lastfreq

## MAIN
teststr = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""

res = solve(teststr)
assert_msg(4, res, "equality expected")

#sys.exit(0)

datastr = ""
with open('day18.in', 'r') as datafile:
  datastr = datafile.read()
print("problem datastr=", datastr)

res = solve(datastr)
print("problem result=", res)
print("end.")
