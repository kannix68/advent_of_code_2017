## Advent of code 2017, AoC day 10 pt2.
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
def knothash_round(inlist, cmdlist, curpos, skipsize):
  print("  inlist=", inlist)
  print("cmdlist=", cmdlist)
  lst = inlist
  lstlen = len(lst)
  cmdct = 0
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
  #return lst[0]*lst[1]
  return [lst, curpos, skipsize]

def decodeinputstr(s):
  return list(map(ord, list(s)))

def getinputlens(s):
  lst = decodeinputstr(s)
  lst += [17, 31, 73, 47, 23]
  return lst

def lst2densehashstr(lst):
  assert len(lst) == 256
  #a = 60
  #b = 13
  #c = a ^ b ^ 0
  #print("CC=", c)
  ofs = 0
  hashstr = ""
  for i in range(16):
    ofs = i * 16
    n = lst[ofs]^lst[ofs+1]^lst[ofs+2]^lst[ofs+3]^lst[ofs+4]^lst[ofs+5]^lst[ofs+6]^lst[ofs+7] \
        ^lst[ofs+8]^lst[ofs+9]^lst[ofs+10]^lst[ofs+11]^lst[ofs+12]^lst[ofs+13]^lst[ofs+14]^lst[ofs+15]
    print("ofs={}, n={} nx={}".format(ofs, n, hex(n)[-2:]))
    hashstr += hex(n)[-2:].replace("x","0")
  print("hashstr=", hashstr)
  return hashstr

def solve(s):
  lenlist = getinputlens(s)
  curpos = 0
  skipsize = 0
  lst = list(range(256)) # [0, ..., 255]
  print("lenlist={}".format(lenlist))
  iters = 64
  for i in range(iters):
    out = knothash_round(lst, lenlist, curpos, skipsize)
    lst, curpos, skipsize = out[0], out[1], out[2]
    #print("iter#{}, curpos={}, skipsize{}, list={}".format(i+1, curpos, skipsize, lst))
    print("iter#{}, curpos={}, skipsize={}".format(i+1, curpos, skipsize))
  #return 0
  return lst2densehashstr(lst)

## MAIN

teststr = "1,2,3"
res = decodeinputstr(teststr)
assert_msg([49,44,50,44,51], res, "equality expected for input={}".format(teststr))

res = getinputlens(teststr)
assert_msg([49,44,50,44,51, 17,31,73,47,23], res, "equality expected for input={}".format(teststr))

datastr = ""
with open('day10.in', 'r') as datafile:
  datastr = datafile.read().rstrip()

inp = ""
res = solve(inp)
#print("knothash64x input={}, result={}".format(inp, res))
assert_msg("a2582a3a0e66e6e86e3812dcb672a272", res, "equality expected for input={}.".format(inp))

inp = "AoC 2017"
res = solve(inp)
assert_msg("33efeb34ea91902bb2f59c9920caa6cd", res, "equality expected for input={}.".format(inp))

inp = "1,2,3"
res = solve(inp)
assert_msg("3efbe78a8d82f29979031a4aa0b16a9d", res, "equality expected for input={}.".format(inp))

inp = "1,2,4"
res = solve(inp)
assert_msg("63960835bcdc130f0b66d7ff4f6a5a8e", res, "equality expected for input={}.".format(inp))

inp = datastr
res = solve(inp)
print("problem output=", res)
print("end.")
