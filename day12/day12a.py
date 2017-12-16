## Advent of code 2017, AoC day 12 pt 1.
## This solution by kannix68, @ 2017-12-15.
## tested on python 3.6
#
## uses NetworkX graph lib
## [Tutorial — NetworkX 2.0 documentation](<https://networkx.github.io/documentation/stable/tutorial.html>)

import networkx as nx

teststr = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
"""

## LIB
def assert_msg(assertion, msg):
  assert assertion, "ERROR on assert: {}".format(msg)
  print("assert-OK: {}".format(msg))

## PROB
def solve(str):
  g = nx.Graph()
  for line in str.splitlines():
    src, right = line.split(" <-> ")
    g.add_node(src)
    targets = right.split(", ")
    for trg in targets:
  	  g.add_node(trg)
  	  g.add_edge(src, trg)
  print("num nodes=", g.number_of_nodes())
  print("num edges=", g.number_of_edges())
  groups = list(nx.connected_components(g))
  print("num groups=", len(groups))
  groupsize = 0
  for grp in groups:
    print(grp)
    if "0" in grp:
      groupsize = len(grp)
      print("groupsize[gr:0]=", groupsize)
      break
  return groupsize

## MAIN

res = solve(teststr)
assert_msg(res==6, "{} expected, got {}".format(6, res))

with open('day12.in', 'r') as datafile:
  datastr = datafile.read() #.replace('\n', '')
  solve(datastr)

print("end.")
