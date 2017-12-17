## Advent of code 2017, AoC day 17 pt1.
## This solution by kannix68, @ 2017-12-11.
## tested on python 3.6

## LIB
def assert_msg(expected, term, msg):
  assert term == expected, "ERROR on assert, got={} but expected={}: {}".format(term, expected, msg)
  print("assert-OK result={}: {}".format(expected, msg))

## PROB
def solve(steps, numiters):
  lst = [0]
  lstptr = 0
  lstlen = len(lst)
  insval = 0
  #print("ptr={}, len={}, list={}".format(lstptr,lstlen,lst))
  for i in range(numiters):
    insval += 1
    lstptr += steps
    lstptr = (lstptr % lstlen) + 1
    #print("  lstptr={} insval={}".format(lstptr, insval))
    lst.insert(lstptr, insval)
    lstlen = len(lst)
    #print("ptr={}, len={}, list={}".format(lstptr,lstlen,lst))
  lstptr = (lstptr+1) % lstlen
  ret = lst[lstptr]
  #print("returns", ret)
  return ret

## MAIN

steps = 3
numiters = 0
expct = 0
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))

numiters = 1; expct = 0
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))

numiters = 2; expct = 1
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))

numiters = 3; expct = 1
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))

numiters = 4; expct = 3
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))
numiters = 5; expct = 2
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))
numiters = 6; expct = 1
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))
numiters = 7; expct = 2
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))
numiters = 8; expct = 6
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))
numiters = 9; expct = 5
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))

datastr = ""
with open('day17.in', 'r') as datafile:
  datastr = datafile.read().rstrip()
steps = int(datastr)
print("problem steps=", steps)
res = solve(steps, 2017)
print("problem result=", res)
print("end.")
