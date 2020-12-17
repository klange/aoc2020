with open('day17.in','r') as f:
    lines = [x.strip() for x in f.readlines()]

for dims in [3,4]:
    print("With a {}-dimensional space...".format(dims))
    space = {}

    def neighbors(coord):
        for x, y, z in [(x, y, z) for x in [-1,0,1] for y in [-1,0,1] for z in [-1,0,1]]:
            for t in [-1,0,1] if dims == 4 else [0]:
                if abs(x) <= 1 and abs(y) <= 1 and abs(z) <= 1 and abs(t) <= 1 and sum([abs(x),abs(y),abs(z), abs(t)]) != 0:
                    yield (coord[0] + x, coord[1] + y, coord[2] + z, coord[3] + t)

    for x, l in enumerate(lines):
        for y, c in enumerate(l):
            if c == '#':
                space[(x,y,0,0)] = c

    for i in range(6):
        nextState = {}
        checks = set(space.keys())
        for c in space.keys():
            for n in neighbors(c):
                if n not in checks:
                    checks.add(n)
        for c in list(checks):
            s = sum(1 if space.get(n) == '#' else 0 for n in neighbors(c))
            if (space.get(c) == '#' and s == 2) or s == 3:
                nextState[c] = '#'
        space = nextState
        print("After pass", i+1, "there are", sum(1 for c in space.values() if c == '#'), "cubes")
