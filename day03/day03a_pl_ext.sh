#!/bin/sh

# code !stolen!
# see: [-- 2017 Day 3 Solutions -- : adventofcode](https://www.reddit.com/r/adventofcode/comments/7h7ufl/2017_day_3_solutions/)
# see: https://www.reddit.com/r/adventofcode/comments/7h7ufl/2017_day_3_solutions/dqoyypp/

# part 1
perl -pae '$o=1;do{$o+=2}until$s=$o**2>=$_;$_=--$o-($s-$_)%$o' < day03.in
echo ""

# part 1 - shaved off 8 chars thanks to Unihedron
perl -pae '$.+=2,until$s=$.**2>=$_;$_=--$.-($s-$_)%$.' < day03.in
echo ""
