with open('day24.in','r') as f: lines = [x.strip() for x in f.readlines()]

def readStep(line):
    if not line: return None, 0
    if line[0] == 'e': return 'e', 1
    if line[0] == 'w': return 'w', 1
    if line[0:2] == 'se': return 'se', 2
    if line[0:2] == 'sw': return 'sw', 2
    if line[0:2] == 'nw': return 'nw', 2
    if line[0:2] == 'ne': return 'ne', 2
    raise ValueError()

def takeStep(c, step):
    x,y = c
    if step == 'e': return (x+1,y)
    if step == 'w': return (x-1,y)
    if step == 'nw': return (x-1,y-1)
    if step == 'ne': return (x,y-1)
    if step == 'sw': return (x,y+1)
    if step == 'se': return (x+1,y+1)
    raise ValueError()

tiles = {}

for line in lines:
    coord = (0,0)
    steps = []
    while line:
        step, size = readStep(line)
        line = line[size:]
        steps.append(step)
    coords = []
    for step in steps:
        coord = takeStep(coord, step)
        coords.append(coord)
    tiles[coord] = not tiles.get(coord,False)

count = lambda tiles: sum(1 for k,v in tiles.items() if v == True)
neighbors = lambda c: [(c[0]+n[0],c[1]+n[1]) for n in ((-1,-1),(-1,0),(0,1),(1,1),(1,0),(0,-1))]

def runDay(tiles):
    candidates = set()
    for c,v in tiles.items():
        if v:
            candidates.add(c)
            for _c in neighbors(c):
                candidates.add(_c)
    out = {}
    for c in list(candidates):
        s = sum(1 for _c in neighbors(c) if tiles.get(_c, False))
        if tiles.get(c,False) and s > 0 and s <= 2:
            out[c] = True
        elif not tiles.get(c,False) and s == 2:
            out[c] = True
    return out

print(count(tiles))
for i in range(100):
    tiles = runDay(tiles)
print(count(tiles))
