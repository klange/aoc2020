with open('day13.in','r') as f:
    lines = [x.strip() for x in f.readlines()]

earliest = int(lines[0])
others = lines[1].split(',')
buses = [int(x) for x in others if x != 'x']

t = earliest
while True:
    if any([t % y == 0 for y in buses]):
        for y in buses:
            if t % y == 0:
                print("Found a bus at", t, y)
                print(y * (t - earliest))
        break
    else:
        t += 1

stuff = []
j = 0
for bus in others:
    if bus != 'x':
        stuff.append((j, int(bus)))
    j += 1

memo = {}
def gcd(a,b):
    if (min(a,b),max(a,b)) not in memo:
        _a, _b = a, b
        while b:
            a, b = b, a % b
        memo[min(a,b),max(a,b)] = a
    return memo[min(a,b),max(a,b)]

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def test(t):
    return all([(t + x) % y == 0 for (x, y) in stuff])


diff = stuff[0][1]
t = diff
n = 1
while True:
    if test(t):
        print(t)
        break
    else:
        diffs = [(t + x) % y for (x,y) in stuff]
        if diffs[n] == 0:
            diff = lcm(diff, stuff[n][1])
            n += 1
        t += diff

