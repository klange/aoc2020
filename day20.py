from collections import deque, defaultdict

with open('day20.in','r') as f:
    lines = [x.strip() for x in f.readlines()]

tiles = []

class Tile(object):
    def __init__(self, number, lines):
        self.number = number
        self.lines = lines
        self.placed = False
        self.x = None
        self.y = None
        self.orientation = None
        self.edges = None
        self.inner = None

    def getEdges(self, v, h, r):
        if self.placed:
            return self.edges

        start = [
            self.lines[0],
            ''.join(x[-1] for x in self.lines),
            ''.join(self.lines[-1][::-1]),
            ''.join(x[0] for x in self.lines[::-1])
        ]

        if v:
            start[0], start[2] = ''.join(start[2][::-1]), ''.join(start[0][::-1])
            start[3], start[1] = ''.join(start[3][::-1]), ''.join(start[1][::-1])

        if h:
            start[1], start[3] = ''.join(start[3][::-1]), ''.join(start[1][::-1])
            start[2], start[0] = ''.join(start[2][::-1]), ''.join(start[0][::-1])

        if r:
            start[3], start[0], start[1], start[2] = start[0], start[1], start[2], start[3]

        return start

    def getInner(self, row):
        return self.inner[row]

    def coords(self):
        assert self.placed
        return self.y, self.x

    def place(self, y, x, orientation):
        assert not self.placed
        self.edges = self.getEdges(*orientation)
        self.orientation = orientation
        self.placed = True
        self.y = y
        self.x = x
        self.inner = []
        tmp = {}
        w = len(self.lines[0])
        for y in range(0, w):
            for x in range(0, w):
                tmp[(y,x)] = self.lines[y][x]
        if orientation[0]:
            tmp = {(w - y - 1, x): v for (y,x),v in tmp.items()}
        if orientation[1]:
            tmp = {(y, w - x - 1): v for (y,x),v in tmp.items()}
        if orientation[2]:
            tmp = {(w - x - 1, y): v for (y,x),v in tmp.items()}
        for y in range(w):
            self.inner.append([])
            for x in range(w):
                self.inner[y].append(tmp[(y,x)])

    def compare(self, myState, other, theirState):
        mine = self.edges if myState == None else self.getEdges(*myState)
        theirs = other.getEdges(*theirState)

        if mine[0] == ''.join(theirs[2][::-1]):
            yield (-1,0)

        if mine[1] == ''.join(theirs[3][::-1]):
            yield (0,1)

        if mine[2] == ''.join(theirs[0][::-1]):
            yield (1,0)

        if mine[3] == ''.join(theirs[1][::-1]):
            yield (0,-1)

collecting = None
data = []
for line in lines:
    if line.startswith("Tile "):
        collecting = line.replace("Tile ","").replace(":","")
    elif not line:
        tiles.append(Tile(collecting, data))
        data = []
    else:
        data.append(line)

searchSpace = set((h,v,r) for h in [0,1] for v in [0,1] for r in [0,1])
corners = []
links = {}

for tile in tiles:
    links[tile] = {}
    potentialplacements = defaultdict(lambda: [])
    for other in [t for t in tiles if t != tile]:
        for theirs in searchSpace:
            for result in tile.compare((0,0,0), other, theirs):
                links[tile][result] = (other, theirs)
                potentialplacements[result].append((other, theirs))
    if len(potentialplacements) < 3:
        corners.append((tile, potentialplacements))

n = 1
for corner, placements in corners:
    n *= int(corner.number)
print(n, ','.join(corner.number for corner, placements in corners))

goodcorner = None
for corner, placements in corners:
    if (0,1) in placements and (1,0) in placements:
        print("Starting from corner", corner.number)
        goodcorner = corner
        break

if not goodcorner:
    raise ValueError("no good corner, bail for now")

base = {(0,0): (goodcorner, 0, 0, 0)}
goodcorner.place(0,0,(0,0,0))

linking = deque([goodcorner])

while linking:
    tile = linking.pop()
    y,x = tile.coords()
    assert (y,x) in base
    for _, neighbor in links[tile].items():
        if neighbor[0].placed:
            continue
        n = 0
        for theirs in searchSpace:
            for (_y, _x) in tile.compare(None, neighbor[0], theirs):
                if (y+_y,x+_x) in base: continue
                base[(y+_y,x+_x)] = (neighbor[0], *theirs)
                linking.append(neighbor[0])
                neighbor[0].place(y+_y,x+_x, theirs)
                n += 1
        if n != 1:
            raise ValueError()

basesize = max([c[0].x for c in corners]) + 1

wholespace = []
for y in range(basesize):
    for row in range(8):
        line = ''.join(''.join(base[(y,x)][0].getInner(row+1)[1:9]) for x in range(basesize))
        wholespace.append(line)

size = len(wholespace)
assert len(wholespace[0]) == size

monster = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]

def isSeamonster(tmp, y, x, mark=False):
    for _y in range(0, 3):
        for _x in range(0, 20):
            if monster[_y][_x] == '#':
                try:
                    if tmp[(y+_y,x+_x)] != '#':
                        return False
                    elif mark:
                        tmp[(y+_y,x+_x)] = 'O'
                except:
                    return False
    return True

def tryIt(orientation):
    tmp = {}
    for y in range(0, size):
        for x in range(0, size):
            tmp[(y,x)] = wholespace[y][x]
    if orientation[0]:
        tmp = {(size - y - 1, x): v for (y,x),v in tmp.items()}
    if orientation[1]:
        tmp = {(y, size - x - 1): v for (y,x),v in tmp.items()}
    if orientation[2]:
        tmp = {(size - x - 1, y): v for (y,x),v in tmp.items()}
    count = 0
    for y in range(size):
        for x in range(size):
            if isSeamonster(tmp, y, x):
                isSeamonster(tmp, y, x, True)
                count += 1
    if count:
        print("Found",count,"monsters",count*15,orientation)
        for y in range(size):
            print(''.join([tmp[(y,x)] if tmp[(y,x)] != 'O' else '\033[31mO\033[0m' for x in range(size)]))
    return count

for orientation in searchSpace:
    count = tryIt(orientation)
    if count: break

c = 0
for line in wholespace:
    for ch in line:
        if ch == '#':
            c += 1
print("For a total of", c-count*15, "non-monster #'s'")
