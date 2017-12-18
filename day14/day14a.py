## Advent of code 2017, AoC day 14 pt1.
## This solution by kannix68, @ 2017-12-17.
## tested on python 3.6

from time import gmtime, localtime, time, strftime
from itertools import cycle
import sys

## LIB
def assert_msg(expected, term, msg):
  assert term == expected, "ERROR on assert, got={} but expected={}: {}".format(term, expected, msg)
  print("assert-OK result={}: {}".format(expected, msg))

## PROB
def knothash_round(inlist, cmdlist, curpos, skipsize):
  #print("  inlist=", inlist)
  #print("cmdlist=", cmdlist)
  lst = inlist
  lstlen = len(lst)
  cmdct = 0
  for cmd in cmdlist:
    cmdct += 1
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
        revlist = list(reversed(sublist))
        intmlist = revlist + restlist
        for i in range(lstlen):
          idx = (curpos + i) % lstlen
          lst[idx] = intmlist[i]
        curpos = (curpos + cmd + skipsize) % lstlen
        skipsize += 1
        break
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
    #print("ofs={}, n={} nx={}".format(ofs, n, hex(n)[-2:]))
    hashstr += hex(n)[-2:].replace("x","0")
  #print("hashstr=", hashstr)
  return hashstr

def knothashhex(s):
  lenlist = getinputlens(s)
  curpos = 0
  skipsize = 0
  lst = list(range(256)) # [0, ..., 255]
  #print("lenlist={}".format(lenlist))
  iters = 64
  for i in range(iters):
    out = knothash_round(lst, lenlist, curpos, skipsize)
    lst, curpos, skipsize = out[0], out[1], out[2]
    #print("iter#{}, curpos={}, skipsize={}".format(i+1, curpos, skipsize))
  return lst2densehashstr(lst)

def hex2binhash(s):
  num_of_bits = 4 #8
  scale = 16
  bhash = ""
  for hx in list(tmp):
    b = bin(int(hx, scale))[2:].zfill(num_of_bits)
    bhash += b
  return bhash  

## MAIN
teststr = "flqrgnkx"

rowstr = teststr + "-0"
tmp = knothashhex(rowstr)
out = hex2binhash(tmp)
print("test-hashrow0=", out)
print("  test-hashrow0 fix=", out[:8])
n = len(list(filter(lambda x: x == "1", list(out[:8]))))
print("    num1=", n)

rowstr = teststr + "-1"
tmp = knothashhex(rowstr)
out = hex2binhash(tmp)
print("test-hashrow1=", out)
print("  test-hashrow1 fix=", out[:8])
n = len(list(filter(lambda x: x == "1", list(out[:8]))))
print("    num1=", n)

rowstr = teststr + "-2"
tmp = knothashhex(rowstr)
out = hex2binhash(tmp)
print("test-hashrow2=", out)
print("  test-hashrow2 fix=", out[:8])
n = len(list(filter(lambda x: x == "1", list(out[:8]))))
print("    num1=", n)

datastr = ""
with open('day14.in', 'r') as datafile:
  datastr = datafile.read().rstrip()
print("problem datastr=", datastr)

num1s = 0
for i in range(128):
  inp = "{}-{}".format(datastr,i)
  tmp = knothashhex(inp)
  out = hex2binhash(tmp)
  n1 = len(list(filter(lambda x: x == "1", list(out))))
  num1s += n1

print("result={}".format(num1s))

sys.exit(0)


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
