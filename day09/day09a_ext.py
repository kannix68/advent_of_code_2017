# code !stolen!
# see: https://www.reddit.com/r/adventofcode/comments/7iksqc/2017_day_9_solutions/dqzi2h6/

#data = aoc.get_input()
f = open('day09.in', 'r')
#data = f.read()
part = 1

#s = data.lines()[0]
s = f.readline()
idx = 0

score_total = 0
uncanc = 0

stack = []
cscore = 0
garbage = False

while True:
    if idx >= len(s):
        break
    if s[idx] == "!":
        idx += 1
    elif garbage:
        if s[idx] == ">":
            garbage = False
        else:
            uncanc += 1
    elif s[idx] == "{":
        cscore += 1
        stack.append(cscore)
    elif s[idx] == "<":
        garbage = True
    elif s[idx] == "}":
        cscore -= 1
        score_total += stack.pop()
    idx += 1

if part == 1:
    result = score_total
else:
    result = uncanc

print(result)