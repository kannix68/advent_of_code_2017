## Advent of code 2017, AoC day 13 pt2.
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
  #maxdelay = (klen+1)*(klen+1)
  maxdelay = klen*klen*klen*klen
  print("  maxdelay=", maxdelay-1)  
  valslst = list()
  valsdir = list()
  valsptr = list()
  for key in range(klen+1):
    valslst.append(kvdict[key])
    valsdir.append(1)
    valsptr.append(0)
  print("valslst={}".format(valslst))
  lastvalsdir = list(valsdir)
  lastvalsptr = list(valsptr)
  for delay in range(maxdelay): 
    if delay % 1000 == 0:
      print("try-delay={} !".format(delay))
    if delay > 0:
      for scn in range(klen+1): # advance all scanners
        scnpos = lastvalsptr[scn]
        scndir = lastvalsdir[scn]
        scnlen = valslst[scn]
        #print("scanner #{}: pos={}, dir={}, depth={}".format(scn, scnpos, scndir, scnlen))
        if scnlen == 0:
          tmp = 1 #print("  skip column without scanner")
        else:
          if scndir == 1 and scnpos < scnlen -1:
            tmp = 1 #print("  move dn")
          elif scndir == 1:
            #print("  invertdir to -")
            scndir = -scndir
          elif scndir == -1 and scnpos > 0:
            tmp = 1 #print("  move up")
          elif scndir == -1 and scnpos == 0:
            #print("  invertdir to +")
            scndir = -scndir
          scnpos += scndir
          lastvalsptr[scn] = scnpos
          lastvalsdir[scn] = scndir
    valsptr = list(lastvalsptr)
    valsdir = list(lastvalsdir)
    ok = 1
    for tm in range(klen+1):
      #print("time={}! scanners at:{}".format(tm, valsptr))
      if valslst[tm]>0 and valsptr[tm] == 0: # caught at col/tm by scanner at pos=0
        #print("caught at tmabs={}, tmrel/col={}, depth={}".format(tm+delay, tm, valslst[tm]))
        ok = 0
        break
      for scn in range(klen+1): # advance all scanners
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
            #print("  invertdir to -")
            scndir = -scndir
          elif scndir == -1 and scnpos > 0:
            tmp = 1 #print("  move up")
          elif scndir == -1 and scnpos == 0:
            #print("  invertdir to +")
            scndir = -scndir
          scnpos += scndir
          valsptr[scn] = scnpos
          valsdir[scn] = scndir
        #print("    new pos={}, dir={}".format(scnpos, scndir))
    if ok == 1:
      print("delay {} OK, break".format(delay))
      break
    else:
      #print("delay {} nok, continue".format(delay))
      tmp = 1
  if ok == 0:
    delay = -1
  return delay

## MAIN
teststr = """
0: 3
1: 2
4: 4
6: 4
"""

teststr = teststr.strip()
res = solve(teststr)
assert_msg(10, res, "equality expected for input={}.".format(teststr))
#sys.exit(0)

datastr = ""
datafilename = os.path.basename(__file__)[:5]+".in" # day22.in
with open(datafilename, 'r') as datafile:
  datastr = datafile.read().strip()
#print("problem datastr=", datastr)

res = solve(datastr)
print("problem output=", res)
print("end.")
