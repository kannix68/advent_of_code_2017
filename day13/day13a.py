## Advent of code 2017, AoC day 13 pt1.
## This solution by kannix68, @ 2017-12-26.
## tested on python 3.6

#from time import gmtime, localtime, time, strftime
from collections import defaultdict #, OrderedDict
import os.path
#import re
import sys

## LIB
def assert_msg(expected, term, msg):
  assert term == expected, "ERROR on assert, got={} but expected={}: {}".format(term, expected, msg)
  print("assert-OK result={}: {}".format(expected, msg))


## PROB
def solve(s):
  keys = []
  vals = []
  kvdict = defaultdict(int) #{}
  for line in s.splitlines():
    key, val = list(map(int,line.split(": ")))
    kvdict[key] = val
  klen = max(kvdict.keys())
  #print("keys={}, vals={}".format(keys, vals))
  print("len={}, kvdict={}".format(klen, kvdict))
  valslst = list()
  valsdir = list()
  valsptr = list()
  for key in range(klen+1):
    valslst.append(kvdict[key])
    valsdir.append(1)
    valsptr.append(0)
  print("valslst={}".format(valslst))
  fireweight = 0
  for tm in range(klen+1):
    print("time={}! scanners at:{}".format(tm, valsptr))
    if valsptr[tm] == 0: # caught at col/tm by scanner at pos=0
      fweight = tm*valslst[tm]
      fireweight += fweight
      print("caught at col={}, depth={}, fweight={}, fireweight={}".format(tm, valslst[tm], fweight, fireweight))
    for scn in range(klen+1):
      scnpos = valsptr[scn]
      scndir = valsdir[scn]
      scnlen = valslst[scn]
      #print("scanner #{}: pos={}, dir={}, depth={}".format(scn, scnpos, scndir, scnlen))
      if scnlen == 0:
        tmp = 1 #print("  skip column without scanner")
      else:
        if scndir == 1 and scnpos < scnlen -1:
          tmp = 1 #print("  move dn")
        elif scndir == 1:
          print("  invertdir to -")
          scndir = -scndir
        elif scndir == -1 and scnpos > 0:
          tmp = 1 #print("  move up")
        elif scndir == -1 and scnpos == 0:
          print("  invertdir to +")
          scndir = -scndir
        scnpos += scndir
        valsptr[scn] = scnpos
        valsdir[scn] = scndir
      #print("    new pos={}, dir={}".format(scnpos, scndir))
  return fireweight

## MAIN
teststr = """
0: 3
1: 2
4: 4
6: 4
"""

teststr = teststr.strip()
res = solve(teststr)
assert_msg(24, res, "equality expected for input={}.".format(teststr))

datastr = ""
datafilename = os.path.basename(__file__)[:5]+".in" # day22.in
with open(datafilename, 'r') as datafile:
  datastr = datafile.read().strip()
#print("problem datastr=", datastr)

res = solve(datastr)
print("problem output=", res)
print("end.")
