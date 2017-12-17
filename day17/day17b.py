## Advent of code 2017, AoC day 17 pt2.
## This solution by kannix68, @ 2017-12-17.
## tested on python 3.6
#
## For part 2 you don't keep a list, because value 0
# is always at index 0 and you just have to watch index 1

from time import gmtime, localtime, time, strftime

## LIB
def assert_msg(expected, term, msg):
  assert term == expected, "ERROR on assert, got={} but expected={}: {}".format(term, expected, msg)
  print("assert-OK result={}: {}".format(expected, msg))

## PROB
def solve(steps, numiters):
  lstptr = 0
  lstlen = 1
  insval = 0
  ret = 0
  print("init: ptr={}, len={}".format(lstptr,lstlen))
  for i in range(numiters):
    insval += 1
    lstptr = ((lstptr+steps) % lstlen) + 1
    #print("  lstptr={}, insval={}, lstlen={}".format(lstptr, insval, lstlen))
    if lstptr == 1:
      ret = insval
    lstlen  += 1
  print("exit: ptr={}, len={}".format(lstptr,lstlen))
  print("returns", ret, " @idx=", lstptr)
  return ret

## MAIN

steps = 3
numiters = 0
expct = 0
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))

numiters = 1; expct = 1
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))

numiters = 2; expct = 2
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))

numiters = 3; expct = 2
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))

numiters = 4; expct = 2
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))
numiters = 5; expct = 5
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))
numiters = 6; expct = 5
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))
numiters = 7; expct = 5
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))
numiters = 8; expct = 5
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))
numiters = 9; expct = 9
res = solve(steps, numiters)
assert_msg(expct, res, "equality; expected={} for steps={}, iters={}".format(expct, steps, numiters))

datastr = ""
with open('day17.in', 'r') as datafile:
  datastr = datafile.read().rstrip()

print("start local time=", strftime("%Y-%m-%d %H:%M:%S", localtime()))
ts = time()

steps = int(datastr)
#numiters = 50*1000*1000
numiters = 50*1000*1000 #2017
print("problem steps=", steps, " iters=", numiters)

res = solve(steps, numiters)

tf = time() #localtime()
print("end local time=", strftime("%Y-%m-%d %H:%M:%S", localtime()))
td = int(tf - ts)
if numiters > 0:
  print("for iters={}, took time={} secs, per thds-iters={}".format(numiters, td, int((tf-ts)/(numiters/1000))))

print("problem result=", res)
print("end.")
