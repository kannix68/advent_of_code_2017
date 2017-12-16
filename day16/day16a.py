## Advent of code 2017, AoC day 16 pt1.
## This solution by kannix68, @ 2017-12-16.
## tested on python 3.6

import re

teststr = "s1,x3/4,pe/b"

## LIB
def assert_msg(expected, term, msg):
  assert term == expected, "ERROR on assert, got={} but expected={}: {}".format(term, expected, msg)
  print("assert-OK result={}: {}".format(expected, msg))

## PROB
def solve(initstr, moves):
  str = initstr
  strlen = len(initstr)
  ct = 0
  for move in moves.split(","):
    ct += 1
    m = re.search(r"^([sxp])([\d\w]+)/?([\d\w]+)?$", move)
    cmd, p1, p2 = m.group(1), m.group(2), m.group(3)
    laststr = str
    #print("cmd={}, p1={}, p2={}, laststr={}".format(cmd, p1, p2, laststr))
    if cmd == "s":
      bknum = int(p1)
      frnum = strlen-bknum
      bk = str[-bknum:]
      fr = str[:frnum]
      str = bk+fr
    elif cmd == "x":
      c1, c2 = str[int(p1)], str[int(p2)]
      str = str.replace(c1, "_").replace(c2, c1).replace("_", c2)
    elif cmd == "p":
      c1, c2 = p1, p2
      str = str.replace(c1, "_").replace(c2, c1).replace("_", c2)
    else:
      assert false, "unknown command {}".format(cmd)
    #print("swap cmd #{}  {} from {} to {}".format(ct, move, laststr, str))
  return str

## MAIN

res = solve("abcde", "s1")
assert_msg("eabcd", res, "equality expected")

res = solve("eabcd", "x3/4")
assert_msg("eabdc", res, "equality expected")

res = solve("eabdc", "pe/b")
assert_msg("baedc", res, "equality expected")

res = solve("abcde", teststr)
assert_msg("baedc", res, "equality expected")

with open('day16.in', 'r') as datafile:
  datastr = datafile.read().rstrip()
  res = solve("abcdefghijklmnop", datastr)
  print("problem result= {}".format(res))

print("end.")
