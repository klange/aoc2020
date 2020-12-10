with open('day10.in','r') as f:
    lines = [int(l.strip())  for l in f.readlines()]

foo = [0] + sorted(lines)
foo += [foo[-1] + 3]

diffs = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
}

for i in range(0,len(foo)-1):
    diff = foo[i+1] - foo[i]
    diffs[diff] += 1

print(diffs[1] * diffs[3])

memo = {}
def recurse_arrangements(x):
    if x == len(foo)-1:
        return 1
    if x in memo: return memo[x]
    else:
        me = foo[x]
        c = 0
        for i in range(x+1,len(foo)):
            if foo[i] <= (me + 3):
                c += recurse_arrangements(i)
            else:
                break
        memo[x] = c
        return c

count = recurse_arrangements(0)
print(count)
