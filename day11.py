with open('day11.in','r') as f:
    lines = [l.strip()  for l in f.readlines()]

#lines = """
#L.LL.LL.LL
#LLLLLLL.LL
#L.L.L..L..
#LLLL.LL.LL
#L.LL.LL.LL
#L.LLLLL.LL
#..L.L.....
#LLLLLLLLLL
#L.LLLLLL.L
#L.LLLLL.LL
#""".strip().split("\n")

def check(c, r, d, lines):
    while True:
        c += d[0]
        r += d[1]
        if c < 0 or c >= len(lines): return False
        if r < 0 or r >= len(lines[c]): return False
        if lines[c][r] == '#': return True
        if lines[c][r] == 'L': return False
        if lines[c][r] == '.': continue

def apply(c, r, lines):
    neighbors = [check(c, r, d, lines) for d in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]]
    if lines[c][r] == 'L' and (not any([n == True for n in neighbors])):
        return '#'
    elif lines[c][r] == '#' and sum([1 if x == True else 0 for x in neighbors]) >= 5:
        return 'L'
    # no change
    return lines[c][r]

def apply_round(lines):
    return [''.join([apply(c, r, lines) for r in range(len(lines[c]))]) for c in range(len(lines))]

def count_diffs(a, b):
    c = 0
    for i in range(0,len(a)):
        for j in range(0,len(a[0])):
            if a[i][j] != b[i][j]:
                c += 1
    return c

while True:
    n = apply_round(lines)
    if n == lines:
        print("done")
        break
    else:
        #print("found", count_diffs(n, lines), "diffs")
        #print('\n'.join(n))
        lines = n

print(sum([sum([1 for x in c if x == '#']) for c in n]))
