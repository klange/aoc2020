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

stuff = [(j, int(others[j])) for j in range(len(others)) if others[j] != 'x']

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

diff = stuff[0][1]
t = diff
iterations = 1
foundset = set()
while True:
    for i in [i for i in range(len(stuff)) if (t + stuff[i][0]) % stuff[i][1] == 0 and i not in foundset]:
        print("Found bus",i,"at time",t,"with",iterations,"iterations")
        foundset.add(i)
        diff = lcm(diff, stuff[i][1])
    if len(foundset) == len(stuff):
        print(t)
        break
    t += diff
    iterations += 1

