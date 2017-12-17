## Advent of code 2017, AoC day 10 pt1.
## This solution by kannix68, @ 2017-12-17.
## tested on python 3.6
#

from time import gmtime, localtime, time, strftime
from itertools import cycle
import sys

## LIB
def assert_msg(expected, term, msg):
  assert term == expected, "ERROR on assert, got={} but expected={}: {}".format(term, expected, msg)
  print("assert-OK result={}: {}".format(expected, msg))

## PROB
def solve(inlist, cmdlist):
  print("  inlist=", inlist)
  print("cmdlist=", cmdlist)
  curpos = 0

  lst = inlist
  lstlen = len(lst)
  cmdct = 0
  skipsize = 0
  for cmd in cmdlist:
    cmdct += 1
    #print("cmd#{} ={}, curpos={}, skipsz={}".format(cmdct, cmd, curpos, skipsize))
    lpos = 0
    sublist = []
    restlist = []
    for lelem in cycle(lst):
      if lpos < curpos:
        lpos += 1
        continue
      elif len(sublist) < cmd:
        sublist.append(lelem)
      elif len(restlist) < lstlen-cmd:
        restlist.append(lelem)
      else:
        #print("lpos={}, sublist={}; restlist={}".format(lpos, sublist, restlist))
        revlist = list(reversed(sublist))
        #print("  revlist={}".format(revlist))
        intmlist = revlist + restlist
        #print("  intermed-list={}".format(intmlist))
        for i in range(lstlen):
          idx = (curpos + i) % lstlen
          lst[idx] = intmlist[i]
        #print("  final-list={}".format(lst))
        curpos = (curpos + cmd + skipsize) % lstlen
        skipsize += 1
        #print("  new curpos={} @val={}, new skipsize={}".format(curpos, lst[curpos], skipsize))
        break
  return lst[0]*lst[1]

## MAIN

teststr = "3,4,1,5"

inlist = list(range(5))

cmdlist = [3]
#res = solve(inlist, cmdlist)
#assert_msg(2, res, "equality expected")

cmdlist = [3, 4]
#res = solve(inlist, cmdlist)
#assert_msg(12, res, "equality expected")

cmdlist = [3, 4, 1]
#res = solve(inlist, cmdlist)
#assert_msg(12, res, "equality expected")

cmdlist = list(map(int, teststr.split(",")))
res = solve(inlist, cmdlist)
assert_msg(12, res, "equality expected")

#sys.exit(0)

datastr = ""
with open('day10.in', 'r') as datafile:
  datastr = datafile.read().rstrip()

print("start local time=", strftime("%Y-%m-%d %H:%M:%S", localtime()))
ts = time()

inlist = list(range(256))
cmdlist = list(map(int, datastr.split(",")))
print("problem cmds=", cmdlist)
print(  "problem initlst=", inlist)

res = solve(inlist, cmdlist)

tf = time() #localtime()
print("end local time=", strftime("%Y-%m-%d %H:%M:%S", localtime()))
td = int(tf - ts)
#if numiters > 0:
#  print("for iters={}, took time={} secs, per thds-iters={}".format(numiters, td, int((tf-ts)/(numiters/1000))))

print("problem result=", res)
print("end.")
