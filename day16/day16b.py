## Advent of code 2017, AoC day 16 pt2.
## This solution by kannix68, @ 2017-12-16.
## tested on python 3.6
#
## memoization of seen transforation is key for performance!

import re
from time import gmtime, localtime, time, strftime

teststr = "s1,x3/4,pe/b"

## LIB
def assert_msg(expected, term, msg):
  assert term == expected, "ERROR on assert, got={} but expected={}: {}".format(term, expected, msg)
  print("assert-OK result={}: {}".format(expected, msg))

## PROB
def solve(initstr, moves, numiters):
  str = initstr
  strlen = len(initstr)
  rex = re.compile(r"^([sxp])([\d\w]+)/?([\d\w]+)?$")
  moveslst = moves.split(",")
  instrset = []
  for move in moveslst:
    m = rex.match(move)
    cmd, p1, p2 = m.group(1), m.group(2), m.group(3)
    instrset.append([cmd, p1, p2])
  trafos = {}
  foundct = 0
  for i in range(numiters):
    if i % 1000 == 0:
      #print("i=", i, ", trafos keysize=", len(trafos.keys()), ", foundcount=", foundct)
      i += 0
    key = str
    if key in trafos:
      str = trafos[key]
      foundct += 1
      continue
    for instr in instrset:
      if instr[0] == "s":
        p1 = int(instr[1])
        str = str[-p1:] + str[:strlen-p1]
      elif instr[0] == "x":
        p1, p2 = str[int(instr[1])], str[int(instr[2])]
        str = str.replace(p1, "_").replace(p2, p1).replace("_", p2)
      else: #elif cmd == "p":
        p1, p2 = instr[1], instr[2]
        str = str.replace(p1, "_").replace(p2, p1).replace("_", p2)
    trafos[key] = str
  print("  done iters=", i+1)
  return str

## MAIN

res = "abcde"
moves = teststr
numiters = 2
res = solve(res, moves, numiters)
assert_msg("ceadb", res, "equality expected for n={}".format(numiters))

datastr = ""
with open('day16.in', 'r') as datafile:
  datastr = datafile.read().rstrip()

print("start local time=", strftime("%Y-%m-%d %H:%M:%S", localtime()))
ts = time()

res = "abcdefghijklmnop"
moves = datastr
numiters = 1000*1000*1000
res = solve(res, moves, numiters)

tf = time() #localtime()
print("end local time=", strftime("%Y-%m-%d %H:%M:%S", localtime()))
td = int(tf - ts)
if numiters > 0:
  print("for iters={}, took time={} secs, per thds-iters={}".format(numiters, td, int((tf-ts)/(numiters/1000))))
print("problem result= {}".format(res))

print("end.")
